# -*- coding: utf-8 -*-
"""
>>> import random
>>> import math
>>> import os
>>> import pickle
>>> import socket
>>> def guard(*args, **kwargs):
...     raise Exception("No internet connection!")
>>> from samila import GenerativeImage, Projection
>>> from samila.functions import is_same_data
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
>>> with open("test/test1_1_d1.pkl", "rb") as fp:
...    temp_data = pickle.load(fp)
>>> is_same_data(g.data1, temp_data)
True
>>> with open("test/test1_1_d2.pkl", "rb") as fp:
...    temp_data = pickle.load(fp)
>>> is_same_data(g.data2, temp_data)
True
>>> g.plot()
>>> result = g.save_image("test.png")
>>> result["status"]
True
>>> result["message"]
'Everything seems good.'
>>> g.plot(color='red')
>>> g.plot(color='red', bgcolor='black')
>>> result = g.save_image("test2.png", depth=5)
>>> result["status"]
True
>>> result["message"]
'Everything seems good.'
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
>>> g = GenerativeImage(f1,f2)
>>> result = g.nft_storage(api_key="")
>>> result["status"]
False
>>> result["message"]
'No figure was found. First run `generate` and `plot` methods.'
>>> result = g.save_image(file_adr="")
>>> result["status"]
False
>>> result["message"]
'No figure was found. First run `generate` and `plot` methods.'
>>> g.fig = 2
>>> result = g.nft_storage(api_key="")
>>> result['status']
False
>>> result = g.save_image(file_adr="")
>>> result["status"]
False
>>> socket.socket = guard
>>> g.generate()
>>> g.plot(color=2,bgcolor=2)
>>> result = g.nft_storage("")
>>> result["status"]
False
>>> result["message"]
'No internet connection!'
>>> result = g.save_data(file_adr="")
>>> result["status"]
False
>>> def f1(x, y):
...    return math.cos(x**2*y) ** 1.926 - math.floor(x-y) ** 1.861 - math.floor(y**2*x)**1.688

>>> def f2(x, y):
...    return x - y**1.617 - math.ceil(y) ** 1.477 - abs(x**2 * y) ** 1.647 - math.cos(x*y)**1.668
>>> g = GenerativeImage(f1, f2)
>>> g.generate(seed=755398)
>>> all(map(lambda x: x.real == x, g.data1))
True
>>> all(map(lambda x: x.real == x, g.data2))
True
>>> result = g.save_data()
>>> result["status"]
True
>>> os.remove("test.png")
>>> os.remove("test2.png")
>>> os.remove("data.json")
"""
