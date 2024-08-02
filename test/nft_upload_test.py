# -*- coding: utf-8 -*-
"""
>>> import os
>>> from pytest import warns
>>> from samila import GenerativeImage, Projection, Gateway
>>> g = GenerativeImage()
>>> g.generate()
>>> g.plot()
>>> NFT_STORAGE_API_KEY = os.environ["NFT_STORAGE_API_KEY"]
>>> g.generate()
>>> g.plot(projection=Projection.RANDOM, color="random", bgcolor="random")
>>> with warns(DeprecationWarning, match='`nft_storage` is deprecated and may be removed in future releases.'):
...     result = g.nft_storage(api_key=NFT_STORAGE_API_KEY, depth=3)
>>> result["status"]
False
>>> with warns(DeprecationWarning, match='`nft_storage` is deprecated and may be removed in future releases.'):
...     result = g.nft_storage(api_key=NFT_STORAGE_API_KEY, upload_config=True)
>>> result['status']["image"]
False
>>> result['status']["config"]
False
>>>  with warns(DeprecationWarning, match='`nft_storage` is deprecated and may be removed in future releases.'):
...      result = g.nft_storage(api_key=NFT_STORAGE_API_KEY, upload_data=True)
>>> result['status']["image"]
False
>>> result['status']["data"]
False
>>>  with warns(DeprecationWarning, match='`nft_storage` is deprecated and may be removed in future releases.'):
...      result = g.nft_storage(api_key=NFT_STORAGE_API_KEY, upload_data=True, upload_config=True, gateway=Gateway.CID)
>>> result['status']["image"]
False
>>> result['status']["data"]
False
>>> result['status']["config"]
False
"""
