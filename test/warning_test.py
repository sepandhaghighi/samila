# -*- coding: utf-8 -*-
"""
>>> import os
>>> from samila import *
>>> from pytest import warns
>>> with warns(RuntimeWarning, match="Neither function nor data is provided."):
...     g = GenerativeImage()
>>> g = GenerativeImage(lambda x,y: 0, lambda x,y: 0)
>>> g.generate(step=0.1)
>>> result = g.save_data()
>>> with warns(RuntimeWarning, match="Just data is provided you can't use generate function."):
...     g_ = GenerativeImage(data=open('data.json', 'r'))
>>> g_.data1 == g.data1
True
>>> g_.data2 == g.data2
True
>>> os.remove('data.json')
"""
