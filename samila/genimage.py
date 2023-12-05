# -*- coding: utf-8 -*-
"""Samila generative image."""
import json
import random
import gc
import itertools
import matplotlib
import matplotlib.pyplot as plt
from .functions import _GI_initializer, plot_params_filter, generate_params_filter, save_params_filter
from .functions import get_config, get_data, get_python_version
from .functions import float_range, save_data_file, save_fig_file, save_fig_buf, save_config_file
from .functions import load_data, load_config, random_equation_gen, nft_storage_upload
from .functions import set_background, rotate
from .params import *
from warnings import warn, catch_warnings, simplefilter


class GenerativeImage:
    """
    Generative Image class.

    >>> def f1(x, y):
    ...    return random.uniform(-1, 1) * x**2 - math.sin(y**3)
    >>> def f2(x, y):
    ...    return random.uniform(-1, 1) * y**3 - math.cos(x**2)
    >>> GI = GenerativeImage(f1, f2)
    """

    def __init__(
            self,
            function1=None,
            function2=None,
            data=None,
            config=None,
            func_seed=None):
        """
        Init method.

        :param function1: function 1
        :type function1: python or lambda function
        :param function2: function 2
        :type function2: python or lambda function
        :param data: prior generated data
        :type data: (io.IOBase & file)
        :param config: generative image config
        :type config: (io.IOBase & file)
        :param func_seed: random seed for function generation
        :type func_seed: Any
        """
        _GI_initializer(self, function1, function2)
        if config is not None:
            load_config(self, config)
        elif data is not None:
            load_data(self, data)
        if self.matplotlib_version != matplotlib.__version__ or \
           self.python_version != get_python_version() or \
           self.__version__ != SAMILA_VERSION:
            warn(
                VERSION_WARNING.format(
                    self.matplotlib_version,
                    self.python_version,
                    self.__version__),
                RuntimeWarning)
        if func_seed is not None:
            random.seed(func_seed)
        if self.function1 is None:
            if self.function1_str is None:
                self.function1_str = random_equation_gen()
            self.function1 = eval("lambda x,y:" + self.function1_str)
        if self.function2 is None:
            if self.function2_str is None:
                self.function2_str = random_equation_gen()
            self.function2 = eval("lambda x,y:" + self.function2_str)

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
        generate_params_filter(self, seed, start, step, stop)
        self.data1 = []
        self.data2 = []
        self.missed_points_number = 0
        range1 = list(float_range(self.start, self.stop, self.step))
        range_prod = itertools.product(range1, range1)
        for point in range_prod:
            random.seed(self.seed)
            try:
                data1_ = self.function1(point[0], point[1]).real
                data2_ = self.function2(point[0], point[1]).real
                self.data1.append(data1_)
                self.data2.append(data2_)
            except Exception:
                self.missed_points_number += 1
        if len(self.data1) < (len(range1) ** 2):
            warn(CALCULATION_EXCEPTION_WARNING, RuntimeWarning)

    def plot(
            self,
            color=None,
            bgcolor=None,
            cmap=None,
            spot_size=None,
            size=None,
            projection=None,
            marker=None,
            alpha=None,
            linewidth=None,
            rotation=None):
        """
        Plot the generated art.

        :param color: point colors
        :type color: str
        :param bgcolor: background color
        :type bgcolor: str
        :param cmap: color map
        :type cmap: matplotlib.colors.Colormap or list of colors
        :param spot_size: point spot size
        :type spot_size: float
        :param size: figure size
        :type size: tuple
        :param projection: projection type
        :type projection: str
        :param marker: marker type
        :type marker: str
        :param alpha: point transparency
        :type alpha: float
        :param linewidth: width of line
        :type linewidth: float
        :param rotation: desired rotation (in degrees)
        :type rotation: float
        :return: None
        """
        plot_params_filter(
            self,
            color,
            bgcolor,
            cmap,
            spot_size,
            size,
            projection,
            marker,
            alpha,
            linewidth,
            rotation)
        fig = plt.figure()
        fig.set_size_inches(self.size[0], self.size[1])
        ax = fig.add_subplot(111, projection=self.projection)
        set_background(self.bgcolor, fig, ax)
        with catch_warnings():
            simplefilter("ignore")
            ax.scatter(
                self.data2,
                self.data1,
                alpha=self.alpha,
                c=self.color,
                cmap=self.cmap,
                s=self.spot_size,
                lw=self.linewidth,
                marker=self.marker)
        ax.set_axis_off()
        ax.patch.set_zorder(-1)
        ax.add_artist(ax.patch)
        ax = rotate(fig, ax, self.rotation)
        self.fig = fig

    def nft_storage(
            self,
            api_key,
            upload_data=False,
            upload_config=False,
            depth=None,
            timeout=3000,
            gateway=Gateway.IPFS_IO):
        """
        Upload image to nft.storage.

        :param api_key: API key
        :type api_key: str
        :param upload_data: upload data flag
        :type upload_data: bool
        :param upload_config: upload config flag
        :type upload_config: bool
        :param depth: image depth
        :type depth: float
        :param timeout: upload timeout (in seconds)
        :type timeout: int
        :param gateway: IPFS gateway
        :type gateway: Gateway enum
        :return: result as dict
        """
        save_params_filter(self, depth)
        response = save_fig_buf(self.fig, self.depth)
        if not response["status"]:
            return {"status": False, "message": response["message"]}
        buf = response["buffer"]
        response = nft_storage_upload(
            api_key=api_key,
            data=buf.getvalue(),
            timeout=timeout,
            gateway=gateway)
        if upload_config == False and upload_data == False:
            return response
        result = {key: {'image': value} for key, value in response.items()}
        if upload_config:
            response = nft_storage_upload(
                api_key=api_key,
                data=json.dumps(get_config(self)),
                timeout=timeout,
                gateway=gateway)
            for key, value in response.items():
                result[key]['config'] = value
        if upload_data:
            response = nft_storage_upload(
                api_key=api_key,
                data=json.dumps(get_data(self)),
                timeout=timeout,
                gateway=gateway)
            for key, value in response.items():
                result[key]['data'] = value
        return result

    def save_image(self, file_adr, depth=None):
        """
        Save generated image.

        :param file_adr: file address
        :type file_adr: str
        :param depth: image depth
        :type depth: float
        :return: result as dict
        """
        save_params_filter(self, depth)
        return save_fig_file(self.fig, file_adr, self.depth)

    def save_data(self, file_adr='data.json'):
        """
        Save data into a file.

        :param file_adr: file address
        :type file_adr: str
        :return: result as dict
        """
        return save_data_file(self, file_adr)

    def save_config(self, file_adr='config.json'):
        """
        Save config into a file.

        :param file_adr: file address
        :type file_adr: str
        :return: result as a dict
        """
        return save_config_file(self, file_adr)

    def __del__(self):
        """
        Destructor.

        :return:None
        """
        try:
            del self.data1
            del self.data2
            if self.fig is not None:
                self.fig.clf()
                plt.close(self.fig)
            gc.collect()
        except Exception:
            gc.collect()
