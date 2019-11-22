# Unit 1 Homework 9001 Test script
# Author: Chris Proctor and Jenny Han
# --------------------
# YOU DO NOT NEED TO UNDERSTAND THIS CODE RIGHT NOW!
# This script imports all the functions from your homework and tests them out. Hopefully they work!
# Testing is really important in computer science, so some nice functions are provided. We'll use them.

import unittest

from hw_01_9001 import *

class TestHomework_01_9000(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(mean([1]), 1.0)
        self.assertEqual(mean([0]), 0.0)
        self.assertEqual(mean([2, 6, 3, 11]), 5.5)


    def test_create_ones_list(self):
        self.assertEqual(create_ones_list(1), [1])
        self.assertEqual(create_ones_list(0), [])
        self.assertEqual(create_ones_list(5), [1,1,1,1,1])
        self.assertEqual(create_ones_list(50), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

    def test_is_even(self):
        self.assertEqual(is_even([1, 2, 3]), False)
        self.assertEqual(is_even([1, 2, 3, 4]), True)
        self.assertEqual(is_even([]), True)
        self.assertEqual(is_even([1]), False)

    def test_make_even(self):
        self.assertEqual(make_even(["hi"]), ["hi", "SIKE"])
        self.assertEqual(make_even(["1", "2"]),["1", "2"] )
        self.assertEqual(make_even(["say", "right", "now"]),["say", "right", "now","SIKE"] )
        self.assertEqual(make_even(["say", "sike", "right", "now"]),["say", "sike", "right", "now"] )

    def test_count_value_1(self):
        self.assertEqual(test_count_value_1([1, 1, 1, 1, 2, 2, 2, 3, 3, 4], 2), 3)
        self.assertEqual(test_count_value_1([1, 1, 1, 1, 2, 2, 2, 3, 3, 4], 3), 2)
        self.assertEqual(test_count_value_1([], 1), 0)

    def test_count_value_2(self):
        self.assertEqual(test_count_value_2([1, 1, 1, 1, 2, 2, 2, 3, 3, 4], 2), 3)
        self.assertEqual(test_count_value_2([1, 1, 1, 1, 2, 2, 2, 3, 3, 4], 3), 2)
        self.assertEqual(test_count_value_2([], 1), 0)

# This runs all the tests.
unittest.main(verbosity=2)
