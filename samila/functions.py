# -*- coding: utf-8 -*-
"""Samila functions."""

import requests
import io
import json
import random
from .params import DEFAULT_START, DEFAULT_STOP, DEFAULT_STEP, DEFAULT_COLOR
from .params import DEFAULT_BACKGROUND_COLOR, DEFAULT_SPOT_SIZE, DEFAULT_PROJECTION
from .params import Projection, VALID_COLORS, NFT_STORAGE_API, OVERVIEW
from .params import DATA_TYPE_ERROR, DATA_PARSING_ERROR, CONFIG_TYPE_ERROR, NO_FIG_ERROR_MESSAGE
from .params import FIG_SAVE_SUCCESS_MESSAGE, NFT_STORAGE_SUCCESS_MESSAGE, DATA_SAVE_SUCCESS_MESSAGE
from .params import ELEMENTS_LIST, ARGUMENTS_LIST, OPERATORS_LIST
from .errors import samilaDataError, samilaConfigError


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
    if isinstance(value, float):
        return value
    return None


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


def save_data_file(data1, data2, matplotlib_version, file_adr):
    """
    Save data as file.

    :param data1: data 1
    :type data1: list
    :param data2: data 2
    :type data2: list
    :param matplotlib_version: matplotlib version
    :type matplotlib_version: str
    :param file_adr: file address
    :type file_adr: str
    :return: result as dict
    """
    data = {}
    data['data1'] = data1
    data['data2'] = data2
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
    data = {}
    if g.function1_str is not None:
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


def load_data(data):
    """
    Load data file.

    :param data: prior generated data
    :type data: (io.IOBase & file)
    :return: (data1, data2)
    """
    if isinstance(data, io.IOBase):
        try:
            data = json.load(data)
            return data['data1'], data['data2'], data['matplotlib_version']
        except Exception:
            raise samilaDataError(DATA_PARSING_ERROR)
    raise samilaDataError(DATA_TYPE_ERROR)


def load_config(g, config):
    """
    Load config file.
    
    :param config: config JSON file
    :type config: (io.IOBase & file)
    :return: None
    """
    if isinstance(config, io.IOBase):
        data = json.load(config)
        g.function1_str = data.get("f1")
        g.function2_str = data.get("f2")
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
