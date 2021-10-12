# -*- coding: utf-8 -*-
"""
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
>>> filter_color(2)
>>> filter_color(4)
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
