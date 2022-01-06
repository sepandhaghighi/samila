# -*- coding: utf-8 -*-
"""Samila functions."""

import requests
import io
import json
import random
import matplotlib
from .params import DEFAULT_START, DEFAULT_STOP, DEFAULT_STEP, DEFAULT_COLOR, DEFAULT_IMAGE_SIZE
from .params import DEFAULT_BACKGROUND_COLOR, DEFAULT_SPOT_SIZE, DEFAULT_PROJECTION
from .params import Projection, VALID_COLORS, NFT_STORAGE_API, OVERVIEW
from .params import DATA_TYPE_ERROR, CONFIG_TYPE_ERROR, PLOT_DATA_ERROR, CONFIG_NO_STR_FUNCTION_ERROR
from .params import NO_FIG_ERROR_MESSAGE, FIG_SAVE_SUCCESS_MESSAGE, NFT_STORAGE_SUCCESS_MESSAGE, SAVE_NO_DATA_ERROR
from .params import DATA_SAVE_SUCCESS_MESSAGE, SEED_LOWER_BOUND, SEED_UPPER_BOUND
from .params import ELEMENTS_LIST, ARGUMENTS_LIST, OPERATORS_LIST
from .errors import samilaDataError, samilaPlotError, samilaConfigError


def random_equation_gen():
    """
    Generate random equation.

    :return: equation as str
    """
    num_elements = random.randint(2, len(ELEMENTS_LIST) + 3)
    result = ""
    index = 1
    random_coef = "random.uniform(-1,1)"
    while(index <= num_elements):
        argument = random.choice(ARGUMENTS_LIST)
        result = result + \
            random.choice(ELEMENTS_LIST).format(random_coef, argument)
        if index < num_elements:
            result = result + random.choice(OPERATORS_LIST)
        index = index + 1
    return result


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


def filter_color(color):
    """
    Filter given color and return it.

    :param color: given color
    :type color: str or tuple
    :return: filtered version of color
    """
    if isinstance(color, tuple):
        return color
    if isinstance(color, str):
        distance_list = list(map(lambda x: distance_calc(color, x),
                                 VALID_COLORS))
        min_distance = min(distance_list)
        return VALID_COLORS[distance_list.index(min_distance)]
    return None


def filter_projection(projection):
    """
    Filter given projection.

    :param projection: given projection
    :type projection: Projection enum
    :return: filtered version of projection
    """
    if isinstance(projection, Projection):
        return projection.value
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


def plot_params_filter(
        g,
        color=None,
        bgcolor=None,
        spot_size=None,
        size=None,
        projection=None):
    """
    Filter plot method parameters.

    :param g: generative image instance
    :type g: GenerativeImage
    :param color: point colors
    :type color: str
    :param bgcolor: background color
    :type bgcolor: str
    :param spot_size: point spot size
    :type spot_size: float
    :param size: figure size
    :type size: tuple
    :param projection: projection type
    :type projection: str
    :return: None
    """
    if g.data1 is None:
        raise samilaPlotError(PLOT_DATA_ERROR.format(1))
    if g.data2 is None:
        raise samilaPlotError(PLOT_DATA_ERROR.format(2))
    color, bgcolor = map(filter_color, [color, bgcolor])
    projection = filter_projection(projection)
    spot_size = filter_float(spot_size)
    size = filter_size(size)
    if color is None:
        color = g.color
    if bgcolor is None:
        bgcolor = g.bgcolor
    if spot_size is None:
        spot_size = g.spot_size
    if size is None:
        size = g.size
    if projection is None:
        projection = g.projection
    g.color, g.bgcolor, g.spot_size, g.size, g.projection = color, bgcolor, spot_size, size, projection


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
    g.matplotlib_version = matplotlib.__version__
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
    g.spot_size = DEFAULT_SPOT_SIZE
    g.size = DEFAULT_IMAGE_SIZE
    g.projection = DEFAULT_PROJECTION


