#!/bin/sh
python -m autopep8 samila --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --verbose --ignore=E721
python -m autopep8 setup.py --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --verbose
