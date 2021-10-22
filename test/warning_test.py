# -*- coding: utf-8 -*-
"""
>>> import os
>>> from samila import *
>>> from pytest import warns
>>> with warns(RuntimeWarning, match='Neither function nor data is provided.'):
...     g = GenerativeImage()
>>> g = GenerativeImage(lambda x,y: 0, lambda x,y: 0)
>>> g.generate(seed=1018273, step=0.1)
>>> g.save_data()
>>> with warns(RuntimeWarning, match='Just data is provided you can't use generate function.'):
...     g = GenerativeImage(data=open('data.json', 'r'))
>>> os.remove('data.json')
"""