# -*- coding: utf-8 -*-
"""
>>> from samila import *
>>> import os
>>> import json
>>> from pytest import warns
>>> g = GenerativeImage(data="data.json")
Traceback (most recent call last):
        ...
samila.errors.samilaDataError: Provided data file is not supported. It should be either file or io.IOBase.
>>> g = GenerativeImage(config="config.json")
Traceback (most recent call last):
        ...
samila.errors.samilaConfigError: Provided config file is not supported. It should be either file or io.IOBase.
>>> g = GenerativeImage(lambda x,y: 0, lambda x,y: 0)
>>> g.generate(step=0.1)
>>> result = g.save_data('data.json')
>>> g = GenerativeImage(data=open('data.json', 'r'))
>>> g.generate()
>>> from samila import *
>>> g = GenerativeImage()
>>> g.plot()
Traceback (most recent call last):
        ...
samila.errors.samilaPlotError: Plotting process can't be Done because data1 is empty. Use generate method first.
>>> with open("data.json", 'w') as fp:
...     json.dump({'data1': [0]}, fp)
>>> g = GenerativeImage(data=open('data.json', 'r'))
>>> g.save_data()
Traceback (most recent call last):
        ...
samila.errors.samilaDataError: Data file can't be saved. At least one of the data1 or data2 is None.
>>> g.plot()
Traceback (most recent call last):
        ...
samila.errors.samilaPlotError: Plotting process can't be Done because data2 is empty. Use generate method first.
>>> g.generate()
>>> g.plot(color=(1, 2, 3, 4, 5))
Traceback (most recent call last):
        ...
samila.errors.samilaPlotError: Given color/bgcolor type is not supported.
>>> g = GenerativeImage(lambda x,y: x, lambda x,y: y)
>>> result = g.save_config()
Traceback (most recent call last):
        ...
samila.errors.samilaConfigError: Config file can't be saved. At least one of the function1_str or function2_str is None.
>>> from samila.functions import *
>>> select_color(2)
Traceback (most recent call last):
        ...
samila.errors.samilaPlotError: Given color/bgcolor type is not supported.
>>> filter_color(2,2)
Traceback (most recent call last):
        ...
samila.errors.samilaPlotError: Given color/bgcolor type is not supported.
>>> g.plot(color=2, bgcolor=2)
Traceback (most recent call last):
        ...
samila.errors.samilaPlotError: Given color/bgcolor type is not supported.
>>> os.remove('data.json')
"""
