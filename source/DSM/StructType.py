#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Struct Type

valid or not / typedef or not / struct names

e.g.
typedef struct A
{
    int a;
    double b;
} T_TEST, *P_T_TEST;

Then StructType.valid = True, StructType.typedef = True, StructType.type = TYPEDEF_STRUCT_A_XXX_T
And StructType.names = ['struct A', 'T_TEST', '*P_T_TEST']  StructType.objs = []
That means these name are related to the struct.

e.g.
struct A
{
    int a;
    double b;
} OBJ;

Then StructType.valid = True, StructType.typedef = False, StructType.type = STRUCT_A_XXX_V_T
And StructType.names = ['struct A']  StructType.objs = ['OBJ']
"""

import re
from enum import Enum

class StructTypeEnum(Enum):
    '''
    结构体类型枚举
    '''
                                           # | has_typedef | has_struct_name | has_tail |
    TYPEDEF_STRUCT_A_XXX_T = 7             #       1               1              1
    TYPEDEF_STRUCT_A_XXX_INVALID = 6       #       1               1              0
    TYPEDEF_STRUCT_XXX_T = 5               #       1               0              1
    TYPEDEF_STRUCT_XXX_INVALID = 4         #       1               0              0
    STRUCT_A_XXX_V_T = 3                   #       0               1              1
    STRUCT_A_XXX = 2                       #       0               1              0
    STRUCT_XXX_V_T = 1                     #       0               0              1
    STRUCT_XXX_INVALID = 0                 #       0               0              0

class StructType(object):
    """
    对应结构体的类型
    """

    TYPEDEF_STRUCT_A_XXX_T = "typedef struct A {xxx} T;"
    TYPEDEF_STRUCT_XXX_T = "typedef struct {xxx} T;"

    TYPEDEF_STRUCT_A_XXX_INVALID = "typedef struct A {xxx}"
    TYPEDEF_STRUCT_XXX_INVALID = "typedef struct {xxx}"

    STRUCT_A_XXX = "struct A {xxx};"
    STRUCT_A_XXX_V_T = "struct A {xxx} V_T;"
    STRUCT_XXX_V_T = "struct {xxx} V_T;"

    STRUCT_XXX_INVALID = "struct {xxx};"

    def __init__(self, header, tail):
        self.type = ""
        self.valid = False
        self.typedef = False
        self.names = []
        self.objs = []
        self._header = header
        self._tail = tail
        self.__parse__()

    def __parse__(self):
        self.__parse_type__()
        self.__parse_names__()
        self.__parse_objs__()

    def __parse_type__(self):
        header_pattern = re.compile(r".*(struct.*?\w+)")
        self._struct_names = header_pattern.findall(self._header)

        self._has_typedef = 0x04 if "typedef" in self._header else 0x00
        self._has_struct_name = 0x02 if self._struct_names else 0x00
        self._has_tail = 0x01 if self._tail != "" else 0x00

        type_index = self._has_typedef | self._has_struct_name | self._has_tail
        type_str = str(StructTypeEnum(type_index)).split('.')[1]

        self.valid = False if 'invalid' in type_str.lower() else True
        self.typedef = False if 'typedef' not in type_str.lower() else True
        self.type = self.__getattribute__(type_str)

    def __parse_names__(self):
        if not self.valid:
            return
        for struct_name in self._struct_names:
            if struct_name.strip() != "":
                self.names.append(struct_name.strip())
        if self.typedef:
            self.names.extend(self.__parse_tail__())

    def __parse_objs__(self):
        if not self.valid:
            return
        if not self.typedef:
            self.objs.extend(self.__parse_tail__())

    def __parse_tail__(self):
        tail_list = []
        for typedef_struct_name in self._tail.split(","):
                if typedef_struct_name.strip() != "":
                    tail_list.append(typedef_struct_name.strip())
        return tail_list

ST = StructType