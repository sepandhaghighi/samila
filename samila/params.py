# -*- coding: utf-8 -*-
"""Samila params."""
import math
from enum import Enum
from matplotlib import colors as mcolors

SAMILA_VERSION = "0.1"  # pragma: no cover

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
NFT_STORAGE_SUCCESS_MESSAGE = "Everything seems good"



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
