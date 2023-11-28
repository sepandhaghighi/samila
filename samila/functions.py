# -*- coding: utf-8 -*-
"""Samila functions."""

import sys
import requests
import io
import os
import re
import json
import random
import matplotlib
from PIL import Image
from .params import SAMILA_VERSION
from .params import DEFAULT_MARKER, DEFAULT_START, DEFAULT_STOP, DEFAULT_STEP, DEFAULT_COLOR, DEFAULT_IMAGE_SIZE, DEFAULT_DEPTH
from .params import DEFAULT_CMAP_NAME, DEFAULT_CMAP_RANGE, DEFAULT_ROTATION
from .params import DEFAULT_BACKGROUND_COLOR, DEFAULT_SPOT_SIZE, DEFAULT_PROJECTION, DEFAULT_ALPHA, DEFAULT_LINEWIDTH
from .params import Projection, Marker, VALID_COLORS, HEX_COLOR_PATTERN, NFT_STORAGE_API, OVERVIEW
from .params import DATA_TYPE_ERROR, DATA_FORMAT_ERROR, CONFIG_TYPE_ERROR, CONFIG_FORMAT_ERROR, PLOT_DATA_ERROR, CONFIG_NO_STR_FUNCTION_ERROR
from .params import NO_FIG_ERROR_MESSAGE, FIG_SAVE_SUCCESS_MESSAGE, NFT_STORAGE_SUCCESS_MESSAGE, SAVE_NO_DATA_ERROR
from .params import INVALID_COLOR_TYPE_ERROR, COLOR_SIZE_ERROR
from .params import BOTH_COLOR_COMPLEMENT_WARNING, COLOR_NOT_FOUND_WARNING
from .params import DATA_SAVE_SUCCESS_MESSAGE, SEED_LOWER_BOUND, SEED_UPPER_BOUND
from .params import ELEMENTS_LIST, ARGUMENTS_LIST, OPERATORS_LIST, RANDOM_COEF_LIST
from .params import RANDOM_EQUATION_MIN_COMPLEXITY, RANDOM_EQUATION_MAX_COMPLEXITY, RANDOM_EQUATION_FOF_MIN_DEPTH, RANDOM_EQUATION_FOF_MAX_DEPTH
from .errors import samilaDataError, samilaPlotError, samilaConfigError
from warnings import warn


def random_equation_gen():
    """
    Generate random equation.

    :return: equation as str
    """
    num_elements = random.randint(
        RANDOM_EQUATION_MIN_COMPLEXITY,
        RANDOM_EQUATION_MAX_COMPLEXITY)
    result = ""
    index = 1
    random_coef = random.choice(RANDOM_COEF_LIST)
    while index <= num_elements:
        element = random.choice(ARGUMENTS_LIST)
        fof_depth = random.randint(
            RANDOM_EQUATION_FOF_MIN_DEPTH,
            RANDOM_EQUATION_FOF_MAX_DEPTH)
        for _ in range(fof_depth):
            element = random.choice(ELEMENTS_LIST).format(random_coef, element)
        result = result + element
        if index < num_elements:
            result = result + random.choice(OPERATORS_LIST)
        index = index + 1
    if random.randint(0, 1) == 1:
        result = random.choice(ELEMENTS_LIST).format(random_coef, result)
    return result


def random_hex_color_gen():
    """
    Generate random hex color code.

    :return: color code as str
    """
    random_color = "#%06x" % random.randint(0, 0xFFFFFF)
    return random_color


def float_range(start, stop, step):
    """
    Generate float range.

    :param start: start point
    :type start: float
    :param stop: stop point
    :type step: float
    :param step: step
    :type step: float
    :return: yield result
    """
    while start < stop:
        yield float(start)
        start += step


