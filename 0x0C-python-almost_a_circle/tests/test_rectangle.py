#!/usr/bin/python3
"""Unit tests for the Rectangle class"""

from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
import os
import io
from unittest.mock import patch

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

    def test_area(self):
        """Test the area() method"""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str_method(self):
        """Test the __str__ method"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_xy(self):
        """Test display() method without x and y"""
        r = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_no_y(self):
        """Test display() method without y"""
        r = Rectangle(3, 2, 1)
        expected_output = " ###\n ###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        """Test display() method"""
        r = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_to_dictionary(self):
        """Test the to_dictionary() method"""
        r = Rectangle(10, 2, 1, 9)
        r_dict = r.to_dictionary()
        expected_dict = {'id': r.id, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r_dict, expected_dict)

    def test_save_to_file_none(self):
        """Test save_to_file with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_empty_list(self):
        """Test save_to_file with an empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file(self):
        """Test save_to_file with a list containing one Rectangle"""
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            expected_output = '[{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8}]'
            self.assertEqual(file.read(), expected_output)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file doesn't exist"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """Test load_from_file when file exists"""
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 1)
        self.assertEqual(str(rectangles[0]), str(r))


if __name__ == "__main__":
    unittest.main()
