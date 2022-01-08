# -*- coding: utf-8 -*-
"""Samila params."""
import math
from enum import Enum
from matplotlib import colors as mcolors

SAMILA_VERSION = "0.4"  # pragma: no cover

OVERVIEW = '''
Samila is a generative art generator written in Python, Samila let's you
create arts based on many thousand points. The position of every single
point is calculated by a formula, which has random parameters.
Because of the random numbers, every image looks different.
'''

DEFAULT_START = -1 * math.pi
DEFAULT_STOP = math.pi
DEFAULT_STEP = 0.01
DEFAULT_COLOR = "black"
DEFAULT_BACKGROUND_COLOR = "white"
DEFAULT_ALPHA = 0.1
DEFAULT_IMAGE_SIZE = (10, 10)
DEFAULT_SPOT_SIZE = 0.01
DEFAULT_PROJECTION = "rectilinear"
SEED_LOWER_BOUND = 0
SEED_UPPER_BOUND = 2**20
VALID_COLORS = list(dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS).keys())
NFT_STORAGE_API = "https://api.nft.storage/upload"
NFT_STORAGE_SUCCESS_MESSAGE = "Everything seems good."
FIG_SAVE_SUCCESS_MESSAGE = "Everything seems good."
DATA_SAVE_SUCCESS_MESSAGE = "Everything seems good."
NO_FIG_ERROR_MESSAGE = "No figure was found. First run `generate` and `plot` methods."
DATA_TYPE_ERROR = "Provided data file is not supported. It should be either file or io.IOBase."
CONFIG_TYPE_ERROR = "Provided config file is not supported. It should be either file or io.IOBase."
CONFIG_NO_STR_FUNCTION_ERROR = "Config file can't be saved. At least one of the function1_str or function2_str is None."
PLOT_DATA_ERROR = "Plotting process can't be Done because data{0} is empty. Use generate method first."
SAVE_NO_DATA_ERROR = "Data file can't be saved. At least one of the data1 or data2 is None."
MATPLOTLIB_VERSION_WARNING = "Source matplotlib version({0}) is different from yours, plots may be different."


class Projection(Enum):
    """
    Samila Projection type class.

    >>> projection = samila.Projection.POLAR
    """

    DEFAULT = DEFAULT_PROJECTION
    POLAR = "polar"
    AITOFF = "aitoff"
    HAMMER = "hammer"
    LAMBERT = "lambert"
    MOLLWEIDE = "mollweide"
    RECTILINEAR = "rectilinear"


ELEMENTS_LIST = [
    "{0}*math.cos({1})",
    "{0}*math.sin({1})",
    "{0}*{1}",
    "{0}*abs({1})",
    "{0}*math.ceil({1})",
    "{0}*math.floor({1})"]

ARGUMENTS_LIST = [
    "x*y",
    "x",
    "y",
    "y-x",
    "x-y",
    "x+y",
    "x**2",
    "y**2",
    "(x**2)*y",
    "(y**2)*x",
    "(x**2)*(y**3)",
    "(x**3)*(y**2)",
    "x*(y**3)",
    "y*(x**3)"]

OPERATORS_LIST = ["+", "-"]
