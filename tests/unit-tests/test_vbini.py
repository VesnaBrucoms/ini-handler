"""Unittests for the vbini.py module"""
import unittest
from ini_handler.vbini import Ini


class TestIni(unittest.TestCase):

    def test_instantiate(self):
        ini_file = Ini()

    def test_instantiate_with_filename(self):
        ini_file = Ini(filename='wizard')
        self.assertEqual(ini_file.filename, 'wizard')

    def test_instantiate_with_directory(self):
        ini_file = Ini(directory='\\test\\directory')
        self.assertEqual(ini_file.directory, '\\test\\directory')

    def test_add_setting(self):
        ini_file = Ini()
        ini_file['test'] = 'wizard'

    def test_add_setting_with_key_type_error(self):
        ini_file = Ini()
        with self.assertRaises(TypeError):
            ini_file[564] = 'wizard'

    def test_get_setting(self):
        ini_file = Ini()
        ini_file['test'] = 'wizard'
        self.assertEqual(ini_file['test'], 'wizard')

    def test_get_setting_key_error(self):
        ini_file = Ini()
        with self.assertRaises(KeyError):
            ini_file['test']

    def test_get_length_empty(self):
        ini_file = Ini()
        self.assertEqual(len(ini_file), 0)

    def test_get_length_not_empty(self):
        ini_file = Ini()
        ini_file['test'] = 'wizard'
        ini_file['castSpell'] = True
        self.assertEqual(len(ini_file), 2)

if __name__ == '__main__':
    unittest.main()
