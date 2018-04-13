# -*- coding: utf-8 -*-
# make print compatible with python 2.7
from __future__ import print_function

"""
Created on Mon Mar 12 21:11:54 2018
"""

import argparse
import fileinput
import re
import sys


def is_greater (var1, var2):
    return var1 > var2

def is_smaller (var1, var2):
    return var1 < var2

if __name__ == "__main__":
    print(is_greater(3,1))

