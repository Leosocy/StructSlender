"""
test struct valid
"""

import sys
sys.path.append('../../')
sys.path.append('../../source/DSM')
import StructManager as StructManager
import unittest

class TestStructValid(unittest.TestCase):

    STRUCT_STR_VALID_WITH_TYPEDEF = \
"typedef struct   A_Test\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n};\r\n\
double *pdB;\r\n}\r\n\
T_TEST_STRUCT, *P_T_TEST_STRUCT;"

    STRUCT_STR_VALID_WITHOUT_TYPEDEF = \
"struct ABC\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n};\r\n\
double *pdB;\r\n};"

    STRUCT_STR_INVALID_WITH_TYPEDEF = \
"typedef struct \r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n\
double *pdB;\r\n}\r\n\
T_TEST_STRUCT, *P_T_TEST_STRUCT;"

    STRUCT_STR_INVALID_WITHOUT_TYPEDEF = \
"struct T_TEST_STRUCT\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n};\r\n\
double *pdB;"

    STRUCT_STR_INVALID_WITHOUT_STRUCT = \
"ABC\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n};\r\n\
double *pdB;\r\n};"

    STRUCT_STR_INVALID_WITHOUT_SEMICOLON = \
"struct A\r\n\
{\r\n  int a[2];\r\n\
  struct A {\r\n    int b;\r\n   };\r\n\
double *pdB;\r\n  }  "

    def setUp(self):
        self.sm_handler = StructManager.SM()
        pass
 
    def tearDown(self):
        # Do something to clear the test environment here.
        pass
 
    def test_Given_Struct_Valid_With_Typedef_When_StructManager_ParseFromString_Then_Struct_Not_None(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_VALID_WITH_TYPEDEF)
        self.assertIsNotNone(structInstance)

    def test_Given_Struct_Valid_Without_Typedef_When_StructManager_ParseFromString_Then_Struct_Not_None(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_VALID_WITHOUT_TYPEDEF)
        self.assertIsNotNone(structInstance)

    def test_Given_Struct_Invalid_With_Typedef_When_StructManager_ParseFromString_Then_Struct_None(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_INVALID_WITH_TYPEDEF)
        self.assertIsNone(structInstance)

    def test_Given_Struct_Invalid_Without_Typedef_When_StructManager_ParseFromString_Then_Struct_None(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_INVALID_WITHOUT_TYPEDEF)
        self.assertIsNone(structInstance)

    def test_Given_Struct_Invalid_Without_StrStruct_When_StructManager_ParseFromString_Then_Struct_None(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_INVALID_WITHOUT_STRUCT)
        self.assertIsNone(structInstance)

    def test_Given_Struct_Invalid_Without_Semicolon_When_StructManager_ParseFromString_Then_Struct_None(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_INVALID_WITHOUT_SEMICOLON)
        self.assertIsNone(structInstance)

 
if __name__ == '__main__':
    unittest.main()