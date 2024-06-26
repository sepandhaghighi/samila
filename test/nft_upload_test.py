# -*- coding: utf-8 -*-
"""
>>> import os
>>> import time
>>> from samila import GenerativeImage, Projection, Gateway
>>> from samila.params import VALID_COLORS
>>> g = GenerativeImage()
>>> g.generate()
>>> g.plot()
>>> NFT_STORAGE_API_KEY = os.environ["NFT_STORAGE_API_KEY"]
>>> g.generate()
>>> g.plot(projection=Projection.RANDOM, color="random", bgcolor="random")
>>> counter = 0
>>> try_limit = 10
>>> status = False
>>> while(status == False and counter<try_limit):
...     result = g.nft_storage(api_key=NFT_STORAGE_API_KEY, depth=3)
...     counter = counter + 1
...     status = result["status"]
...     time.sleep(10)
>>> status
True
>>> status = False
>>> counter = 0
>>> while(status == False and counter<try_limit):
...     result = g.nft_storage(api_key=NFT_STORAGE_API_KEY, upload_config=True)
...     counter = counter + 1
...     status = all(result["status"].values())
...     time.sleep(10)
>>> result['status']["image"]
True
>>> result['status']["config"]
True
>>> status = False
>>> counter = 0
>>> while(status == False and counter<try_limit):
...     result = g.nft_storage(api_key=NFT_STORAGE_API_KEY, upload_data=True)
...     counter = counter + 1
...     status = all(result["status"].values())
...     time.sleep(10)
>>> result['status']["image"]
True
>>> result['status']["data"]
True
>>> status = False
>>> counter = 0
>>> while(status == False and counter<try_limit):
...     result = g.nft_storage(api_key=NFT_STORAGE_API_KEY, upload_data=True, upload_config=True, gateway=Gateway.CID)
...     counter = counter + 1
...     status = all(result["status"].values())
...     time.sleep(10)
>>> result['status']["image"]
True
>>> result['status']["data"]
True
>>> result['status']["config"]
True
"""
