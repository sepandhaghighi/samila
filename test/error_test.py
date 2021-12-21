# -*- coding: utf-8 -*-
"""
>>> from samila import *
>>> import os
>>> from pytest import warns
>>> g = GenerativeImage(data="data.json")
Traceback (most recent call last):
        ...
samila.errors.samilaDataError: Provided data file is not supported. It should be either file or io.IOBase.
>>> g = GenerativeImage(data="config.json")
Traceback (most recent call last):
        ...
samila.errors.samilaConfigError: Provided config file is not supported. It should be either file or io.IOBase.
>>> with open('data.json', 'w') as fp:
...     result = fp.write('test')
>>> g = GenerativeImage(data=open("data.json", 'r'))
Traceback (most recent call last):
        ...
samila.errors.samilaDataError: Provided data format is wrong. It should be in JSON format including data1 and data2 fields.
>>> g = GenerativeImage(lambda x,y: 0, lambda x,y: 0)
>>> g.generate(step=0.1)
>>> result = g.save_data('data.json')
>>> g = GenerativeImage(data=open('data.json', 'r'))
>>> g.generate()
>>> os.remove('data.json')
"""
