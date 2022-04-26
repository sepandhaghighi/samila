# -*- coding: utf-8 -*-
"""
>>> import random
>>> from samila.functions import *
>>> s = list(float_range(1,1.5,0.1))
>>> s
[1.0, 1.1, 1.2000000000000002, 1.3000000000000003, 1.4000000000000004]
>>> is_same_data(s,[1,1.1,1.2,1.3,1.4])
True
>>> is_same_data([1,1.1,1.2,1.3,1.4],[1,1.11,1.3,1.4,1.5])
False
>>> filter_color("yellow")
'yellow'
>>> filter_color((0.2,0.3,0.4))
(0.2, 0.3, 0.4)
>>> filter_color("#FFFFFF")
"#FFFFFF"
>>> random.seed(2)
>>> color1 = filter_color("random")
>>> random.seed(3)
>>> color2 = filter_color("RANDOM")
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
>>> filter_color(2)
>>> filter_color(4)
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
