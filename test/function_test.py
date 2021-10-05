# -*- coding: utf-8 -*-
"""
>>> import random
>>> import math
>>> from samila import GenerativeImage, Projection
>>> from samila.functions import isSimilarData
>>> import pickle
>>> def f1(x,y):
...    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
...    return result
>>> def f2(x,y):
...    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
...    return result
>>> g = GenerativeImage(f1,f2)
>>> g.function1 == f1
True
>>> g.function2 == f2
True
>>> g.fig
>>> g.generate()
>>> isinstance(g.data1, list)
True
>>> isinstance(g.data2, list)
True
>>> g.generate(seed=10, start=-2*math.pi, step=0.1, stop=math.pi/2)
>>> g.seed
10
>>> isSimilarData(g.data1, "test/test1_1_d1.pkl")
True
>>> isSimilarData(g.data2, "test/test1_1_d2.pkl")
True
>>> g.plot()
>>> g.plot(color='red')
>>> g.plot(color='red', bgcolor='black')
>>> from samila import GenerativeImage, Projection
>>> g.plot(projection=Projection.POLAR, color='red', bgcolor='black')
>>> g.plot(projection=Projection.POLAR, color=(.1, .2, .8))
>>> g.plot(bgcolor=(.1, .2, .8), spot_size=0.1)
>>> g.plot(size=(20, 20))
>>> result = g.nft_storage(api_key="")
>>> result['status']
False
>>> result['message']
'API Key is missing, make sure the `Authorization` header has a value in the following format `Bearer {api key}`.'
"""
