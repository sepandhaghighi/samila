# -*- coding: utf-8 -*-
"""Samila main."""

from art import tprint
from .params import SAMILA_VERSION
from .functions import samila_help

if __name__ == "__main__":
    tprint("samila")
    tprint("V:" + SAMILA_VERSION)
    samila_help()
