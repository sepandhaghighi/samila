<div align="center">
	<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/logo.png" width=400 height=400>
	<br/>
	<h1>Samila</h1>
	<br/>
	<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
	<a href="https://codecov.io/gh/sepandhaghighi/samila"><img src="https://codecov.io/gh/sepandhaghighi/samila/branch/master/graph/badge.svg"></a>
	<a href="https://badge.fury.io/py/samila"><img src="https://badge.fury.io/py/samila.svg" alt="PyPI version" height="18"></a>
	<a href="https://anaconda.org/sepandhaghighi/samila"><img src="https://anaconda.org/sepandhaghighi/samila/badges/version.svg"></a>
	<a href="https://colab.research.google.com/github/sepandhaghighi/samila/blob/master"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Samila-Colab"></a>
	<a href="https://discord.com/invite/94bz5QGZWb"><img src="https://img.shields.io/discord/900055829225562162.svg" alt="Discord Channel"></a>
</div>


## Overview

<p align="justify">	
Samila is a generative art generator written in Python, Samila lets you create images based on many thousand points. The position of every single point is calculated by a formula, which has random parameters. Because of the random numbers, every image looks different.
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
		<td align="center"><img src="https://github.com/sepandhaghighi/samila/actions/workflows/test.yml/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/samila/actions/workflows/test.yml/badge.svg?branch=dev"></td>
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

### PyPI
- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install samila==1.4`

### Source code
- Download [Version 1.4](https://github.com/sepandhaghighi/samila/archive/v1.4.zip) or [Latest Source](https://github.com/sepandhaghighi/samila/archive/dev.zip)
- Run `pip install .`

### Conda
- Check [Conda Managing Package](https://conda.io)
- `conda install -c sepandhaghighi samila`


## Usage

### Magic
```pycon
>>> import matplotlib.pyplot as plt
>>> from samila import GenerativeImage
>>> g = GenerativeImage()
>>> g.generate()
>>> g.plot()
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/7.png">	

ℹ️ You can change function generation seed by `func_seed` parameter in `GenerativeImage`

### Basic
```pycon
>>> import random
>>> import math
>>> def f1(x, y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
>>> def f2(x, y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result
>>> g = GenerativeImage(f1, f2)
>>> g.generate()
>>> g.plot()
>>> g.seed
188781
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/1.png">	

### Generation mode
```pycon
>>> from samila import GenerateMode
>>> g = GenerativeImage(f1, f2)
>>> g.generate(mode=GenerateMode.F1_VS_INDEX)
>>> g.plot()
>>> g.seed
883114
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/10.png">	

ℹ️ Supported modes : `F1_VS_F2`, `F2_VS_F1`, `F1_VS_INDEX`, `F2_VS_INDEX`, `INDEX_VS_F1`, `INDEX_VS_F2`, `F1_VS_X1`, `F1_VS_X2`, `F2_VS_X1`, `F2_VS_X2`, `X1_VS_F1`, `X1_VS_F2`, `X2_VS_F1` and `X2_VS_F2`

ℹ️ Default mode is `F1_VS_F2`

### Projection
```pycon
>>> from samila import Projection
>>> g = GenerativeImage(f1, f2)
>>> g.generate()
>>> g.plot(projection=Projection.POLAR)
>>> g.seed
829730
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/2.png">	

ℹ️ Supported projections : `RECTILINEAR`, `POLAR`, `AITOFF`, `HAMMER`, `LAMBERT`, `MOLLWEIDE` and `RANDOM`

ℹ️ Default projection is `RECTILINEAR`

### Marker
```pycon
>>> from samila import Marker
>>> g = GenerativeImage(f1, f2)
>>> g.generate()
>>> g.plot(marker=Marker.CIRCLE, spot_size=10)
>>> g.seed
448742
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/9.png">	

ℹ️ Supported markers : `POINT`, `PIXEL`, `CIRCLE`, `TRIANGLE_DOWN`, `TRIANGLE_UP`, `TRIANGLE_LEFT`, `TRIANGLE_RIGHT`, `TRI_DOWN`, `TRI_UP`, `TRI_LEFT`, `TRI_RIGHT`, `OCTAGON`, `SQUARE`, `PENTAGON`, `PLUS`, `PLUS_FILLED`, `STAR`, `HEXAGON_VERTICAL`, `HEXAGON_HORIZONTAL`, `X`, `X_FILLED`, `DIAMOND`, `DIAMON_THIN`, `VLINE`, `HLINE` and `RANDOM`

ℹ️ Default marker is `POINT`

### Rotation
You can even rotate your art by using `rotation` parameter. Enter your desired rotation for the image in degrees and you will have it.

