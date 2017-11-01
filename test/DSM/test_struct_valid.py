"""
test struct type
"""

import sys
sys.path.append('../../')
import source.DSM.struct as struct
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
 
    def setUp(self):
        self.sm_handler = struct.SM()
        pass
 
    def tearDown(self):
        # Do something to clear the test environment here.
        pass
 
    def test_struct_valid_with_typedef(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_VALID_WITH_TYPEDEF)
        self.assertIsNotNone(structInstance)

    def test_struct_valid_without_typedef(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_VALID_WITHOUT_TYPEDEF)
        self.assertIsNotNone(structInstance)

    def test_struct_invalid_with_typedef(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_INVALID_WITH_TYPEDEF)
        self.assertIsNone(structInstance)

    def test_struct_invalid_without_typedef(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_STR_INVALID_WITHOUT_TYPEDEF)
        self.assertIsNone(structInstance)

 
if __name__ == '__main__':
    unittest.main()