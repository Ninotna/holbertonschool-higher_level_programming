#!/usr/bin/python3
import unittest
import sys
import os

# Add the parent directory to sys.path so Python can find the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from max_integer import max_integer  # Import the function from your module

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_regular_list(self):
        """Test with a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_with_negatives(self):
        """Test with a list containing negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_mixed_values(self):
        """Test with a list containing both positive and negative integers."""
        self.assertEqual(max_integer([-10, 5, 0, 10]), 10)

    def test_single_element_list(self):
        """Test with a list that contains a single element."""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test with an empty list, should return None."""
        self.assertIsNone(max_integer([]))

    def test_list_of_same_values(self):
        """Test with a list where all elements are the same."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_list_of_floats(self):
        """Test with a list of floating-point numbers."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_list_with_one_negative(self):
        """Test with a list that has one negative number."""
        self.assertEqual(max_integer([1, 2, -1, 3]), 3)

    def test_none_argument(self):
        """Test with an argument of None. Should raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_list_argument(self):
        """Test with a non-list argument like a string."""
        self.assertEqual(max_integer("hello"), 'o')


if __name__ == "__main__":
    unittest.main()