```pycon
>>> g = GenerativeImage(f1, f2)
>>> g.generate()
>>> g.plot(rotation=45)
```

ℹ️ Default rotation is `0`

### Range
```pycon
>>> g = GenerativeImage(f1, f2)
>>> g.generate(start=-2*math.pi, step=0.01, stop=0)
>>> g.plot()
>>> g.seed
234752
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/3.png">	

ℹ️ Default range is $(-\pi, \pi)$

### Color
```pycon
>>> g = GenerativeImage(f1, f2)
>>> g.generate()
>>> g.plot(color="yellow", bgcolor="black", projection=Projection.POLAR)
>>> g.seed
1018273
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/4.png">	

ℹ️ Default color is `black`

ℹ️ Default background-color is `white`

ℹ️ Supported colors are available in `VALID_COLORS` list

ℹ️ `color` and `bgcolor` parameters supported formats:

1. Color name (example: `color="yellow"`)
2. RGB/RGBA (example: `color=(0.1,0.1,0.1)`, `color=(0.1,0.1,0.1,0.1)`)
3. Hex (example: `color="#eeefff"`)
4. Random (example: `color="random"`)
5. Complement (example: `color="complement", bgcolor="blue"`)
6. Transparent (example: `bgcolor="transparent"`)
7. List (example: `color=["black", "#fffeef",...]`)

⚠️ **Transparent** mode is only available for background

⚠️ **List** mode is only available for color

⚠️ In **List** mode, the length of this list must be equal to the lengths of data1 and data2

#### Point color
You can make your custom color map and use it in Samila.

```pycon
>>> colorarray = [
...  [0.7, 0.2, 0.2, 1],
...  [0.6, 0.3, 0.2, 1],
...  "black",
...  [0.4, 0.4, 0.3, 1],
...  [0.3, 0.4, 0.4, 1],
...  "#ff2561"]
>>> g.generate()
>>> g.seed
454893
>>> g.plot(cmap=colorarray, color=g.data2, projection=Projection.POLAR)
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/8.png">	


### Regeneration
```pycon
>>> g = GenerativeImage(f1, f2)
>>> g.generate(seed=1018273)
>>> g.plot(projection=Projection.POLAR)
>>> plt.show()
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/5.png">	

