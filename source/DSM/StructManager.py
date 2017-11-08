#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Struct Manager
"""

import re
from Struct import *

class StructManager(object):
    """
    结构体的管理类，用于从字符串中解析结构体，判断结构体合法性，
    存储原始字符串用于优化顺序后写回操作
    """

    PATTERN_STRUCT_HEADER = re.compile(r'([\w ]*?struct.*?)\{')
    PATTERN_STRUCT_BODY = re.compile(r'\{(.+)\}')
    PATTERN_STRUCT_TAIL = re.compile(r'.*\}(.*);')

    def parse_from_string(self, struct_str):
        """
        Parse struct from string.
        """

        struct_str = re.sub('[\r\n\t]', '', struct_str.strip())
        if not StructManager.valid(struct_str) or not self._is_struct(struct_str):
            return None
        struct_instance = Struct(self._STRUCT_HEADER, self._STRUCT_BODY, self._STRUCT_TAIL)
        return struct_instance

    def _is_struct(self, struct_str):
        headers = self.PATTERN_STRUCT_HEADER.findall(struct_str)
        body = self.PATTERN_STRUCT_BODY.findall(struct_str)
        tail = self.PATTERN_STRUCT_TAIL.findall(struct_str)

        if not headers or not body:
            return False
        self._STRUCT_HEADER = headers[0].strip()
        if struct_str.find(self._STRUCT_HEADER) != 0 or struct_str[-1] != ';':
            return False
        self._STRUCT_BODY = body[0].strip()
        self._STRUCT_TAIL = ""
        if tail:
            self._STRUCT_TAIL = tail[0].strip()
        return True

    def valid(struct_str):
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

SM = StructManager
