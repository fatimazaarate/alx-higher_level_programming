#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_no_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_with_all_args(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 12, 9)

    def test_x_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, '1', 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 5.7, 1, 12)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 4, 12)

    def test_y_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, 'hi', 12)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -4, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 5, 1.1, 12)

    def test_width_error(self):
        with self.assertRaises(TypeError):
            Rectangle('10', 2, 0, 1, 12)

    def test_height_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, '2', 0, 1, 12)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        with self.assertRaises(TypeError):
            Rectangle(3).display()

    def test_str_def_args(self):
        """Testing __str__ with default args"""
        r1 = Rectangle(2, 3)
        output = "[Rectangle] ({}) 0/0 - 2/3".format(r1.id)
        self.assertEqual(str(r1), output)

    def test_update_id(self):
        """Testing with one argument"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_two_args(self):
        """Testing update with two arguments"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_no_args(self):
        """Testing update with no args given"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (12) 10/10 - 10/10")


if __name__ == '__main__':
    unittest.main()