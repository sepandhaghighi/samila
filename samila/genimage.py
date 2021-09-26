# -*- coding: utf-8 -*-
"""Samila generative image."""
import random
import itertools
import matplotlib.pyplot as plt
from .functions import float_range
from .params import *

class GenerativeImage:

    def __init__(self, function1, function2):
        self.function1 = function1
        self.function2 = function2

    def generate(self, seed=None, start=DEFAULT_START, step=DEFAULT_STEP, stop=DEFAULT_STOP):
        self.data1 = []
        self.data2 = []
        self.seed = seed
        random.seed(self.seed)
        range1 = list(float_range(start, stop, step))
        range2 = list(float_range(start, stop, step))
        range_prod = list(itertools.product(range1, range2))
        for item in range_prod:
            self.data1.append(self.function1(item[0], item[1]))
            self.data2.append(self.function2(item[0], item[1]))

    def plot(self, color=DEFAULT_COLOR, spot_size=DEFAULT_SPOT_SIZE, size=DEFAULT_IMAGE_SIZE, projection=DEFAULT_PROJECTION):
        fig = plt.figure()
        fig.set_size_inches(size[0], size[1])
        ax = fig.add_subplot(111, projection=projection)
        ax.scatter(self.data2, self.data1, alpha=0.1, c=color, s=spot_size)
        ax.axis('off')


