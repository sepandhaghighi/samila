# -*- coding: utf-8 -*-
"""Samila generative image."""
import random
import itertools
import matplotlib.pyplot as plt
from .functions import float_range, filter_color, filter_projection
from .params import *


class GenerativeImage:

    def __init__(self, function1, function2):
        self.function1 = function1
        self.function2 = function2

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
            self.data1.append(self.function1(item[0], item[1]))
            self.data2.append(self.function2(item[0], item[1]))

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
        color = filter_color(color) if not None else DEFAULT_COLOR
        bgcolor = filter_color(
            bgcolor) if not None else DEFAULT_BACKGROUND_COLOR
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
