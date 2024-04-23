#!/usr/bin/python3
"""Unit tests for the Square class"""

import unittest
from models.square import Square
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_square_1_exists(self):
        """Test Square(1) exists"""
        s = Square(1)
        self.assertIsNotNone(s)

    def test_square_1_2_exists(self):
        """Test Square(1, 2) exists"""
        s = Square(1, 2)
        self.assertIsNotNone(s)

    def test_square_1_2_3_exists(self):
        """Test Square(1, 2, 3) exists"""
        s = Square(1, 2, 3)
        self.assertIsNotNone(s)

    def test_square_string_1_exists(self):
        """Test Square("1") exists"""
        s = Square(1)
        self.assertIsNotNone(s)

    def test_square_1_string_2_exists(self):
        """Test Square(1, "2") exists"""
        s = Square(1, 2)
        self.assertIsNotNone(s)

    def test_square_1_2_string_3_exists(self):
        """Test Square(1, 2, "3") exists"""
        s = Square(1, 2, 3)
        self.assertIsNotNone(s)

    def test_square_1_2_3_4_exists(self):
        """Test Square(1, 2, 3, 4) exists"""
        s = Square(1, 2, 3, 4)
        self.assertIsNotNone(s)

    def test_square_negative_1_exists(self):
        """Test Square(-1) exists"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_1_negative_2_exists(self):
        """Test Square(1, -2) exists"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_1_2_negative_3_exists(self):
        """Test Square(1, 2, -3) exists"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_0_exists(self):
        """Test Square(0) exists"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str_method_exists(self):
        """Test the existence of the __str__() method"""
        s = Square(1)
        self.assertTrue(hasattr(s, '__str__'))

    def test_to_dictionary_method_exists(self):
        """Test the existence of the to_dictionary() method"""
        s = Square(1)
        self.assertTrue(hasattr(s, 'to_dictionary'))

    def test_update_method_exists(self):
        """Test the existence of the update() method"""
        s = Square(1)
        self.assertTrue(hasattr(s, 'update'))

    def test_update_89_method_exists(self):
        """Test the existence of the update(89) method"""
        s = Square(1)
        self.assertTrue(hasattr(s, 'update'))
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1_method_exists(self):
        """Test the existence of the update(89, 1) method"""
        s = Square(1)
        self.assertTrue(hasattr(s, 'update'))
        s.update(89, 1)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_update_89_1_2_method_exists(self):
        """Test the existence of the update(89, 1, 2) method"""
        s = Square(1)
        self.assertTrue(hasattr(s, 'update'))
        s.update(89, 1, 2)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_update_89_1_2_3_method_exists(self):
        """Test the existence of the update(89, 1, 2, 3) method"""
        s = Square(1)
        self.assertTrue(hasattr(s, 'update'))
        s.update(89, 1, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_with_dictionary_method_exists(self):
        """Test the existence of the update(**{'id': 89}) method"""
        s = Square(1)
        self.assertTrue(hasattr(s, 'update'))
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_method_exists(self):
        """Test the existence of the create() method"""
        self.assertTrue(hasattr(Square, 'create'))

    def test_create_89_method_exists(self):
        """Test the existence of the create(89) method"""
        s = Square.create(id=89)
        self.assertEqual(s.id, 89)

    def test_create_89_1_method_exists(self):
        """Test the existence of the create(89, 1) method"""
        s = Square.create(id=89, size=1)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_create_89_1_2_method_exists(self):
        """Test the existence of the create(89, 1, 2) method"""
        s = Square.create(id=89, size=1, x=2)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_create_89_1_2_3_method_exists(self):
        """Test the existence of the create(89, 1, 2, 3) method"""
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_save_to_file_method_exists(self):
        """Test the existence of the save_to_file() method"""
        self.assertTrue(hasattr(Square, 'save_to_file'))

    def test_save_to_file_none_method_exists(self):
        """Test the existence of the save_to_file(None) method"""
        self.assertTrue(hasattr(Square, 'save_to_file'))

    def test_save_to_file_empty_list_method_exists(self):
        """Test the existence of the save_to_file([]) method"""
        self.assertTrue(hasattr(Square, 'save_to_file'))

    def test_save_to_file_square_1_method_exists(self):
        """Test the existence of the save_to_file([Square(1)]) method"""
        self.assertTrue(hasattr(Square, 'save_to_file'))

    def test_load_from_file_not_exist_method_exists(self):
        """Test the existence of load_from_file() method if no file"""
        self.assertTrue(hasattr(Square, 'load_from_file'))

    def test_load_from_file_exist_method_exists(self):
        """Test the existence of the load_from_file() method if file exists"""
        self.assertTrue(hasattr(Square, 'load_from_file'))


if __name__ == "__main__":
    unittest.main()
