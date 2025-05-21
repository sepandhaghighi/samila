# -*- coding: utf-8 -*-
"""Samila generative image."""
from typing import List, Tuple, Dict, Callable
from typing import Union, Iterable
from typing import Any
import random
import io
import gc
import itertools
import matplotlib
import matplotlib.pyplot as plt
from .functions import _GI_initializer, plot_params_filter, generate_params_filter, save_params_filter
from .functions import get_python_version
from .functions import float_range, save_data_file, save_fig_file, save_config_file
from .functions import load_data, load_config, random_equation_gen
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
            function1: Callable = None,
            function2: Callable = None,
            data: io.IOBase = None,
            config: io.IOBase = None,
            func_seed: Any = None) -> None:
        """
        Init method.

        :param function1: function 1
        :param function2: function 2
        :param data: prior generated data
        :param config: generative image config
        :param func_seed: random seed for function generation
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
            seed: int = None,
            start: float = None,
            step: float = None,
            stop: float = None,
            mode: GenerateMode = None) -> None:
        """
        Generate a raw format of art.

        :param seed: random seed
        :param start: range start point
        :param step: range step size
        :param stop: range stop point
        :param mode: generate mode
        """
        generate_params_filter(self, seed, start, step, stop, mode)
        self.data1 = []
        self.data2 = []
        self.missed_points_number = 0
        range1 = list(float_range(self.start, self.stop, self.step))
        range_prod = itertools.product(range1, range1)
        for index, point in enumerate(range_prod):
            random.seed(self.seed)
            try:
                if self.generate_mode == GenerateMode.F1_VS_F2.value:
                    data1_ = self.function1(point[0], point[1]).real
                    data2_ = self.function2(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.F2_VS_F1.value:
                    data2_ = self.function1(point[0], point[1]).real
                    data1_ = self.function2(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.F2_VS_INDEX.value:
                    data2_ = index
                    data1_ = self.function2(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.F1_VS_INDEX.value:
                    data2_ = index
                    data1_ = self.function1(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.INDEX_VS_F1.value:
                    data1_ = index
                    data2_ = self.function1(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.INDEX_VS_F2.value:
                    data1_ = index
                    data2_ = self.function2(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.F1_VS_X1.value:
                    data1_ = self.function1(point[0], point[1]).real
                    data2_ = point[0]
                elif self.generate_mode == GenerateMode.F2_VS_X1.value:
                    data1_ = self.function2(point[0], point[1]).real
                    data2_ = point[0]
                elif self.generate_mode == GenerateMode.F1_VS_X2.value:
                    data1_ = self.function1(point[0], point[1]).real
                    data2_ = point[1]
                elif self.generate_mode == GenerateMode.F2_VS_X2.value:
                    data1_ = self.function2(point[0], point[1]).real
                    data2_ = point[1]
                elif self.generate_mode == GenerateMode.X1_VS_F1.value:
                    data1_ = point[0]
                    data2_ = self.function1(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.X1_VS_F2.value:
                    data1_ = point[0]
                    data2_ = self.function2(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.X2_VS_F1.value:
                    data1_ = point[1]
                    data2_ = self.function1(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.X2_VS_F2.value:
                    data1_ = point[1]
                    data2_ = self.function2(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.F1F2_VS_F1.value:
                    data1_ = self.function1(point[0], point[1]).real * self.function2(point[0], point[1]).real
                    data2_ = self.function1(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.F1F2_VS_F2.value:
                    data1_ = self.function1(point[0], point[1]).real * self.function2(point[0], point[1]).real
                    data2_ = self.function2(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.F1_VS_F1F2.value:
                    data1_ = self.function1(point[0], point[1]).real
                    data2_ = self.function1(point[0], point[1]).real * self.function2(point[0], point[1]).real
                elif self.generate_mode == GenerateMode.F2_VS_F1F2.value:
                    data1_ = self.function2(point[0], point[1]).real
                    data2_ = self.function1(point[0], point[1]).real * self.function2(point[0], point[1]).real
                self.data1.append(data1_)
                self.data2.append(data2_)
            except Exception:
                self.missed_points_number += 1
        if len(self.data1) < (len(range1) ** 2):
            warn(CALCULATION_EXCEPTION_WARNING, RuntimeWarning)

    def plot(
            self,
            color: Union[str, Iterable[str]] = None,
            bgcolor: Union[str, Iterable[str]] = None,
            cmap: Union[matplotlib.colors.Colormap, List]=None,
            spot_size: float=None,
            size: Tuple[float, float]=None,
            projection: Projection = None,
            marker: Marker = None,
            alpha: float = None,
            linewidth: float = None,
            rotation: float = None) -> None:
        """
        Plot the generated art.

        :param color: point colors
        :param bgcolor: background color
        :param cmap: color map
        :param spot_size: point spot size
        :param size: figure size
        :param projection: projection type
        :param marker: marker type
        :param alpha: point transparency
        :param linewidth: width of line
        :param rotation: desired rotation (in degrees)
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

    def save_image(self, file_adr: str, depth: float = None) -> Dict[str, Any]:
        """
        Save generated image.

        :param file_adr: file address
        :param depth: image depth
        """
        save_params_filter(self, depth)
        return save_fig_file(self.fig, file_adr, self.depth)

    def save_data(self, file_adr: str = 'data.json') -> Dict[str, Any]:
        """
        Save data into a file.

        :param file_adr: file address
        """
        return save_data_file(self, file_adr)

    def save_config(self, file_adr: str = 'config.json') -> Dict[str, Any]:
        """
        Save config into a file.

        :param file_adr: file address
        """
        return save_config_file(self, file_adr)

    def __del__(self) -> None:
        """Destructor."""
        try:
            del self.data1
            del self.data2
            if self.fig is not None:
                self.fig.clf()
                plt.close(self.fig)
            gc.collect()
        except Exception:
            gc.collect()
