# -*- coding: utf-8 -*-
"""Samila params."""
import math
from enum import Enum
import matplotlib

SAMILA_VERSION = "1.2"  # pragma: no cover

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
DEFAULT_CMAP_NAME = "viridis"
DEFAULT_CMAP_RANGE = 256
DEFAULT_ALPHA = 0.1
DEFAULT_LINEWIDTH = 1.5
DEFAULT_IMAGE_SIZE = (10, 10)
DEFAULT_SPOT_SIZE = 0.01
DEFAULT_DEPTH = 1
DEFAULT_ROTATION = 0.0
DEFAULT_PROJECTION = "rectilinear"
DEFAULT_MARKER = "."
SEED_LOWER_BOUND = 0
SEED_UPPER_BOUND = 2**20
VALID_COLORS = list(
    dict(
        matplotlib.colors.BASE_COLORS,
        **matplotlib.colors.CSS4_COLORS))
HEX_COLOR_PATTERN = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
NFT_STORAGE_API = "https://api.nft.storage/upload"
NFT_STORAGE_SUCCESS_MESSAGE = "Everything seems good."
FIG_SAVE_SUCCESS_MESSAGE = "Everything seems good."
DATA_SAVE_SUCCESS_MESSAGE = "Everything seems good."
NO_FIG_ERROR_MESSAGE = "No figure was found. First run `generate` and `plot` methods."
DATA_TYPE_ERROR = "Provided data file is not supported. It should be either file or io.IOBase."
DATA_FORMAT_ERROR = "Provided data file is not supported. It should include data1 and data2."
CONFIG_TYPE_ERROR = "Provided config file is not supported. It should be either file or io.IOBase."
CONFIG_FORMAT_ERROR = "Provided config file is not supported. It should include f1 and f2."
CONFIG_NO_STR_FUNCTION_ERROR = "Config file can't be saved. At least one of the function1_str or function2_str is None."
PLOT_DATA_ERROR = "Plotting process can't be Done because data{0} is empty. Use generate method first."
COLOR_SIZE_ERROR = "Color list size is not equal to the data size."
SAVE_NO_DATA_ERROR = "Data file can't be saved. At least one of the data1 or data2 is None."
INVALID_COLOR_TYPE_ERROR = "Given color/bgcolor type is not supported."
VERSION_WARNING = "Your plots may differ as the version of matplotlib ({0}), Python ({1}), or Samila ({2}) that you are using is not the same as the source."
CALCULATION_EXCEPTION_WARNING = "The given functions are undefined at some points. Your plot may not be complete."
BOTH_COLOR_COMPLEMENT_WARNING = "It is not possible to set color and bgcolor to 'complement' at the same time! Both are automatically set to the previous or default selection."
COLOR_NOT_FOUND_WARNING = "color '{0}' not found. Replacing it with '{1}'"


class Gateway(Enum):
    """
    IPFS gateway class.

    >>> import samila
    >>> gateway = samila.Gateway.IPFS_IO
    """

    CID = "{0}"
    IPFS_IO = "https://ipfs.io/ipfs/{0}"
    GATEWAY_IPFS_IO = "https://gateway.ipfs.io/ipfs/{0}"
    VIA0 = "https://via0.com/ipfs/{0}"
    CLOUDFLARE_IPFS = "https://cloudflare-ipfs.com/ipfs/{0}"
    HARDBIN = "https://hardbin.com/ipfs/{0}"
    PINATA = "https://gateway.pinata.cloud/ipfs/{0}"
    JORROPO = "https://jorropo.net/ipfs/{0}"
    DWEB = "https://dweb.link/ipfs/{0}"
    BEST_PRACTICE = "https://ipfs.best-practice.se/ipfs/{0}"
    RUNFISSION = "https://ipfs.runfission.com/ipfs/{0}"
    ARAGON_NETWORK = "https://ipfs.eth.aragon.network/ipfs/{0}"
    TEXTILE = "https://hub.textile.io/ipfs/{0}"
    EVERLAND = "https://{0}.ipfs.4everland.io"
    CF_IPFS = "https://{0}.ipfs.cf-ipfs.com"
    LITNET = "https://ipfs.litnet.work/ipfs/{0}"
    JPU = "https://ipfs.jpu.jp/ipfs/{0}"
    CZIP = "https://ipfs.czip.it/ipfs/{0}"
    W3S = "https://{0}.ipfs.w3s.link"
    GW3 = "https://{0}.ipfs.gw3.io"


class Projection(Enum):
    """
    Samila Projection type class.

    >>> import samila
    >>> projection = samila.Projection.POLAR
    """

    DEFAULT = DEFAULT_PROJECTION
    POLAR = "polar"
    AITOFF = "aitoff"
    HAMMER = "hammer"
    LAMBERT = "lambert"
    MOLLWEIDE = "mollweide"
    RECTILINEAR = "rectilinear"
    RANDOM = "random"


class Marker(Enum):
    """
    Samila Marker type class.

    >>> import samila
    >>> marker = samila.Marker.POINT
    """

    DEFAULT = DEFAULT_MARKER
    POINT = "."
    PIXEL = ","
    CIRCLE = "o"
    TRIANGLE_DOWN = "v"
    TRIANGLE_UP = "^"
    TRIANGLE_LEFT = "<"
    TRIANGLE_RIGHT = ">"
    TRI_DOWN = "1"
    TRI_UP = "2"
    TRI_LEFT = "3"
    TRI_RIGHT = "4"
    OCTAGON = "8"
    SQUARE = "s"
    PENTAGON = "p"
    PLUS = "+"
    PLUS_FILLED = "P"
    STAR = "*"
    HEXAGON_VERTICAL = "h"
    HEXAGON_HORIZONTAL = "H"
    X = "x"
    X_FILLED = "X"
    DIAMOND = "D"
    DIAMON_THIN = "d"
    VLINE = "|"
    HLINE = "_"
    RANDOM = "random"


RANDOM_COEF_LIST = [
    "random.uniform(-1,1)",
    "random.gauss(0,1)",
    "random.betavariate(1,1)",
    "random.gammavariate(1,1)",
    "random.lognormvariate(0,1)"]

ELEMENTS_LIST = [
    "{0}*math.atan({1})",
    "{0}*math.asinh({1})",
    "{0}*math.acosh(abs({1})+1)",
    "{0}*math.erf({1})",
    "{0}*math.sqrt(abs({1}))",
    "{0}*math.log(abs({1})+1)",
    "{0}*math.tanh({1})",
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
    "1/x",
    "1/y",
    "x/y",
    "y-x",
    "x-y",
    "x+y",
    "x**3",
    "y**3",
    "x**2",
    "y**2",
    "(x**2)*y",
    "(y**2)*x",
    "(y**2)+(x**2)",
    "(y**2)-(x**2)",
    "(x**2)*(y**3)",
    "(x**3)*(y**2)",
    "x*(y**3)",
    "y*(x**3)"]

OPERATORS_LIST = ["+", "-", "*", "/"]

RANDOM_EQUATION_MAX_COMPLEXITY = len(ELEMENTS_LIST) + 1

RANDOM_EQUATION_MIN_COMPLEXITY = 1

RANDOM_EQUATION_FOF_MAX_DEPTH = 2

RANDOM_EQUATION_FOF_MIN_DEPTH = 1
