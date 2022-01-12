# -*- coding: utf-8 -*-
"""
>>> import os
>>> import json
>>> from samila import *
>>> from pytest import warns
>>> with warns(RuntimeWarning, match="Neither function nor data is provided."):
...     g = GenerativeImage()
>>> g = GenerativeImage(lambda x,y: 0, lambda x,y: 0)
>>> g.generate(step=0.1)
>>> result = g.save_data()
>>> with warns(RuntimeWarning, match="Just data is provided, generate method is not available in this mode."):
...     g_ = GenerativeImage(data=open('data.json', 'r'))
>>> g_.data1 == g.data1
True
>>> g_.data2 == g.data2
True
>>> with open('data.json', 'w') as fp:
...     json.dump({'data1': [0], 'data2': [0], 'matplotlib_version': '0'}, fp)
>>> with warns(RuntimeWarning, match=r"Source matplotlib version(.*) is different from yours, plots may be different."):
...     g = GenerativeImage(lambda x,y: 0, lambda x,y: 0, data=open('data.json', 'r'))
>>> os.remove('data.json')
"""
