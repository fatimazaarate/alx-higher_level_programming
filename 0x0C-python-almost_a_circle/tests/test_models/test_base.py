#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_no_args(self):
        b1 = Base(None)
        b2 = Base()
        b3 = Base()
        b4 = Base(None)
        b5 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b1.id, b5.id - 4)

    def test_not_None_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_int_id(self):
        self.assertEqual(Base(20).id, 20)

    def test_str_id(self):
        self.assertEqual(Base('hi').id, 'hi')
    
    def test_float_id(self):
        self.assertEqual(Base(2.6).id, 2.6)

    def test_more_args(self):
        with self.assertRaises(TypeError):
            base = Base(5, 4)

    


if __name__ == '__main__':
    unittest.main()
