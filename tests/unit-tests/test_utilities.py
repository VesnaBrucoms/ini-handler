"""Unittests for the utilities.py module"""
import unittest
from ini_handler.utilities import validate_key_type


class TestUtilities(unittest.TestCase):

    def test_validate_key_type(self):
        validate_key_type('test')

    def test_validate_key_type_with_error(self):
        with self.assertRaises(TypeError):
            validate_key_type(3)

if __name__ == '__main__':
    unittest.main()