def distance_calc(s1, s2):
    """
    Calculate Levenshtein distance between two words.

    :param s1: first string
    :type s1 : str
    :param s2: second string
    :type s2 : str
    :return: distance between two string

    References :
    1- https://stackoverflow.com/questions/2460177/edit-distance-in-python
    2- https://en.wikipedia.org/wiki/Levenshtein_distance
    """
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(
                    1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


def is_valid_color(color):
    """
    Check that input color format is valid or not.

    :param color: given color
    :type color: any format
    :return: result as bool
    """
    if color is None:
        return True
    try:
        _ = matplotlib.colors.to_hex(color)
        return True
    except ValueError:
        return False


def color_complement(color):
    """
    Calculate complement color.

    :param color: given color (hex format)
    :type color: str
    :return: complement color (hex format) as str
    """
    color = color[1:]
    color = int(color, 16)
    comp_color = 0xFFFFFF ^ color
    comp_color = "#%06x" % comp_color
    return comp_color


def filter_color(color, bgcolor):
    """
    Filter given color and bgcolor.

    :param color: given color
    :type color: any format
    :param bgcolor: given background color
    :type bgcolor: any format
    :return: filtered version of color and bgcolor
    """
    color = select_color(color)
    bgcolor = select_color(bgcolor)
    if color == "COMPLEMENT" and bgcolor == "COMPLEMENT":
        warn(BOTH_COLOR_COMPLEMENT_WARNING, RuntimeWarning)
        return None, None
    if color == "COMPLEMENT":
        bgcolor = matplotlib.colors.to_hex(bgcolor)
        color = color_complement(bgcolor)
    if bgcolor == "COMPLEMENT":
        color = matplotlib.colors.to_hex(color)
        bgcolor = color_complement(color)
    return color, bgcolor


def get_cmap(name=DEFAULT_CMAP_NAME, lut=256):
    """
    Get colormap.

    :param name: colormap name
    :type name: str
    :param lut: look up table for colormap
    :type lut: int
    :return: desired colormap
    """
    try:
        return matplotlib.colormaps.get_cmap(name)
    except BaseException:  # pragma: no cover
        return matplotlib.cm.get_cmap(name, lut)


def filter_cmap(cmap):
    """
    Filter given cmap.

    :param cmap: color map
    :type cmap: matplotlib.colors.Colormap or list of colors
    :return: filtered version of cmap
    """
    if isinstance(cmap, str):
        cmap = get_cmap(cmap, 256)
    if type(cmap) == matplotlib.colors.Colormap:
        cmap = get_cmap(cmap.__getattribute__("name"))
    if isinstance(cmap, matplotlib.colors.ListedColormap):
        return cmap
    if isinstance(cmap, (matplotlib.colors.LinearSegmentedColormap)):
        cmap = cmap(range(DEFAULT_CMAP_RANGE))
        return matplotlib.colors.ListedColormap(cmap)
    if isinstance(cmap, list):
        cmap = list(map(select_color, cmap))
        return matplotlib.colors.ListedColormap(cmap)
    return None


def select_color(color):
    """
    Select color and return it.

    :param color: given color
    :type color: any format
    :return: color
    """
    if isinstance(color, str):
        if color.upper() == "TRANSPARENT":
            return "TRANSPARENT"
        if color.upper() == "COMPLEMENT":
            return "COMPLEMENT"
        if color.upper() == "RANDOM":
            return random_hex_color_gen()
        if re.match(HEX_COLOR_PATTERN, color):
            return color.lower()
        distance_list = list(map(lambda x: distance_calc(color, x),
                                 VALID_COLORS))
        min_distance = min(distance_list)
        most_similar_color = VALID_COLORS[distance_list.index(min_distance)]
        if min_distance != 0:
            warn(
                COLOR_NOT_FOUND_WARNING.format(
                    color,
                    most_similar_color),
                RuntimeWarning)
        return most_similar_color
    if is_valid_color(color):
        return color
    raise samilaPlotError(INVALID_COLOR_TYPE_ERROR)


def set_background(bgcolor, fig, ax):
    """
    Set background for figure and axis.

    :param bgcolor: given background color
    :type bgcolor: any format
    :param fig: figure
    :type fig: matplotlib.figure.Figure
    :param ax: axis
    :type ax: matplotlib.axes._subplots.AxesSubplot
    :return: None
    """
    if bgcolor == "TRANSPARENT":
        ax.patch.set_visible(False)
        fig.patch.set_visible(False)
        return
    fig.set_facecolor(bgcolor)
    ax.set_facecolor(bgcolor)
    return


def filter_projection(projection):
    """
    Filter given projection.

    :param projection: given projection
    :type projection: Projection enum
    :return: filtered version of projection
    """
    if isinstance(projection, Projection):
        projection_value = projection.value
        if projection_value == "random":
            projection_list = list(Projection)
            projection_list.remove(Projection.RANDOM)
            projection_value = random.choice(projection_list).value
        return projection_value
    return None


def filter_marker(marker):
    """
    Filter given marker.

    :param marker: given marker
    :type marker: Marker enum
    :return: filtered version of marker
    """
    if isinstance(marker, Marker):
        marker_value = marker.value
        if marker_value == "random":
            marker_list = list(Marker)
            marker_list.remove(Marker.RANDOM)
            marker_value = random.choice(marker_list).value
        return marker_value
    return None


def filter_float(value):
    """
    Filter given float value.

    :param value: given value
    :type value: float
    :return: filtered version of value
    """
    if isinstance(value, (float, int)):
        return value
    return None


def filter_size(size):
    """
    Filter given image size.

    :param value: given size
    :type value: tuple of float
    :return: filtered version of size
    """
    if isinstance(size, tuple):
        if not any(map(lambda x: x != filter_float(x), size)):
            return size
    return None


def rotate(fig, ax, rotation):
    """
    Rotate the given figure and return axis.

    :param fig: figure containing the image
    :type fig: Figure
    :param ax: axis on which rotated image is ploted
    :type ax: Axis
    :param rotation: desired rotation (in degrees)
    :type rotation: float
    :return: axis containing rotated image
    """
    if rotation != DEFAULT_ROTATION:
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        ax.cla()
        with Image.open(buf) as im:
            ax.imshow(im.rotate(rotation))
        ax.set_axis_off()
        ax.patch.set_zorder(-1)
        ax.add_artist(ax.patch)
    return ax


def plot_params_filter(
        g,
        color=None,
        bgcolor=None,
        cmap=None,
        spot_size=None,
        size=None,
        projection=None,
        marker=None,
        alpha=None,
        linewidth=None,
        rotation=None):
    """
    Filter plot method parameters.

    :param g: generative image instance
    :type g: GenerativeImage
    :param color: point colors
    :type color: str
    :param bgcolor: background color
    :type bgcolor: str
    :param cmap: color map
    :type cmap: matplotlib.colors.Colormap or list of colors
    :param spot_size: point spot size
    :type spot_size: float
    :param size: figure size
    :type size: tuple
    :param projection: projection type
    :type projection: str
    :param marker: marker type
    :type marker: str
    :param alpha: point transparency
    :type alpha: float
    :param linewidth: width of line
    :type linewidth: float
    :param rotation: desired rotation (in degrees)
    :type rotation: float
    :return: None
    """
    if g.data1 is None:
        raise samilaPlotError(PLOT_DATA_ERROR.format(1))
    if g.data2 is None:
        raise samilaPlotError(PLOT_DATA_ERROR.format(2))
    if isinstance(color, list):
        if len(color) != len(g.data1):
            raise samilaPlotError(COLOR_SIZE_ERROR)
        bgcolor = select_color(bgcolor)
    else:
        color, bgcolor = filter_color(color, bgcolor)
    cmap = filter_cmap(cmap)
    projection = filter_projection(projection)
    marker = filter_marker(marker)
    alpha = filter_float(alpha)
    linewidth = filter_float(linewidth)
    spot_size = filter_float(spot_size)
    size = filter_size(size)
    if color is None:
        color = g.color
    if bgcolor is None:
        bgcolor = g.bgcolor
    if cmap is None:
        cmap = g.cmap
    if spot_size is None:
        spot_size = g.spot_size
    if size is None:
        size = g.size
    if projection is None:
        projection = g.projection
    if marker is None:
        marker = g.marker
    if alpha is None:
        alpha = g.alpha
    if linewidth is None:
        linewidth = g.linewidth
    if rotation is None:
        rotation = g.rotation
    g.color, g.bgcolor, g.cmap, g.spot_size, g.size, g.projection, g.marker, g.alpha, g.linewidth, g.rotation = \
        color, bgcolor, cmap, spot_size, size, projection, marker, alpha, linewidth, rotation


def generate_params_filter(
        g,
        seed=None,
        start=None,
        step=None,
        stop=None):
    """
    Filter generate method parameters.

    :param g: generative image instance
    :type g: GenerativeImage
    :param seed: random seed
    :type seed: int
    :param start: range start point
    :type start: float
    :param step: range step size
    :type step: float
    :param stop: range stop point
    :type stop: float
    :return: None
    """
    start, step, stop = map(filter_float, [start, step, stop])
    if start is None:
        start = g.start
    if step is None:
        step = g.step
    if stop is None:
        stop = g.stop
    if seed is None:
        seed = g.seed
        if g.seed is None:
            seed = random.randint(SEED_LOWER_BOUND, SEED_UPPER_BOUND)
    g.seed, g.start, g.step, g.stop = seed, start, step, stop


def save_params_filter(g, depth=None):
    """
    Filter save_image method parameters.

    :param depth: depth of image
    :type depth: float
    :return: None
    """
    if depth is None:
        depth = g.depth
    g.depth = depth


def _GI_initializer(g, function1, function2):
    """
    Initialize the generative image.

    :param g: generative image instance
    :type g: GenerativeImage
    :param function1: function 1
    :type function1: python or lambda function
    :param function2: function 2
    :type function2: python or lambda function
    :return: None
    """
    g.__version__ = SAMILA_VERSION
    g.matplotlib_version = matplotlib.__version__
    g.python_version = get_python_version()
    g.function1 = function1
    g.function1_str = None
    g.function2 = function2
    g.function2_str = None
    g.fig = None
    g.seed = None
    g.start = DEFAULT_START
    g.step = DEFAULT_STEP
    g.stop = DEFAULT_STOP
    g.data1 = None
    g.data2 = None
    g.color = DEFAULT_COLOR
    g.bgcolor = DEFAULT_BACKGROUND_COLOR
    g.cmap = get_cmap()
    g.spot_size = DEFAULT_SPOT_SIZE
    g.size = DEFAULT_IMAGE_SIZE
    g.projection = DEFAULT_PROJECTION
    g.marker = DEFAULT_MARKER
    g.alpha = DEFAULT_ALPHA
    g.linewidth = DEFAULT_LINEWIDTH
    g.rotation = DEFAULT_ROTATION
    g.depth = DEFAULT_DEPTH
    g.missed_points_number = 0


def nft_storage_upload(api_key, data, timeout, gateway):
    """
    Upload file to nft.storage.

    :param api_key: API key
    :type api_key: str
    :param data: image data
    :type data: binary
    :param timeout: upload timeout (in seconds)
    :type timeout: int
    :param gateway: IPFS gateway
    :type gateway: Gateway enum
    :return: result as dict
    """
    result = {"status": True, "message": NFT_STORAGE_SUCCESS_MESSAGE}
    try:
        headers = {'Authorization': 'Bearer {0}'.format(api_key)}
        response = requests.post(
            url=NFT_STORAGE_API,
            data=data,
            headers=headers,
            timeout=timeout)
        response_json = response.json()
        if response_json["ok"]:
            result["message"] = gateway.value.format(
                response_json['value']['cid'])
            return result
        result["status"] = False
        result["message"] = response_json["error"]["message"]
        return result
    except Exception as e:
        result["status"] = False
        result["message"] = str(e)
        return result


def save_data_file(g, file_adr):
    """
    Save data as file.

    :param g: generative image instance
    :type g: GenerativeImage
    :param file_adr: file address
    :type file_adr: str
    :return: result as dict
    """
    data = get_data(g)
    result = {"status": True, "message": DATA_SAVE_SUCCESS_MESSAGE}
    try:
        with open(file_adr, 'w') as fp:
            json.dump(data, fp)
        result["message"] = os.path.abspath(file_adr)
    except Exception as e:
        result["status"] = False
        result["message"] = str(e)
    return result


def get_python_version():
    """
    Get Python's version.

    :return: python's version as 'major.minor'
    """
    return "{}.{}".format(
        sys.version_info.major,
        sys.version_info.minor
    )


def get_data(g):
    """
    Return data.

    :param g: generative image instance
    :type g: GenerativeImage
    :return: data as a dict
    """
    data = {}
    if g.data1 is None or g.data2 is None:
        raise samilaDataError(SAVE_NO_DATA_ERROR)
    data['data1'] = g.data1
    data['data2'] = g.data2
    data['plot'] = {
        "color": g.color,
        "bgcolor": g.bgcolor,
        "cmap": _serialize_cmap(g.cmap),
        "spot_size": g.spot_size,
        "projection": g.projection,
        "marker": g.marker,
        "alpha": g.alpha,
        "linewidth": g.linewidth,
        "depth": g.depth,
        "rotation": g.rotation,
    }
    data['matplotlib_version'] = g.matplotlib_version
    data['python_version'] = g.python_version
    data['__version__'] = g.__version__
    return data


def get_config(g):
    """
    Return config.

    :param g: generative image instance
    :type g: GenerativeImage
    :return: config as a dict
    """
    config = {}
    if g.function1_str is None or g.function2_str is None:
        raise samilaConfigError(CONFIG_NO_STR_FUNCTION_ERROR)
    config['f1'] = g.function1_str
    config['f2'] = g.function2_str
    config['generate'] = {
        "seed": g.seed,
        "start": g.start,
        "step": g.step,
        "stop": g.stop
    }
    config['plot'] = {
        "color": g.color,
        "bgcolor": g.bgcolor,
        "cmap": _serialize_cmap(g.cmap),
        "spot_size": g.spot_size,
        "projection": g.projection,
        "marker": g.marker,
        "alpha": g.alpha,
        "linewidth": g.linewidth,
        "depth": g.depth,
        "rotation": g.rotation,
    }
    config['matplotlib_version'] = g.matplotlib_version
    config['python_version'] = g.python_version
    config['__version__'] = g.__version__
    return config


def save_config_file(g, file_adr):
    """
    Save config as file.

    :param g: generative image instance
    :type g: GenerativeImage
    :param file_adr: file address
    :type file_adr: str
    :return: result as dict
    """
    config = get_config(g)
    result = {"status": True, "message": DATA_SAVE_SUCCESS_MESSAGE}
    try:
        with open(file_adr, 'w') as fp:
            json.dump(config, fp, indent=4)
        result["message"] = os.path.abspath(file_adr)
    except Exception as e:
        result["status"] = False
        result["message"] = str(e)
    return result


def save_fig_file(figure, file_adr, depth):
    """
    Save figure as file.

    :param figure: matplotlib figure
    :type figure: matplotlib.figure.Figure
    :param file_adr: file address
    :type file_adr: str
    :param depth: image depth
    :type depth: float
    :return: result as dict
    """
    if figure is None:
        return {"status": False, "message": NO_FIG_ERROR_MESSAGE}
    result = {"status": True, "message": FIG_SAVE_SUCCESS_MESSAGE}
    try:
        figure.savefig(
            file_adr,
            dpi=depth * figure.dpi,
            facecolor=figure.get_facecolor(),
            edgecolor='none')
        result["message"] = os.path.abspath(file_adr)
        return result
    except Exception as e:
        result["status"] = False
        result["message"] = str(e)
        return result


def save_fig_buf(figure, depth):
    """
    Save figure as buffer.

    :param figure: matplotlib figure
    :type figure: matplotlib.figure.Figure
    :param depth: image depth
    :type depth: float
    :return: result as dict
    """
    if figure is None:
        return {"status": False, "message": NO_FIG_ERROR_MESSAGE}
    result = {
        "status": True,
        "message": FIG_SAVE_SUCCESS_MESSAGE,
        "buffer": None}
    try:
        buf = io.BytesIO()
        figure.savefig(
            buf,
            dpi=depth * figure.dpi,
            format='png',
            facecolor=figure.get_facecolor(),
            edgecolor='none')
        result["buffer"] = buf
        return result
    except Exception as e:
        result["status"] = False
        result["message"] = str(e)
        return result


def samila_help():
    """
    Print samila details.

    :return: None
    """
    print(OVERVIEW)
    print("Website : https://www.samila.site")
    print("Repo : https://github.com/sepandhaghighi/samila")


def is_same_data(data1, data2, precision=10**-5):
    """
    Compare two data to be the same.

    :param data1: given data1
    :type data1: list
    :param data2: given data2
    :type data2: list
    :param precision: comparing precision
    :type precision: float
    :return: True if they are the same
    """
    if len(data1) != len(data2):
        return False
    is_same = map(lambda x, y: abs(x - y) < precision, data1, data2)
    return all(is_same)


def _serialize_color(color):
    """
    Serialize the given color to a json serializable object.

    :param color: given color
    :type color: str or nd.array
    :return: the serializable version of the color
    """
    if isinstance(color, str):
        return color
    return list(color)


def _serialize_cmap(cmap):
    """
    Serialize the cmap for saving.

    :param cmap: color map
    :type cmap: matplotlib.colors.Colormap
    :return: list of colors
    """
    return list(map(_serialize_color, cmap.colors))


def _load_cmap(config):
    """
    Load the cmap from config.

    :param config: plot part configuration
    :type config: dict or json
    :return: ListedColormap from cmap
    """
    if "cmap" not in config:
        return get_cmap()
    cmap = config["cmap"]
    return matplotlib.colors.ListedColormap(cmap)


def load_data(g, data):
    """
    Load data file.

    :param g: generative image instance
    :type g: GenerativeImage
    :param data: prior generated data
    :type data: (io.IOBase & file)
    :return: None
    """
    if isinstance(data, io.IOBase):
        data = json.load(data)
        g.data1 = data.get('data1')
        g.data2 = data.get('data2')
        if g.data1 is None or g.data2 is None:
            raise samilaDataError(DATA_FORMAT_ERROR)
        if 'matplotlib_version' in data:
            g.matplotlib_version = data['matplotlib_version']
        if 'python_version' in data:
            g.python_version = data['python_version']
        if '__version__' in data:
            g.__version__ = data['__version__']
        plot_config = data.get("plot")
        if plot_config is not None:
            g.color = plot_config.get("color", DEFAULT_COLOR)
            g.bgcolor = plot_config.get("bgcolor", DEFAULT_BACKGROUND_COLOR)
            g.cmap = _load_cmap(plot_config)
            g.spot_size = plot_config.get("spot_size", DEFAULT_SPOT_SIZE)
            g.projection = plot_config.get("projection", DEFAULT_PROJECTION)
            g.marker = plot_config.get("marker", DEFAULT_MARKER)
            g.alpha = plot_config.get("alpha", DEFAULT_ALPHA)
            g.linewidth = plot_config.get("linewidth", DEFAULT_LINEWIDTH)
            g.depth = plot_config.get("depth", DEFAULT_DEPTH)
            g.rotation = plot_config.get("rotation", DEFAULT_ROTATION)
        return
    raise samilaDataError(DATA_TYPE_ERROR)


def load_config(g, config):
    """
    Load config file.

    :param g: generative image instance
    :type g: GenerativeImage
    :param config: config JSON file
    :type config: (io.IOBase & file)
    :return: None
    """
    if isinstance(config, io.IOBase):
        config = json.load(config)
        g.function1_str = config.get("f1")
        g.function2_str = config.get("f2")
        if g.function1_str is None or g.function2_str is None:
            raise samilaConfigError(CONFIG_FORMAT_ERROR)
        if 'matplotlib_version' in config:
            g.matplotlib_version = config['matplotlib_version']
        if 'python_version' in config:
            g.python_version = config['python_version']
        if '__version__' in config:
            g.__version__ = config['__version__']
        generate_config = config.get("generate")
        if generate_config is not None:
            g.seed = generate_config.get("seed")
            g.start = generate_config.get("start", DEFAULT_START)
            g.step = generate_config.get("step", DEFAULT_STEP)
            g.stop = generate_config.get("stop", DEFAULT_STOP)
        plot_config = config.get("plot")
        if plot_config is not None:
            g.color = plot_config.get("color", DEFAULT_COLOR)
            g.bgcolor = plot_config.get("bgcolor", DEFAULT_BACKGROUND_COLOR)
            g.cmap = _load_cmap(plot_config)
            g.spot_size = plot_config.get("spot_size", DEFAULT_SPOT_SIZE)
            g.projection = plot_config.get("projection", DEFAULT_PROJECTION)
            g.marker = plot_config.get("marker", DEFAULT_MARKER)
            g.alpha = plot_config.get("alpha", DEFAULT_ALPHA)
            g.linewidth = plot_config.get("linewidth", DEFAULT_LINEWIDTH)
            g.depth = plot_config.get("depth", DEFAULT_DEPTH)
            g.rotation = plot_config.get("rotation", DEFAULT_ROTATION)
        return
    raise samilaConfigError(CONFIG_TYPE_ERROR)
