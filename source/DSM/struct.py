#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
struct
"""

import sys
from StructType import *

class Struct(object):
    """
    A class that corresponds to the properties of a structure.
    """


    def __init__(self, header, body, tail):
        self.orig_struct_str = ""
        self.struct_type = StructType(header, tail)
        self._variables = []

    def __str__(self):
        return "Orig <%s>, StructName <%s>, Variables <%s>" % (self.orig_struct_str, self.struct_name, self._variables)

