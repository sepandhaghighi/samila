# -*- coding: utf-8 -*-
"""Samila params."""
import math
from matplotlib import colors as mcolors

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
