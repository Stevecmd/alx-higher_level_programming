#!/usr/bin/python3
"""Unit tests for the Square class"""

import unittest
from models.square import Square
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_str_method(self):
        """Test the existence of the __str__() method"""
        s = Square(1)
        self.assertTrue(hasattr(s, '__str__'))

    def test_str_method(self):
        """Test the __str__ method"""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_square_num_1_2(self):
        """Test Square(1, 2)"""
        s = Square(1, 2)
        self.assertIsNotNone(s)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.area(), 1)
        self.assertEqual(str(s), "[Square] ({}) 2/0 - 1".format(s.id))

    def test_square_1_2_3_4(self):
        """Test Square(1, 2, 3, 4)"""
        s = Square(1, 2, 3, 4)
        self.assertIsNotNone(s)

    def test_square_1_2_string_3(self):
        """Test Square(1, 2, "3")"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_1_string_2(self):
        """Test Square("1")"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_1_2_3(self):
        """Test Square(1, 2, 3)"""
        s = Square(1, 2, 3)
        self.assertIsNotNone(s)

    def test_square_1_2(self):
        """Test Square(1, 2)"""
        s = Square(1, 2)
        self.assertIsNotNone(s)

    def test_save_to_file_none(self):
        """Test the existence of the save_to_file(None) method"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == "__main__":
    unittest.main()
