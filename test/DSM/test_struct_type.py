"""
test struct type
"""

import sys
sys.path.append('../../')
sys.path.append('../../source/DSM')
from StructType import *
from StructManager import *
import unittest

class TestStructType(unittest.TestCase):

    TYPEDEF_STRUCT_A_XXX_T1 = \
"typedef struct A\r\n\
{\r\nint a[2];\r\n\
struct B {\r\nint b;\r\n};\r\n\
double *pdB;\r\n\
} T_TEST;"

    TYPEDEF_STRUCT_A_XXX_T1_PT2 = \
"typedef struct A\r\n\
{\r\nint a[2];\r\n\
struct B {\r\nint b;\r\n};\r\n\
double *pdB;\r\n\
} T_TEST, P_T_TEST;"

    TYPEDEF_STRUCT_XXX_T1 = \
"typedef struct\r\n\
{\r\nint a[2];\r\n\
struct B {\r\nint b;\r\n};\r\n\
double *pdB;\r\n\
} T_TEST;"

    TYPEDEF_STRUCT_XXX = \
"typedef struct\r\n\
{\r\nint a[2];\r\n\
struct B {\r\nint b;\r\n};\r\n\
double *pdB;\r\n};"

    TYPEDEF_STRUCT_A_XXX = \
"typedef struct A\r\n\
{\r\nint a[2];\r\n\
struct B {\r\nint b;\r\n};\r\n\
double *pdB;\r\n};"

    STRUCT_A_XXX = \
"struct A\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n\};\r\n\
double *pdB;\r\n};"

    STRUCT_A_XXX_M1 = \
"struct A\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n\};\r\n\
double *pdB;\r\n\
} M1;"

    STRUCT_A_XXX_M1_PM1 = \
"struct A\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n\};\r\n\
double *pdB;\r\n\
} M1,  *PM1;"

    STRUCT_XXX_M1 = \
"struct\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n\};\r\n\
double *pdB;\r\n\
} M1; "

    STRUCT_XXX = \
"struct\r\n\
{\r\nint a[2];\r\n\
struct A {\r\nint b;\r\n\};\r\n\
double *pdB;\r\n\
} ; "


    def setUp(self):
        self.sm_handler = SM()
        pass
 
    def tearDown(self):
        # Do something to clear the test environment here.
        pass
 
    def test_Given_TYPEDEF_STRUCT_A_XXX_T1_When_StructType_ParseType_Then_Struct_Info_Correct(self):
        structInstance = self.sm_handler.parse_from_string(self.TYPEDEF_STRUCT_A_XXX_T1)
        structType = structInstance.struct_type

        self.assertEqual(structType.type, StructType.TYPEDEF_STRUCT_A_XXX_T)
        self.assertTrue(structType.valid)
        self.assertTrue(structType.typedef)
        self.assertListEqual(structType.names, ['struct A', 'T_TEST'])
        self.assertListEqual(structType.objs, [])

    def test_Given_TYPEDEF_STRUCT_A_XXX_T1_PT2_When_StructType_ParseType_Then_Struct_Info_Correct(self):
        structInstance = self.sm_handler.parse_from_string(self.TYPEDEF_STRUCT_A_XXX_T1_PT2)
        structType = structInstance.struct_type

        self.assertEqual(structType.type, StructType.TYPEDEF_STRUCT_A_XXX_T)
        self.assertTrue(structType.valid)
        self.assertTrue(structType.typedef)
        self.assertListEqual(structType.names, ['struct A', 'T_TEST', 'P_T_TEST'])
        self.assertListEqual(structType.objs, [])

    def test_Given_TYPEDEF_STRUCT_XXX_T1_When_StructType_ParseType_Then_Struct_Info_Correct(self):
        structInstance = self.sm_handler.parse_from_string(self.TYPEDEF_STRUCT_XXX_T1)
        structType = structInstance.struct_type

        self.assertEqual(structType.type, StructType.TYPEDEF_STRUCT_XXX_T)
        self.assertTrue(structType.valid)
        self.assertTrue(structType.typedef)
        self.assertListEqual(structType.names, ['T_TEST'])
        self.assertListEqual(structType.objs, [])

    def test_Given_TYPEDEF_STRUCT_XXX_When_StructType_ParseType_Then_Struct_Info_Correct(self):
        structInstance = self.sm_handler.parse_from_string(self.TYPEDEF_STRUCT_XXX)
        structType = structInstance.struct_type

        self.assertEqual(structType.type, StructType.TYPEDEF_STRUCT_XXX_INVALID)
        self.assertFalse(structType.valid)
        self.assertTrue(structType.typedef)
        self.assertListEqual(structType.names, [])
        self.assertListEqual(structType.objs, [])

    def test_Given_TYPEDEF_STRUCT_A_XXX_When_StructType_ParseType_Then_Struct_Info_Correct(self):
        structInstance = self.sm_handler.parse_from_string(self.TYPEDEF_STRUCT_A_XXX)
        structType = structInstance.struct_type

        self.assertEqual(structType.type, StructType.TYPEDEF_STRUCT_A_XXX_INVALID)
        self.assertFalse(structType.valid)
        self.assertTrue(structType.typedef)
        self.assertListEqual(structType.names, [])
        self.assertListEqual(structType.objs, [])

    def test_Given_STRUCT_A_XXX_When_StructType_ParseType_Then_Struct_Info_Correct(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_A_XXX)
        structType = structInstance.struct_type

        self.assertEqual(structType.type, StructType.STRUCT_A_XXX)
        self.assertTrue(structType.valid)
        self.assertFalse(structType.typedef)
        self.assertListEqual(structType.names, ['struct A'])
        self.assertListEqual(structType.objs, [])

    def test_Given_STRUCT_A_XXX_M1_When_StructType_ParseType_Then_Struct_Info_Correct(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_A_XXX_M1)
        structType = structInstance.struct_type

        self.assertEqual(structType.type, StructType.STRUCT_A_XXX_V_T)
        self.assertTrue(structType.valid)
        self.assertFalse(structType.typedef)
        self.assertListEqual(structType.names, ['struct A'])
        self.assertListEqual(structType.objs, ['M1'])
    
    def test_Given_STRUCT_A_XXX_M1_PM1_When_StructType_ParseType_Then_Struct_Info_Correct(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_A_XXX_M1_PM1)
        structType = structInstance.struct_type

        self.assertEqual(structType.type, StructType.STRUCT_A_XXX_V_T)
        self.assertTrue(structType.valid)
        self.assertFalse(structType.typedef)
        self.assertListEqual(structType.names, ['struct A'])
        self.assertListEqual(structType.objs, ['M1', '*PM1'])

    def test_Given_STRUCT_XXX_M1_When_StructType_ParseType_Then_Struct_Info_Correct(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_XXX_M1)
        structType = structInstance.struct_type

        self.assertEqual(structType.type, StructType.STRUCT_XXX_V_T)
        self.assertTrue(structType.valid)
        self.assertFalse(structType.typedef)
        self.assertListEqual(structType.names, [])
        self.assertListEqual(structType.objs, ['M1'])

    def test_Given_STRUCT_XXX_When_StructType_ParseType_Then_Struct_Info_Correct(self):
        structInstance = self.sm_handler.parse_from_string(self.STRUCT_XXX)
        structType = structInstance.struct_type

        self.assertEqual(structType.type, StructType.STRUCT_XXX_INVALID)
        self.assertFalse(structType.valid)
        self.assertFalse(structType.typedef)
        self.assertListEqual(structType.names, [])
        self.assertListEqual(structType.objs, [])

if __name__ == '__main__':
    unittest.main()