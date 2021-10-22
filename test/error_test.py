# -*- coding: utf-8 -*-
"""
>>> from samila import *
>>> import os
>>> from pytest import warns
>>> g = GenerativeImage(data="data.json")
Traceback (most recent call last):
        ...
samila.errors.samilaDataError: Provided data file is not supported. It should be either file or io.IOBase.
>>> with open('data.json', 'r') as fp:
...     fp.write('test')
>>> g = GenerativeImage(data="data.json")
        ...
samila.errors.samilaDataError: Provided data format is wrong. It should be in JSON format including data1 and data2 fields.
>>> g = GenerativeImage(lambda x,y: 0, lambda x,y: 0)
>>> g.generate(step=0.1)
>>> g.save_data('data.json')
>>> g = GenerativeImage(data="data.json")
>>> with warns(RuntimeWarning, match='Just data is provided you can't use generate function.'):
...     g = GenerativeImage(data=open('data.json', 'r'))
>>> g.generate()
samila.errors.samilaGenerateError: At least one of the given functions are None.
"""