def nft_storage_upload(api_key, data):
    """
    Upload file to nft.storage.

    :param api_key: API key
    :type api_key: str
    :param data: image data
    :type data: binary
    :return: result as dict
    """
    result = {"status": True, "message": NFT_STORAGE_SUCCESS_MESSAGE}
    try:
        headers = {'Authorization': 'Bearer {0}'.format(api_key)}
        response = requests.post(
            url=NFT_STORAGE_API,
            data=data,
            headers=headers)
        response_json = response.json()
        if response_json["ok"]:
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
    matplotlib_version = matplotlib.__version__
    data = {}
    if g.data1 is None or g.data2 is None:
        raise samilaDataError(SAVE_NO_DATA_ERROR)
    data['data1'] = g.data1
    data['data2'] = g.data2
    data['plot'] = {
        "color": g.color,
        "bgcolor": g.bgcolor,
        "spot_size": g.spot_size,
        "projection": g.projection
    }
    data['matplotlib_version'] = matplotlib_version
    result = {"status": True, "message": DATA_SAVE_SUCCESS_MESSAGE}
    try:
        with open(file_adr, 'w') as fp:
            json.dump(data, fp)
    except Exception as e:
        result["status"] = False
        result["message"] = str(e)
    return result


def save_config_file(g, file_adr):
    """
    Save config as file.

    :param g: generative image instance
    :type g: GenerativeImage
    :param file_adr: file address
    :type file_adr: str
    :return: result as dict
    """
    matplotlib_version = matplotlib.__version__
    data = {}
    if g.function1_str is None or g.function2_str is None:
        raise samilaConfigError(CONFIG_NO_STR_FUNCTION_ERROR)
    data['f1'] = g.function1_str
    data['f2'] = g.function2_str
    data['generate'] = {
        "seed": g.seed,
        "start": g.start,
        "step": g.step,
        "stop": g.stop
    }
    data['plot'] = {
        "color": g.color,
        "bgcolor": g.bgcolor,
        "spot_size": g.spot_size,
        "projection": g.projection
    }
    data['matplotlib_version'] = matplotlib_version
    result = {"status": True, "message": DATA_SAVE_SUCCESS_MESSAGE}
    try:
        with open(file_adr, 'w') as fp:
            json.dump(data, fp, indent=4)
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
        return result
    except Exception as e:
        result["status"] = False
        result["message"] = str(e)
        return result


def save_fig_buf(figure):
    """
    Save figure as buffer.

    :param figure: matplotlib figure
    :type figure: matplotlib.figure.Figure
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
    is_same = map(lambda x, y: abs(x - y) < precision, data1, data2)
    return all(is_same)


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
        if 'matplotlib_version' in data:
            g.matplotlib_version = data['matplotlib_version']
        plot_config = data.get("plot")
        if plot_config is not None:
            g.color = plot_config.get("color", DEFAULT_COLOR)
            g.bgcolor = plot_config.get("bgcolor", DEFAULT_BACKGROUND_COLOR)
            g.spot_size = plot_config.get("spot_size", DEFAULT_SPOT_SIZE)
            g.projection = plot_config.get("projection", DEFAULT_PROJECTION)
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
        data = json.load(config)
        g.function1_str = data.get("f1")
        g.function2_str = data.get("f2")
        if 'matplotlib_version' in data:
            g.matplotlib_version = data['matplotlib_version']
        generate_config = data.get("generate")
        if generate_config is not None:
            g.seed = generate_config.get("seed")
            g.start = generate_config.get("start", DEFAULT_START)
            g.step = generate_config.get("step", DEFAULT_STEP)
            g.stop = generate_config.get("stop", DEFAULT_STOP)
        plot_config = data.get("plot")
        if plot_config is not None:
            g.color = plot_config.get("color", DEFAULT_COLOR)
            g.bgcolor = plot_config.get("bgcolor", DEFAULT_BACKGROUND_COLOR)
            g.spot_size = plot_config.get("spot_size", DEFAULT_SPOT_SIZE)
            g.projection = plot_config.get("projection", DEFAULT_PROJECTION)
        return
    raise samilaConfigError(CONFIG_TYPE_ERROR)
