"""struct
"""

import sys
import re

class StructManager(object):
    """
    结构体的管理类，用于从字符串中解析结构体，判断结构体合法性，
    存储原始字符串用于优化顺序后写回操作
    """

    STRUCT_REGIX_1 = r'(.*struct?)(.*{?)(.*})(.*);'

    def parse_from_string(self, struct_str, encoding='utf-8'):
        if self._is_struct(struct_str):
            return None
        struct_instance = Struct()
        struct_instance._m_orig_struct_str = struct_str
        return struct_instance

    def _is_struct(self, struct_str):
        print(struct_str)
        searchObj = re.search(self.STRUCT_REGIX_1, str(struct_str), re.M|re.S)
        return False

    def _is_valid(self, struct_str):
        left_brackets = ['{', '[', '(']
        right_brackets = ['}', ']', ')']
        for char in struct_str:
            



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
        return "Orig <%s>, StructName <%s>, Variables <%s>" % (self._m_orig_struct_str, self._m_struct_name, self._m_variables)

if __name__ == '__main__':
    STRUCT_TEST_STRING = u"typdef struct \r\n{\r\nint a;\r\nstruct A {\r\nint b;\r\n};\r\ndouble *pdB;\r\n} T_TEST_STRUCT, *P_T_TEST_STRUCT;"
    SM = StructManager();
    struct = SM.parse_from_string(STRUCT_TEST_STRING)
    print(struct._m_has_typedef)
