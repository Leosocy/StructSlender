"""struct
"""

import sys, os

class StructManager(object):
    """
    结构体的管理类，用于从字符串中解析结构体，判断结构体合法性，
    存储原始字符串用于优化顺序后写会操作
    """

    def parseFromString(struct_str, encoding='utf-8'):
        structInstance = Struct()
        return structInstance


class Struct(object):
    """
    A class that corresponds to the properties of a structure.
    """

    def __init__(self):
        self._m_orig_struct_str = ""
        self._m_has_typedef = False
        self._m_struct_name = []
        self._m_variables = []

    def __str__(self):
        return "StructName <%s>, Variables <%s>" % ({name for name in self._m_struct_name}, {var for var in self._m_variables})
