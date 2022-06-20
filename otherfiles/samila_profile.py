# -*- coding: utf-8 -*-
"""Samila profile."""
from samila import *
import random
import math


def f1(x, y):
    result = random.uniform(-1, 1) * x**2 - math.sin(y**2) + abs(y-x)
    return result


def f2(x, y):
    result = random.uniform(-1, 1) * y**3 - math.cos(x**2) + 2*x
    return result

g = GenerativeImage(f1, f2)
g.generate(seed=200)
g.plot()
g.save_image("test.png")
