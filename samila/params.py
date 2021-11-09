# -*- coding: utf-8 -*-
"""Samila params."""
import math
from enum import Enum
from matplotlib import colors as mcolors

SAMILA_VERSION = "0.3"  # pragma: no cover

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
DEFAULT_PROJECTION = None
VALID_COLORS = list(dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS).keys())
NFT_STORAGE_API = "https://api.nft.storage/upload"
NFT_STORAGE_SUCCESS_MESSAGE = "Everything seems good."
FIG_SAVE_SUCCESS_MESSAGE = "Everything seems good."
DATA_SAVE_SUCCESS_MESSAGE = "Everything seems good."
NO_FIG_ERROR_MESSAGE = "No figure was found. First run `generate` and `plot` methods."
DATA_TYPE_ERROR = "Provided data file is not supported. It should be either file or io.IOBase."
DATA_PARSING_ERROR = "Provided data format is wrong. It should be in JSON format including data1 and data2 fields."
NO_FUNCTION_ERROR = "At least one of the given functions are None."
JUST_DATA_WARNING = "Just data is provided, generate method is not available in this mode."
NOTHING_PROVIDED_WARNING = "Neither function nor data is provided."
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
