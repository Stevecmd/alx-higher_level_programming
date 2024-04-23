# #!/usr/bin/python3
# """Unit tests for the Base class"""

# from models.base import Base
# import unittest
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# class TestBase(unittest.TestCase):
#     """Test cases for the Base class"""

#     def setUp(self):
#         """Reset __nb_objects attribute before each test"""
#         Base._Base__nb_objects = 0

#     def test_constructor_no_id(self):
#         """Test constructor with no id provided"""
#         b = Base()
#         self.assertEqual(b.id, 1)

#     def test_constructor_with_id(self):
#         """Test constructor with id provided"""
#         b = Base(10)
#         self.assertEqual(b.id, 10)

#     def test_constructor_increment_id(self):
#         """Test constructor increments id"""
#         b1 = Base()
#         b2 = Base()
#         self.assertEqual(b2.id, b1.id + 1)

#     def test_constructor_non_integer_id(self):
#         """Test constructor with non-integer id"""
#         with self.assertRaises(TypeError):
#             b = Base("string")

#     def test_constructor_negative_id(self):
#         """Test constructor with negative id"""
#         with self.assertRaises(ValueError):
#             b = Base(-1)

#     def test_constructor_zero_id(self):
#         """Test constructor with zero id"""
#         b = Base(0)
#         self.assertEqual(b.id, 0)

#     def test_constructor_max_int_id(self):
#         """Test constructor with maximum integer id"""
#         max_int = sys.maxsize
#         b = Base(max_int)
#         self.assertEqual(b.id, max_int)

#     def test_constructor_max_int_id_overflow(self):
#         """Test constructor with maximum integer id overflow"""
#         max_int = sys.maxsize
#         b1 = Base(max_int)
#         b2 = Base()
#         self.assertEqual(b2.id, 1)

#     def test_constructor_same_id(self):
#         """Test constructor with same id"""
#         b1 = Base(5)
#         b2 = Base(5)
#         self.assertEqual(b1.id, b2.id)

#     def test_constructor_negative_max_int_id(self):
#         """Test constructor with negative maximum integer id"""
#         with self.assertRaises(ValueError):
#             b = Base(-sys.maxsize)


# if __name__ == "__main__":
#     unittest.main()
