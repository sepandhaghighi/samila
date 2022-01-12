# -*- coding: utf-8 -*-
"""
>>> import os
>>> import math
>>> import random
>>> import time
>>> from samila import GenerativeImage, Projection
>>> from samila.params import VALID_COLORS
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
>>> random_projection = random.choice(list(Projection))
>>> random_color = random.choice(VALID_COLORS)
>>> random_bgcolor = random.choice(VALID_COLORS)
>>> g.plot(projection=random_projection,color=random_color,bgcolor=random_bgcolor)
>>> counter = 0
>>> try_limit = 5
>>> status = False
>>> while(status == False and counter<try_limit):
...     result = g.nft_storage(api_key=NFT_STORAGE_API_KEY)
...     counter = counter + 1
...     status = result["status"]
...     time.sleep(5)
>>> status
True
"""
