# -*- coding: utf-8 -*-
"""Samila generative image."""
import random
import itertools
import matplotlib
import matplotlib.pyplot as plt
from .functions import _GI_initializer, plot_params_filter, generate_params_filter
from .functions import float_range, save_data_file, save_fig_file, save_fig_buf, save_config_file
from .functions import load_data, load_config, random_equation_gen, nft_storage_upload
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

    def __init__(self, function1=None, function2=None, data=None, config=None):
        """
        Init method.

        :param function1: Function 1
        :type function1: python or lambda function
        :param function2: Function 2
        :type function2: python or lambda function
        :param data: prior generated data
        :type data: (io.IOBase & file)
        :param config: generative image configs
        :type config: JSON
        """
        _GI_initializer(self)
        self.function1 = function1
        self.function1_str = None
        self.function2 = function2
        self.function2_str = None
        self.fig = None
        if config is not None:
            matplotlib_version = load_config(self, config)
            if matplotlib_version != matplotlib.__version__:
                warn(MATPLOTLIB_VERSION_WARNING.format(
                    matplotlib_version), RuntimeWarning)
        if data is not None:
            matplotlib_version = load_data(self, data)
            if matplotlib_version != matplotlib.__version__:
                warn(MATPLOTLIB_VERSION_WARNING.format(
                    matplotlib_version), RuntimeWarning)
        if self.function1 is None:
            if self.function1_str is None:
                self.function1_str = random_equation_gen()
            self.function1 = eval("lambda x,y:" + self.function1_str)
        if self.function2 is None:
            if self.function2_str is None:
                self.function2_str = random_equation_gen()
            self.function2 = eval("lambda x,y:" + self.function1_str)

    def generate(
            self,
            seed=None,
            start=None,
            step=None,
            stop=None):
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
        seed, start, step, stop = generate_params_filter(
            self, seed, start, step, stop)
        self.seed = seed
        self.data1 = []
        self.data2 = []
        range1 = list(float_range(start, stop, step))
        range2 = list(float_range(start, stop, step))
        range_prod = list(itertools.product(range1, range2))
        for item in range_prod:
            random.seed(self.seed)
            self.data1.append(self.function1(item[0], item[1]).real)
            self.data2.append(self.function2(item[0], item[1]).real)

    def plot(
            self,
            color=None,
            bgcolor=None,
            spot_size=None,
            size=None,
            projection=None):
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
        color, bgcolor, spot_size, size, projection = plot_params_filter(
            self, color, bgcolor, spot_size, size, projection)
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

    def save_config(self, file_adr='config.json'):
        """
        Save config into a file.

        :param file_adr: file address
        :type file_adr: str
        :return: result as a dict
        """
        return save_config_file(self, matplotlib.__version__, file_adr)
