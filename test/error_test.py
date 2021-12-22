# -*- coding: utf-8 -*-
"""
>>> from samila import *
>>> import os
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
>>> os.remove('data.json')
"""
