# -*- coding: utf-8 -*-
# make print compatible with python 2.7
from __future__ import print_function

import unittest
import program

class testFunctionality(unittest.TestCase):

    def test_is_greater(self):
        self.assertEqual(program.is_greater(5,2), True)

    def test_is_not_greater(self):
        self.assertEqual(program.is_greater(2,2), False)

    def test_is_smaller(self):
        self.assertEqual(program.is_smaller(1,2), True)

    def test_is_not_smaller(self):
        self.assertEqual(program.is_smaller(3,2), False)

if __name__ == "__main__":
    unittest.main()

