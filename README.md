<div align="center">
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/logo.png" width=400 height=400>
<br/>
<h1>Samila</h1>
<br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://codecov.io/gh/sepandhaghighi/samila">
  <img src="https://codecov.io/gh/sepandhaghighi/samila/branch/master/graph/badge.svg" />
</a>
<a href="https://badge.fury.io/py/samila"><img src="https://badge.fury.io/py/samila.svg" alt="PyPI version" height="18"></a>
</div>

----------
## Table of contents					
   * [Overview](https://github.com/sepandhaghighi/samila#overview)
   * [Installation](https://github.com/sepandhaghighi/samila#installation)
   * [Usage](https://github.com/sepandhaghighi/samila#usage)
   * [Mathematical Details](https://github.com/sepandhaghighi/samila#mathematical-details)
   * [Issues & Bug Reports](https://github.com/sepandhaghighi/samila#issues--bug-reports)
   * [Dependencies](https://github.com/sepandhaghighi/samila#dependencies)
   * [Contribution](https://github.com/sepandhaghighi/samila/blob/master/.github/CONTRIBUTING.md)
   * [References](https://github.com/sepandhaghighi/samila#references)
   * [Authors](https://github.com/sepandhaghighi/samila/blob/master/AUTHORS.md)
   * [License](https://github.com/sepandhaghighi/samila/blob/master/LICENSE)
   * [Show Your Support](https://github.com/sepandhaghighi/samila#show-your-support)
   * [Changelog](https://github.com/sepandhaghighi/samila/blob/master/CHANGELOG.md)
   * [Code of Conduct](https://github.com/sepandhaghighi/samila/blob/master/.github/CODE_OF_CONDUCT.md)

## Overview

<p align="justify">	
Samila is a generative art generator written in Python, Samila let's you create arts based on many thousand points. The position of every single point is calculated by a formula, which has random parameters. Because of the random numbers, every image looks different.
</p>


<table>
	<tr> 
		<td align="center">Open Hub</td>
		<td align="center"><a href="https://www.openhub.net/p/samila"><img src="https://www.openhub.net/p/samila/widgets/project_thin_badge.gif"></a></td>	
	</tr>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/project/samila"><img src="http://pepy.tech/badge/samila"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/samila"><img src="https://img.shields.io/github/stars/sepandhaghighi/samila.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
    <tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/samila/workflows/CI/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/samila/workflows/CI/badge.svg?branch=dev"></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td><a href="https://www.codacy.com/gh/sepandhaghighi/samila/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/samila&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/14df8ed5f8434aaea85889555b0182a9"/></a></td>
		<td><a href="https://codebeat.co/projects/github-com-sepandhaghighi-samila-dev"><img alt="codebeat badge" src="https://codebeat.co/badges/01e6aa48-4cc2-4d9c-8288-c9fb490ad371" /></a></td>
		<td><a href="https://www.codefactor.io/repository/github/sepandhaghighi/samila"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/samila/badge" alt="CodeFactor" /></a></td>
	</tr>
</table>



## Installation		


### Source code
- Download [Version 0.2](https://github.com/sepandhaghighi/samila/archive/v0.2.zip) or [Latest Source ](https://github.com/sepandhaghighi/samila/archive/dev.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install samila==0.2` or `pip3 install samila==0.2` (Need root access)

### Easy install

- Run `easy_install --upgrade samila` (Need root access)


## Usage

### Basic
```pycon
>>> import random
>>> import math
>>> import matplotlib.pyplot as plt
>>> from samila import GenerativeImage
>>> def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
>>> def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result
>>> g = GenerativeImage(f1,f2)
>>> g.generate()
>>> g.plot()
>>> g.seed
188781
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/1.png">	

### Projection
```pycon
>>> from samila import Projection
>>> g = GenerativeImage(f1,f2)
>>> g.generate()
>>> g.plot(projection=Projection.POLAR)
>>> g.seed
829730
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/2.png">	

* Supported projections : `RECTILINEAR`, `POLAR`, `AITOFF`, `HAMMER`, `LAMBERT` and `MOLLWEIDE`
* Default projection is `RECTILINEAR`

### Range
```pycon
>>> g = GenerativeImage(f1,f2)
>>> g.generate(start = -2*math.pi,step=0.1,stop=0)
>>> g.plot()
>>> g.seed
234752
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/3.png">	

### Color
```pycon
>>> g = GenerativeImage(f1,f2)
>>> g.generate()
>>> g.plot(color="yellow",bgcolor="black",projection=Projection.POLAR)
>>> g.seed
1018273
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/4.png">	

* Supported colors are available in `VALID_COLORS` list
* `color` and `bgcolor` parameters support color name and RGB/RGBA formats

### Regeneration
```pycon
>>> g = GenerativeImage(f1,f2)
>>> g.generate(seed=1018273)
>>> g.plot(projection=Projection.POLAR)
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/5.png">	

### NFT.storage
Upload generated image directly to [NFT.storage](https://NFT.storage)

```pycon
>>> g.nft_storage(api_key = YOUR_API_KEY)
{'status': True, 'message': 'Everything seems good'}
```

### Save
Save generated image

```pycon
>>> g.save_image(file_adr="test.png")
{'status': True, 'message': 'Everything seems good'}
```

## Mathematical details
Samila is simply a transformation between a square-shaped space from the Cartesian coordinate system to any arbitrary coordination like [Polar coordinate system](https://en.wikipedia.org/wiki/Polar_coordinate_system).

### Example
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/mathematical_details/transformation.png">

We have set of points in the first space (left square) which can be define as follow:

<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/mathematical_details/S1.jpg">

And bellow functions are used for transformation:

```pycon
>>> def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
>>> def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result
```

<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/mathematical_details/S2.jpg">

here we uses `Projection.POLAR` so later space will be the polar space and we have:

```pycon
>>> g = GenerativeImage(f1,f2)
>>> g.generate(seed=10)
>>> g.plot(projection=Projection.POLAR)
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/mathematical_details/S2_.jpg">

<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/6.png">

## Issues & bug reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [info@4r7.ir](mailto:info@4r7.ir "info@4r7.ir"). 

* Please complete the issue template


## Dependencies

<table>
	<tr> 
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center"><a href="https://requires.io/github/sepandhaghighi/samila/requirements/?branch=master"><img src="https://requires.io/github/sepandhaghighi/samila/requirements.svg?branch=master" alt="Requirements Status" /></a></td>
		<td align="center"><a href="https://requires.io/github/sepandhaghighi/samila/requirements/?branch=dev"><img src="https://requires.io/github/sepandhaghighi/samila/requirements.svg?branch=dev" alt="Requirements Status" /></a></td>
	</tr>
</table>


## References			

<blockquote>1- Schönlieb, Carola-Bibiane, and Franz Schubert. "Random simulations for generative art construction–some examples." Journal of Mathematics and the Arts 7.1 (2013): 29-39.</blockquote>

<blockquote>2- <a href="https://github.com/cutterkom/generativeart">Create Generative Art with R</a></blockquote>

<blockquote>3- <a href="https://nft.storage/">NFT.storage : Free decentralized storage and bandwidth for NFTs</a></blockquote>
	

## Show your support
								
<h3>Star this repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to our project</h3>	

If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .			

<h4>Bitcoin</h4>
1KtNLEEeUbTEK9PdN6Ya3ZAKXaqoKUuxCy
<h4>Ethereum</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Litecoin</h4>
Ldnz5gMcEeV8BAdsyf8FstWDC6uyYR6pgZ
<h4>Doge</h4>
DDUnKpFQbBqLpFVZ9DfuVysBdr249HxVDh
<h4>Tron</h4>
TCZxzPZLcJHr2qR3uPUB1tXB6L3FDSSAx7
<h4>Ripple</h4>
rN7ZuRG7HDGHR5nof8nu5LrsbmSB61V1qq
<h4>Binance Coin</h4>
bnb1zglwcf0ac3d0s2f6ck5kgwvcru4tlctt4p5qef
<h4>Tether</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Dash</h4>
Xd3Yn2qZJ7VE8nbKw2fS98aLxR5M6WUU3s
<h4>Stellar</h4>
GALPOLPISRHIYHLQER2TLJRGUSZH52RYDK6C3HIU4PSMNAV65Q36EGNL
<h4>Zilliqa</h4>
zil1knmz8zj88cf0exr2ry7nav9elehxfcgqu3c5e5
<h4>Coffeete</h4>
<a href="http://www.coffeete.ir/opensource">
<img src="http://www.coffeete.ir/images/buttons/lemonchiffon.png" style="width:260px;" />
</a>


