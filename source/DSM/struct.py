"""
struct
"""

import sys
import re

class StructManager(object):
    """
    结构体的管理类，用于从字符串中解析结构体，判断结构体合法性，
    存储原始字符串用于优化顺序后写回操作
    """

    STRUCT_REGIX_HEADER = r'([\w ]*?struct.*?)\{'
    STRUCT_REGIX_BODY = r'\{(.+)\}'
    STRUCT_REGIX_TAIL = r'.*\}(.*);'

    def parse_from_string(self, struct_str):
        """
        Parse struct from string.
        """

        struct_str = re.sub('[\r\n\t]', '', struct_str.strip())
        if (not self._is_valid(struct_str)) or (not self._is_struct(struct_str)):
            return None
        struct_instance = Struct()
        return struct_instance

    def _is_struct(self, struct_str):
        print(struct_str)
        pattern = re.compile(self.STRUCT_REGIX_TAIL)
        searchObj = pattern.findall(struct_str)
        if not searchObj:
            return False
        print(searchObj)
        return True

    def _is_valid(self, struct_str):
        brackets_map = {'{':'}', '[':']', '(':')'}
        brackets_stack = []
        for char in struct_str:
            if char in brackets_map.keys():
                brackets_stack.append(char)
            elif char in brackets_map.values():
                if not brackets_stack or char != brackets_map[brackets_stack[-1]]:
                    return False
                else:
                    brackets_stack.pop()
        if brackets_stack:
            return False
        else:
            return True

class StructType(object):
    """
    对应结构体的类型
    """

    TYPEDEF_STRUCT_A_XXX_T = "typedef struct A {xxx} T;"
    TYPEDEF_STRUCT_XXX_T = "typedef struct {xxx} T;"

    STRUCT_A_XXX = "struct A {xxx};"
    STRUCT_A_XXX_V_T = "struct A {xxx} V_T;"
    STRUCT_XXX_V_T = "struct {xxx} V_T"

class Struct(object):
    """
    A class that corresponds to the properties of a structure.
    """


    def __init__(self):
        self.orig_struct_str = ""
        self.has_typedef = False
        self.struct_name = []
        self._variables = []

    def __str__(self):
        return "Orig <%s>, StructName <%s>, Variables <%s>" % (self.orig_struct_str, self.struct_name, self._variables)

SM = StructManager

if __name__ == '__main__':
    STRUCT_TEST_STRING = u"typdef struct \r\n{\r\nint a[2];\r\nstruct A {\r\nint b;\r\n};\r\ndouble *pdB;\r\n} T_TEST_STRUCT, *P_T_TEST_STRUCT;"
    SM = StructManager()
    struct = SM.parse_from_string(STRUCT_TEST_STRING)
    print(struct.has_typedef)
