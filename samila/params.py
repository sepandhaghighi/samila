# -*- coding: utf-8 -*-
"""Samila params."""
import math
from enum import Enum
from matplotlib import colors as mcolors

SAMILA_VERSION = "0.2"  # pragma: no cover

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
NO_FIG_ERROR_MESSAGE = "No figure was found. First run `generate` and `plot` methods."


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
