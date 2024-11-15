# -*- coding: utf-8 -*-
"""
>>> from samila.cli import *
>>> main(sys_args=["--version"])
1.3
>>> main(sys_args=["--info"])
                        _  _
 ___   __ _  _ __ ___  (_)| |  __ _
/ __| / _` || '_ ` _ \ | || | / _` |
\__ \| (_| || | | | | || || || (_| |
|___/ \__,_||_| |_| |_||_||_| \__,_|
<BLANKLINE>
<BLANKLINE>
__     __    _     _____
\ \   / / _ / |   |___ /
 \ \ / / (_)| |     |_ \
  \ V /   _ | | _  ___) |
   \_/   (_)|_|(_)|____/
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Samila is a generative art generator written in Python, Samila let's you
create arts based on many thousand points. The position of every single
point is calculated by a formula, which has random parameters.
Because of the random numbers, every image looks different.

Website : https://www.samila.site
Repo : https://github.com/sepandhaghighi/samila
>>> main(sys_args=["--no-display"])
>>> main(sys_args=["--no-display", "--save-image", "test.png", "--save-config", "config.json", "--save-data", "data.json"])
>>> main(sys_args=["--no-display", "--save-image", "test.png", "--save-config", "config.json", "--save-data", "data.json", "--verbose"])
[LOG] GenerativeImage object created.
******************************
[LOG] GenerativeImage generated.
******************************
[LOG] GenerativeImage plotted.
******************************
[LOG] Image saved. File address: C:\Users\Sepkjaer\AppData\Local\Programs\Python\Python38-32\test.png
******************************
[LOG] Data saved. File address: C:\Users\Sepkjaer\AppData\Local\Programs\Python\Python38-32\data.json
******************************
[LOG] Config saved. File address: C:\Users\Sepkjaer\AppData\Local\Programs\Python\Python38-32\config.json
******************************

"""
