#!/usr/bin/python3
"""Unit tests for the Square class"""

import unittest
from models.square import Square
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_str_method_exists(self):
        """Test the existence of the __str__() method"""
        s = Square(1)
        self.assertTrue(hasattr(s, '__str__'))

    def test_str_method(self):
        """Test the __str__ method"""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_square_1_2_3_4_exists(self):
        """Test Square(1, 2, 3, 4) exists"""
        s = Square(1, 2, 3, 4)
        self.assertIsNotNone(s)

    def test_square_1_2_string_3_exists(self):
        """Test Square(1, 2, "3") exists"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_1_string_2_exists(self):
        """Test Square("1") exists"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_1_2_3_exists(self):
        """Test Square(1, 2, 3) exists"""
        s = Square(1, 2, 3)
        self.assertIsNotNone(s)

    def test_square_1_2_exists(self):
        """Test Square(1, 2) exists"""
        s = Square(1, 2)
        self.assertIsNotNone(s)


if __name__ == "__main__":
    unittest.main()
