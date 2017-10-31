"""
struct test
"""

import struct
import unittest

class TestStringMethods(unittest.TestCase):

    STRUCT_STR_VALID_WITH_TYPEDEF = \
"typdef struct \r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n};\r\n\
double *pdB;\r\n}\r\n\
T_TEST_STRUCT, *P_T_TEST_STRUCT;"

    STRUCT_STR_VALID_WITHOUT_TYPEDEF = \
"struct T_TEST_STRUCT\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n};\r\n\
double *pdB;\r\n};"

    STRUCT_STR_INVALID_WITH_TYPEDEF = \
"typdef struct \r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n\
double *pdB;\r\n}\r\n\
T_TEST_STRUCT, *P_T_TEST_STRUCT;"

    STRUCT_STR_INVALID_WITHOUT_TYPEDEF = \
"struct T_TEST_STRUCT\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n};\r\n\
double *pdB;"
 
    def setUp(self):
        self.sm_handler = struct.SM()
        pass
 
    def tearDown(self):
        # Do something to clear the test environment here.
        pass
 
    def test_struct_valid_with_typedef(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_VALID_WITH_TYPEDEF)
        self.assertIsNotNone(structInstance)
        self.assertTrue(structInstance.has_typedef)

    def test_struct_valid_without_typedef(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_VALID_WITHOUT_TYPEDEF)
        self.assertIsNotNone(structInstance)
        self.assertTrue(structInstance.has_typedef)

    def test_struct_invalid_with_typedef(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_INVALID_WITH_TYPEDEF)
        self.assertIsNone(structInstance)

    def test_struct_invalid_without_typedef(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_INVALID_WITHOUT_TYPEDEF)
        self.assertIsNone(structInstance)

 
if __name__ == '__main__':
    unittest.main()