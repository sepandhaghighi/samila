# -*- coding: utf-8 -*-
"""
>>> import random
>>> import math
>>> import os
>>> import pickle
>>> import socket
>>> import json
>>> import sys
>>> import matplotlib
>>> def guard(*args, **kwargs):
...     raise Exception("No internet connection!")
>>> from samila import GenerativeImage, Projection, Marker, GenerateMode
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
>>> g.python_version == '.'.join(sys.version.split()[0].split('.')[:2])
True
>>> g.fig
>>> g.generate()
>>> isinstance(g.data1, list)
True
>>> isinstance(g.data2, list)
True
>>> g.missed_points_number == 0
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
>>> isinstance(result["message"], str)
True
>>> g.plot(color='red')
>>> g.plot(color='red', bgcolor='black')
>>> result = g.save_image("test2.png", depth=5)
>>> result["status"]
True
>>> isinstance(result["message"], str)
True
>>> g.plot(projection=Projection.POLAR, color='red', bgcolor='black')
>>> g.color
'red'
>>> g.bgcolor
'black'
>>> g.plot(projection=Projection.POLAR, color='rod', bgcolor='blacc')
>>> g.color
'red'
>>> g.bgcolor
'black'
>>> g.plot(projection=Projection.POLAR, color="#EEE245", bgcolor="#000000")
>>> g.projection
'polar'
>>> g.color
'#eee245'
>>> g.bgcolor
'#000000'
>>> g.plot(projection=Projection.POLAR, color=(.1, .2, .8))
>>> g.color
(0.1, 0.2, 0.8)
>>> g.plot(projection=Projection.POLAR, color="#FFFFF1", bgcolor="complement")
>>> g.color
'#fffff1'
>>> g.bgcolor
'#00000e'
>>> g.plot(projection=Projection.POLAR, color="complement", bgcolor="#AAAAAA")
>>> g.color
'#555555'
>>> g.bgcolor
'#aaaaaa'
>>> g.plot(projection=Projection.POLAR, color="complement", bgcolor="complement", marker=Marker.X, spot_size=100)
>>> g.color
'#555555'
>>> g.bgcolor
'#aaaaaa'
>>> g.marker
'x'
>>> g.spot_size
100
>>> g.plot(rotation=45)
>>> int(g.rotation)
45
>>> g.plot(bgcolor=(.1, .2, .8), spot_size=0.1)
>>> g.plot(size=(20, 20))
>>> g.size
(20, 20)
>>> g.plot(alpha=0.5, linewidth=2.2)
>>> g.alpha
0.5
>>> g.linewidth
2.2
>>> random.seed(2)
>>> g.plot(color="random", bgcolor="random", projection=Projection.RANDOM, marker=Marker.RANDOM)
>>> color1, bgcolor1, projection1, marker1 = g.color, g.bgcolor, g.projection, g.marker
>>> random.seed(3)
>>> g.plot(color="random", bgcolor="random", projection=Projection.RANDOM, marker=Marker.RANDOM)
>>> color2, bgcolor2, projection2, marker2 = g.color, g.bgcolor, g.projection, g.marker
>>> color1 == color2
False
>>> bgcolor1 == bgcolor2
False
>>> projection1 == projection2
False
>>> marker1 == marker2
False
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
>>> g.plot()
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
>>> isinstance(result["message"], str)
True
>>> g = GenerativeImage()
>>> g.generate()
>>> g.plot(color="white", bgcolor="transparent")
>>> g.bgcolor == "TRANSPARENT"
True
>>> g.plot()
>>> result = g.save_config()
>>> result["status"]
True
>>> isinstance(result["message"], str)
True
>>> result = g.save_data()
>>> result["status"]
True
>>> isinstance(result["message"], str)
True
>>> g_ = GenerativeImage(config=open("config.json", 'r'))
>>> g_.seed == g.seed
True
>>> g_.function1_str == g.function1_str
True
>>> g_.function2_str == g.function2_str
True
>>> g.color == g_.color
True
>>> g.bgcolor == g_.bgcolor
True
>>> g.spot_size == g_.spot_size
True
>>> g.projection == g_.projection
True
>>> g.marker == g_.marker
True
>>> g.alpha == g_.alpha
True
>>> g.linewidth == g_.linewidth
True
>>> g.depth == g_.depth
True
>>> g_ = GenerativeImage(data=open("data.json", 'r'))
>>> g.color == g_.color
True
>>> g.bgcolor == g_.bgcolor
True
>>> g.spot_size == g_.spot_size
True
>>> g.projection == g_.projection
True
>>> g.marker == g_.marker
True
>>> g.rotation == g_.rotation
True
>>> g.alpha == g_.alpha
True
>>> g.linewidth == g_.linewidth
True
>>> g.depth == g_.depth
True
>>> g.plot(color="white", bgcolor="black", spot_size=2, projection=Projection.POLAR, marker=Marker.X, alpha=0.2, linewidth=1)
>>> result = g.save_config()
>>> result["status"]
True
>>> isinstance(result["message"], str)
True
>>> result = g.save_data()
>>> result["status"]
True
>>> isinstance(result["message"], str)
True
>>> g_ = GenerativeImage(config=open("config.json", 'r'))
>>> g_.seed == g.seed
True
>>> g_.function1_str == g.function1_str
True
>>> g_.function2_str == g.function2_str
True
>>> g.color == g_.color
True
>>> g.bgcolor == g_.bgcolor
True
>>> g.spot_size == g_.spot_size
True
>>> g.projection == g_.projection
True
>>> g.marker == g_.marker
True
>>> g.rotation == g_.rotation
True
>>> g.alpha == g_.alpha
True
>>> g.linewidth == g_.linewidth
True
>>> g.depth == g_.depth
True
>>> g_ = GenerativeImage(data=open("data.json", 'r'))
>>> g.color == g_.color
True
>>> g.bgcolor == g_.bgcolor
True
>>> g.spot_size == g_.spot_size
True
>>> g.projection == g_.projection
True
>>> g.marker == g_.marker
True
>>> g.alpha == g_.alpha
True
>>> g.linewidth == g_.linewidth
True
>>> g.depth == g_.depth
True
>>> with open("config.json", 'w') as fp:
...     json.dump({'f1': 'y', 'f2': 'x'}, fp)
>>> g = GenerativeImage(config=open("config.json", 'r'))
>>> g.function1_str
'y'
>>> g.function2_str
'x'
>>> result = g.save_config(file_adr="")
>>> result["status"]
False
>>> with open("data.json", 'w') as fp:
...     json.dump({'data1': [0], 'data2': [1]}, fp)
>>> g = GenerativeImage(data=open("data.json", 'r'))
>>> g.data1
[0]
>>> g.data2
[1]
>>> with open("data.json", 'w') as fp:
...     json.dump({'data1': [0], 'data2': [1], 'plot':{}}, fp)
>>> g = GenerativeImage(data=open("data.json", 'r'))
>>> with open("config.json", 'w') as fp:
...     json.dump({'f1': "x", 'f2': "y", 'plot':{}}, fp)
>>> g = GenerativeImage(config=open("config.json", 'r'))
>>> g = GenerativeImage()
>>> g.generate()
>>> cm = matplotlib.colors.Colormap(name="Purples")
>>> g.plot(cmap=cm)
>>> result = g.save_config("config.json")
>>> result["status"]
True
>>> g_ = GenerativeImage(config=open("config.json", 'r'))
>>> bool((g_.cmap.colors == g.cmap.colors).all())
True
>>> cm = ["black", [0.6, 0.2, 0.2, 1], [0.5, 0.2, 0.2, 1], [0.4, 0.2, 0.2, 1], "yellow", [0.2, 0.2, 0.2, 1],]
>>> g.plot(cmap=cm)
>>> result = g.save_config("config.json")
>>> result["status"]
True
>>> g_ = GenerativeImage(config=open("config.json", 'r'))
>>> g_.cmap.colors == g.cmap.colors
True
>>> g.plot(cmap="Purples")
>>> cm = matplotlib.colors.Colormap(name="viridis")
>>> g.plot(cmap=cm)
>>> cmap = [[0.7, 0.2, 0.2, 1], [0.6, 0.2, 0.2, 1], [0.3, 0.2, 0.2, 1], [0.2, 0.2, 0.2, 1]]
>>> g.plot(cmap=matplotlib.colors.ListedColormap(cmap))
>>> g = GenerativeImage()
>>> g.generate()
>>> g.plot(cmap=cmap, color=g.data1)
>>> result = g.save_data("data.json")
>>> result["status"]
True
>>> g_ = GenerativeImage(data=open("data.json", "r"))
>>> g_.plot()
>>> g_.cmap.colors == g.cmap.colors
True
>>> g.plot(color=g.data1)
>>> g_ = GenerativeImage()
>>> del(g)
>>> del g_.data1
>>> del(g_)
>>> g1 = GenerativeImage()
>>> function1 = eval("lambda x, y:" + g1.function1_str)
>>> function2 = eval("lambda x, y:" + g1.function2_str)
>>> g2 = GenerativeImage(function1=function1, function2=function2)
>>> g1.generate(seed=22)
>>> g2.generate(seed=22)
>>> is_same_data(g1.data1, g2.data1)
True
>>> is_same_data(g1.data2, g2.data2)
True
>>> len(g1.data1) > 0
True
>>> len(g1.data2) > 0
True
>>> del(g1)
>>> del(g2)
>>> random.seed(22)
>>> g = GenerativeImage()
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2)
>>> g_ = GenerativeImage(func_seed=22)
>>> g_.generate(start=-2*math.pi, step=0.1, stop=math.pi/2)
>>> g.function1_str == g_.function1_str
True
>>> g.function2_str == g_.function2_str
True
>>> random.seed(22)
>>> g = GenerativeImage()
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.F1_VS_INDEX)
>>> g.generate_mode == GenerateMode.F1_VS_INDEX.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.F2_VS_INDEX)
>>> g.generate_mode == GenerateMode.F2_VS_INDEX.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.INDEX_VS_F1)
>>> g.generate_mode == GenerateMode.INDEX_VS_F1.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.INDEX_VS_F2)
>>> g.generate_mode == GenerateMode.INDEX_VS_F2.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.F1_VS_F2)
>>> g.generate_mode == GenerateMode.F1_VS_F2.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.F2_VS_F1)
>>> g.generate_mode == GenerateMode.F2_VS_F1.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.F1_VS_X1)
>>> g.generate_mode == GenerateMode.F1_VS_X1.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.F2_VS_X1)
>>> g.generate_mode == GenerateMode.F2_VS_X1.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.F1_VS_X2)
>>> g.generate_mode == GenerateMode.F1_VS_X2.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.F2_VS_X2)
>>> g.generate_mode == GenerateMode.F2_VS_X2.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.X1_VS_F1)
>>> g.generate_mode == GenerateMode.X1_VS_F1.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.X1_VS_F2)
>>> g.generate_mode == GenerateMode.X1_VS_F2.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.X2_VS_F1)
>>> g.generate_mode == GenerateMode.X2_VS_F1.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.X2_VS_F2)
>>> g.generate_mode == GenerateMode.X2_VS_F2.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.F1F2_VS_F1)
>>> g.generate_mode == GenerateMode.F1F2_VS_F1.value
True
>>> g.generate(start=-2*math.pi, step=0.1, stop=math.pi/2, mode=GenerateMode.F1F2_VS_F2)
>>> g.generate_mode == GenerateMode.F1F2_VS_F2.value
True
>>> os.remove("test.png")
>>> os.remove("test2.png")
>>> os.remove("data.json")
>>> os.remove("config.json")
"""
