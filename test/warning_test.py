# -*- coding: utf-8 -*-
"""
>>> import os
>>> import json
>>> from samila import *
>>> from pytest import warns
>>> g = GenerativeImage(lambda x,y: 0, lambda x,y: 0)
>>> g.generate(step=0.1)
>>> result = g.save_data()
>>> g_ = GenerativeImage(data=open('data.json', 'r'))
>>> g_.data1 == g.data1
True
>>> g_.data2 == g.data2
True
>>> with open('data.json', 'w') as fp:
...     json.dump({'data1': [0], 'data2': [0], 'matplotlib_version': '0'}, fp)
>>> with warns(RuntimeWarning, match=r"Source matplotlib version(.*) is different from yours, plots may be different."):
...     g = GenerativeImage(lambda x,y: 0, lambda x,y: 0, data=open('data.json', 'r'))
>>> with open('config.json', 'w') as fp:
...     json.dump({'f1': 'x', 'f2': 'y', 'matplotlib_version': '0'}, fp)
>>> with warns(RuntimeWarning, match=r"Source matplotlib version(.*) is different from yours, plots may be different."):
...     g = GenerativeImage(config=open('config.json', 'r'))
>>> g = GenerativeImage(lambda x, y: 1 / x, lambda x, y: 1 / (y - 1))
>>> with warns(RuntimeWarning, match=r"The given functions are undefined at some points. Your plot may not be complete."):
...     g.generate(start=0, stop=2, step=0.1)
>>> with warns(RuntimeWarning, match=r"It is not possible to set color and bgcolor to 'complement' at the same time! Both are automatically set to the previous or default selection."):
...     g.plot(color='complement', bgcolor='complement')
>>> with warns(RuntimeWarning, match=r"color 'rad' not found. Replacing it with 'red'"):
...     g.plot(color='rad')
>>> os.remove('data.json')
>>> os.remove('config.json')
"""
