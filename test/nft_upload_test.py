# -*- coding: utf-8 -*-
"""
>>> import os
>>> import math
>>> import random
>>> from samila import GenerativeImage, Projection
>>> def f1(x,y):
...    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
...    return result
>>> def f2(x,y):
...    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
...    return result
>>> g = GenerativeImage(f1,f2)
>>> g.generate()
>>> g.plot()
>>> NFT_STORAGE_API_KEY = os.environ["NFT_STORAGE_API_KEY"]
>>> g.generate()
>>> g.plot()
>>> result = g.nft_storage(api_key=NFT_STORAGE_API_KEY)
>>> print(NFT_STORAGE_API_KEY[:6])
>>> result["status"]
True
"""
