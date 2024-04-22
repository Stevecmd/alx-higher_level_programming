#!/usr/bin/python3
"""Unit tests for the Rectangle class"""

from models.rectangle import Rectangle
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_constructor_no_id(self):
        """Test constructor with no id provided"""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)

    def test_constructor_with_id(self):
        """Test constructor with id provided"""
        r = Rectangle(2, 10, id=5)
        self.assertEqual(r.id, 5)

    def test_width_getter_setter(self):
        """Test width getter and setter"""
        r = Rectangle(5, 10)
        r.width = 15
        self.assertEqual(r.width, 15)

    def test_height_getter_setter(self):
        """Test height getter and setter"""
        r = Rectangle(5, 10)
        r.height = 20
        self.assertEqual(r.height, 20)

    def test_x_getter_setter(self):
        """Test x getter and setter"""
        r = Rectangle(5, 10, 1)
        r.x = 2
        self.assertEqual(r.x, 2)

    def test_y_getter_setter(self):
        """Test y getter and setter"""
        r = Rectangle(5, 10, 1, 2)
        r.y = 3
        self.assertEqual(r.y, 3)

    def test_constructor_negative_width(self):
        """Test constructor with negative width"""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10)

    def test_constructor_negative_height(self):
        """Test constructor with negative height"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10)

    def test_constructor_negative_x(self):
        """Test constructor with negative x"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -1)

    def test_constructor_negative_y(self):
        """Test constructor with negative y"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 1, -2)

    def test_constructor_non_integer_width(self):
        """Test constructor with non-integer width"""
        with self.assertRaises(TypeError):
            r = Rectangle("string", 10)

    def test_constructor_non_integer_height(self):
        """Test constructor with non-integer height"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, "string")

    def test_constructor_non_integer_x(self):
        """Test constructor with non-integer x"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "string")

    def test_constructor_non_integer_y(self):
        """Test constructor with non-integer y"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 1, "string")


if __name__ == "__main__":
    unittest.main()
