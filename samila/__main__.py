# -*- coding: utf-8 -*-
"""Samila main."""

import doctest
import sys
from art import tprint
from .params import *
from .functions import samila_help

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        if args[1].upper() == "TEST":
            error_flag = doctest.testfile(
                "test.py",
                optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
                | doctest.IGNORE_EXCEPTION_DETAIL,
                verbose=False)[0]
            sys.exit(error_flag)
        else:
            tprint("samila")
            tprint("V:" + SAMILA_VERSION)
            samila_help()
    else:
        tprint("samila")
        tprint("V:" + SAMILA_VERSION)
        samila_help()