### NFT.storage
Upload generated image directly to [NFT.storage](https://NFT.storage)

```pycon
>>> g.nft_storage(api_key="YOUR_API_KEY", timeout=5000)
{'status': True, 'message': 'FILE_LINK'}
```

You can also upload your config/data to nft storage as follows:
```pycon
>>> g.nft_storage(api_key="API_KEY", upload_config=True)
{'status': {'image': True, 'config':True}, 'message': {'image':'IMAGE_FILE_LINK', 'config':'CONFIG_FILE_LINK'}
```
or
```pycon
>>> g.nft_storage(api_key="API_KEY", upload_data=True)
{'status': {'image': True, 'data':True}, 'message': {'image':'IMAGE_FILE_LINK', 'data':'DATA_FILE_LINK'}
```

You have the option to choose a specific IPFS gateway:
```pycon
>>> from samila import Gateway
>>> g.nft_storage(api_key="API_KEY", upload_data=True, gateway=Gateway.DWEB)
{'status': {'image': True, 'data':True}, 'message': {'image':'IMAGE_FILE_LINK', 'data':'DATA_FILE_LINK'}
```


⚠️ This method is deprecated and may be removed in future releases

ℹ️ Default timeout is `3000` seconds

ℹ️ Default gateway is `IPFS_IO`

### Save image
Save generated image.

```pycon
>>> g.save_image(file_adr="test.png")
{'status': True, 'message': 'FILE_PATH'}
```
Save generated image in higher resolutions.

```pycon
>>> g.save_image(file_adr="test.png", depth=5)
{'status': True, 'message': 'FILE_PATH'}
```

### Save data
Save generated image data.

```pycon
>>> g.save_data(file_adr="data.json")
{'status': True, 'message': 'FILE_PATH'}
```
So you can load it into a `GenerativeImage` instance later by

```pycon
>>> g = GenerativeImage(data=open('data.json', 'r'))
```

Data structure:
```JSON
{
  "plot": {
    "projection": "polar",
    "bgcolor": "black",
    "color": "snow",
    "spot_size": 0.01
  },
  "matplotlib_version": "3.0.3",
  "data1": [
    0.3886741692042526,
    22.57390286376703,
    -0.1646310981668766,
    66.23632344600155
  ],
  "data2": [
    -0.14588750183600108,
    20.197945942677833,
    0.5485453260942901,
    -589.3284610518896
  ]
}
```

### Save config
Save generated image config. It contains string formats of functions which is also human readable.

```pycon
>>> g.save_config(file_adr="config.json")
{'status': True, 'message': 'FILE_PATH'}
```
So you can load it into a `GenerativeImage` instance later by

```pycon
>>> g = GenerativeImage(config=open('config.json', 'r'))
```

Config structure:

```JSON
{
    "matplotlib_version": "3.0.3",
    "generate": {
        "seed": 379184,
        "stop": 3.141592653589793,
        "step": 0.01,
        "start": -3.141592653589793
    },
    "f2": "random.uniform(-1,1)*math.cos(x*(y**3))+random.uniform(-1,1)*math.ceil(y-x)",
    "f1": "random.uniform(-1,1)*math.ceil(y)-random.uniform(-1,1)*y**2+random.uniform(-1,1)*abs(y-x)",
    "plot": {
        "color": "snow",
        "bgcolor": "black",
        "projection": "polar",
        "spot_size": 0.01
    }
}
```

### Command Line Interface (CLI)
You can easily create art directly from the command line with Samila CLI. Here's an example command to get started:
```bash
samila --color=red --bgcolor=black --rotation=30 --projection=polar --mode f2_vs_f1 --save-image test.png
```

In this example:
- `--color=red`: Sets the primary color of the art.
- `--bgcolor=black`: Sets the background color.
- `--rotation=30`: Rotates the artwork by 30 degrees.
- `--projection=polar`: Use polar projection for plotting.
- `--mode=f2_vs_f1`: Sets the generation mode
- `--save-image=test.png`: Saves the generated image as test.png.

For more options and detailed usage, run the following command to access help:
```bash
samila --help
```
This will provide additional information on all available parameters and how to customize your artwork further.

## Mathematical details
Samila is simply a transformation between a square-shaped space from the Cartesian coordinate system to any arbitrary coordination like [Polar coordinate system](https://en.wikipedia.org/wiki/Polar_coordinate_system).

### Example
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/mathematical_details/transformation.png">

We have set of points in the first space (left square) which can be defined as follow:

<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/mathematical_details/S1.jpg">

And below functions are used for transformation:

```pycon
>>> def f1(x, y):
    result = random.uniform(-1,1) * x**2 - math.sin(y**2) + abs(y-x)
    return result
>>> def f2(x, y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result
```

<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/mathematical_details/S2.jpg">

here we use `Projection.POLAR` so later space will be the polar space and we have:

```pycon
>>> g = GenerativeImage(f1, f2)
>>> g.generate(seed=10)
>>> g.plot(projection=Projection.POLAR)
```
<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/mathematical_details/S2_.jpg">

<img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/images/6.png">

## Try Samila in your browser!
Samila can be used online in interactive Jupyter Notebooks via the Binder or Colab services!

Try it out now!

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sepandhaghighi/samila/master)

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sepandhaghighi/samila/blob/master)

ℹ️ Check `examples` folder 

## Issues & bug reports			

Just fill an issue and describe it. We'll check it ASAP! or send an email to [info@samila.site](mailto:info@samila.site "info@samila.site"). 

- Please complete the issue template
 
You can also join our discord server

<a href="https://discord.com/invite/94bz5QGZWb">
  <img src="https://img.shields.io/discord/900055829225562162.svg?style=for-the-badge" alt="Discord Channel">
</a>


## Social media

1. [Instagram](https://www.instagram.com/samila_arts)
2. [Telegram](https://t.me/samila_arts)
3. [Twitter](https://twitter.com/samila_arts)
4. [Discord](https://discord.com/invite/94bz5QGZWb)


## References			

<blockquote>1- Schönlieb, Carola-Bibiane, and Franz Schubert. "Random simulations for generative art construction–some examples." Journal of Mathematics and the Arts 7.1 (2013): 29-39.</blockquote>

<blockquote>2- <a href="https://github.com/cutterkom/generativeart">Create Generative Art with R</a></blockquote>

<blockquote>3- <a href="https://nft.storage/">NFT.storage : Free decentralized storage and bandwidth for NFTs</a></blockquote>

## Acknowledgments

This project was funded through the **Next Step Microgrant**, a program established by [Protocol Labs](https://protocol.ai/).

## Show your support
								
<h3>Star this repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to our project</h3>	

If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .			

<a href="http://www.samila.site/donate.html" target="_blank"><img src="https://github.com/sepandhaghighi/samila/raw/master/otherfiles/donate-button.png" height="90px" width="270px" alt="Samila Donation"></a>



