# -*- coding: utf-8 -*-
"""
>>> import random
>>> from samila.functions import *
>>> is_valid_color("blue")
True
>>> is_valid_color((0,0,0))
True
>>> is_valid_color((0.1,0.1,0,1))
True
>>> is_valid_color([1,1,1,1])
True
>>> is_valid_color("#FFFAAF")
True
>>> color_complement("#FFFFFF")
'#000000'
>>> color_complement("#FFAFBF")
'#005040'
>>> color_complement("#000000")
'#ffffff'
>>> select_color("blue")
'blue'
>>> select_color("#FFFFFA")
'#fffffa'
>>> select_color((0.1,0.1,0.1))
(0.1, 0.1, 0.1)
>>> select_color(None)
>>> select_color("complement")
'COMPLEMENT'
>>> select_color("transparent")
'TRANSPARENT'
>>> s = list(float_range(1,1.5,0.1))
>>> s
[1.0, 1.1, 1.2000000000000002, 1.3000000000000003, 1.4000000000000004]
>>> is_same_data(s,[1,1.1,1.2,1.3,1.4])
True
>>> is_same_data([1,1.1,1.2,1.3,1.4],[1,1.11,1.3,1.4,1.5])
False
>>> is_same_data(s,[1,1.1,1.2,1.3,1.4,1.5,1.6])
False
>>> is_same_data(s,[])
False
>>> filter_color("yellow", "blue")
('yellow', 'blue')
>>> filter_color((0.2,0.3,0.4), (0.2,0.3,0.4,1))
((0.2, 0.3, 0.4), (0.2, 0.3, 0.4, 1))
>>> filter_color("#FFFFFF", "#ffffe1")
('#ffffff', '#ffffe1')
>>> random.seed(2)
>>> color1, bgcolor1 = filter_color("random", "random")
>>> random.seed(3)
>>> color2, bgcolor2 = filter_color("RANDOM", "RANDOM")
>>> color1 == color2
False
>>> random.seed(2)
>>> color1 = random_hex_color_gen()
>>> random.seed(3)
>>> color2 = random_hex_color_gen()
>>> color1 == color2
False
>>> len(color1)
7
>>> len(color2)
7
>>> filter_size(2)
>>> filter_size((2, 'test'))
>>> filter_size((2, 3.5))
(2, 3.5)
>>> filter_projection(2)
>>> filter_projection(Projection.POLAR)
'polar'
>>> random.seed(2)
>>> projection1 = filter_projection(Projection.RANDOM)
>>> random.seed(3)
>>> projection2 = filter_projection(Projection.RANDOM)
>>> projection1 == projection2
False
>>> distance_calc("test","test1")
1
>>> distance_calc("te1st","test")
1
>>> distance_calc("test12","test234")
3
>>> samila_help()
<BLANKLINE>
Samila is a generative art generator written in Python, Samila let's you
create arts based on many thousand points. The position of every single
point is calculated by a formula, which has random parameters.
Because of the random numbers, every image looks different.
<BLANKLINE>
Repo : https://github.com/sepandhaghighi/samila
"""
