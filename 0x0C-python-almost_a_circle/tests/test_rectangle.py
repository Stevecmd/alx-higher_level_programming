#!/usr/bin/python3
"""Unit tests for the Rectangle class"""

from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Reset the __nb_objects counter before each test"""
        Base._Base__nb_objects = 0

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


    def test_rectangle_1_2_exists(self):
        """Test constructor with width=1 and height=2"""
        r = Rectangle(1, 2)
        self.assertIsNotNone(r)

    def test_rectangle_1_2_3_exists(self):
        """Test constructor with width=1, height=2, and x=3"""
        r = Rectangle(1, 2, 3)
        self.assertIsNotNone(r)

    def test_rectangle_1_2_3_4_exists(self):
        """Test constructor with width=1, height=2, x=3, and y=4"""
        r = Rectangle(1, 2, 3, 4)
        self.assertIsNotNone(r)

    def test_rectangle_0_2_exists(self):
        """Test constructor with width=0 and height=2"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_rectangle_1_0_exists(self):
        """Test constructor with width=1 and height=0"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_str_method_exists(self):
        """Test the existence of the __str__() method"""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, '__str__'))

    def test_to_dictionary_method_exists(self):
        """Test the existence of the to_dictionary() method"""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, 'to_dictionary'))

    def test_update_method_exists(self):
        """Test the existence of the update() method"""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, 'update'))

    def test_update_89_method_exists(self):
        """Test the existence of the update(89) method"""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, 'update'))
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1_method_exists(self):
        """Test the existence of the update(89, 1) method"""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, 'update'))
        r.update(89, 1)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_update_89_1_2_method_exists(self):
        """Test the existence of the update(89, 1, 2) method"""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, 'update'))
        r.update(89, 1, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_update_89_1_2_3_method_exists(self):
        """Test the existence of the update(89, 1, 2, 3) method"""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, 'update'))
        r.update(89, 1, 2, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_update_89_1_2_3_4_method_exists(self):
        """Test the existence of the update(89, 1, 2, 3, 4) method"""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, 'update'))
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_with_dictionary_method_exists(self):
        """Test the existence of the update(**{'id': 89}) method"""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, 'update'))
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)



if __name__ == "__main__":
    unittest.main()
