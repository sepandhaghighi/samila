# -*- coding: utf-8 -*-
"""Samila generative image."""
import random
import itertools
import matplotlib
import matplotlib.pyplot as plt
from .functions import float_range, filter_color, filter_projection, nft_storage_upload, save_data_file, save_fig_file, save_fig_buf, load_data
from .errors import samilaGenerateError
from .params import *
from warnings import warn


class GenerativeImage:
    """
    Generative Image class.

    >>> def f1(x, y):
    ...    return random.uniform(-1, 1) * x**2 - math.sin(y**3)
    >>> def f2(x, y):
    ...    return random.uniform(-1, 1) * y**3 - math.cos(x**2)
    >>> GI = GenerativeImage(f1, f2)
    """

    def __init__(self, function1=None, function2=None, data=None):
        """
        Init method.

        :param function1: Function 1
        :type function1: python or lambda function
        :param function2: Function 2
        :type function2: python or lambda function
        :param data: prior generated data
        :type data: (io.IOBase & file)
        """
        if function1 is None or function2 is None:
            if data is None:
                warn(NOTHING_PROVIDED_WARNING, RuntimeWarning)
            else:
                warn(JUST_DATA_WARNING, RuntimeWarning)
        if data is not None:
            self.data1, self.data2, matplotlib_version = load_data(data)
            if matplotlib_version != matplotlib.__version__:
                warn(MATPLOTLIB_VERSION_WARNING.format(matplotlib_version), RuntimeWarning)
        self.function1 = function1
        self.function2 = function2
        self.fig = None

    def generate(
            self,
            seed=None,
            start=DEFAULT_START,
            step=DEFAULT_STEP,
            stop=DEFAULT_STOP):
        """
        Generate a raw format of art.

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
        if self.function1 is None or self.function2 is None:
            raise samilaGenerateError(NO_FUNCTION_ERROR)
        self.data1 = []
        self.data2 = []
        self.seed = seed
        if seed is None:
            self.seed = random.randint(0, 2 ** 20)
        range1 = list(float_range(start, stop, step))
        range2 = list(float_range(start, stop, step))
        range_prod = list(itertools.product(range1, range2))
        for item in range_prod:
            random.seed(self.seed)
            self.data1.append(self.function1(item[0], item[1]).real)
            self.data2.append(self.function2(item[0], item[1]).real)

    def plot(
            self,
            color=DEFAULT_COLOR,
            bgcolor=DEFAULT_BACKGROUND_COLOR,
            spot_size=DEFAULT_SPOT_SIZE,
            size=DEFAULT_IMAGE_SIZE,
            projection=DEFAULT_PROJECTION):
        """
        Plot the generated art.

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
        color, bgcolor = map(filter_color, [color, bgcolor])
        if color is None:
            color = DEFAULT_COLOR
        if bgcolor is None:
            bgcolor = DEFAULT_BACKGROUND_COLOR
        projection = filter_projection(projection)
        fig = plt.figure()
        fig.set_size_inches(size[0], size[1])
        fig.set_facecolor(bgcolor)
        ax = fig.add_subplot(111, projection=projection)
        ax.set_facecolor(bgcolor)
        ax.scatter(
            self.data2,
            self.data1,
            alpha=DEFAULT_ALPHA,
            edgecolors=color,
            s=spot_size)
        ax.set_axis_off()
        ax.patch.set_zorder(-1)
        ax.add_artist(ax.patch)
        self.fig = fig

    def nft_storage(self, api_key):
        """
        Upload image to nft.storage.

        :param api_key: API key
        :type api_key: str
        :return: result as dict
        """
        response = save_fig_buf(self.fig)
        if not response["status"]:
            return {"status": False, "message": response["message"]}
        buf = response["buffer"]
        response = nft_storage_upload(api_key=api_key, data=buf.getvalue())
        return response

    def save_image(self, file_adr, depth=1):
        """
        Save generated image.

        :param file_adr: file address
        :type file_adr: str
        :param depth: image depth
        :type depth: float
        :return: result as dict
        """
        return save_fig_file(figure=self.fig, file_adr=file_adr, depth=depth)

    def save_data(self, file_adr='data.json'):
        """
        Save data into a file.

        :param file_adr: file address
        :type file_adr: str
        :return: result as dict
        """
        return save_data_file(
            self.data1,
            self.data2,
            matplotlib.__version__,
            file_adr)
