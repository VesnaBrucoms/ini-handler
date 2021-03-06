"""Unittests for the vbini.py module"""
import functools
import re
import unittest
from unittest import mock
from ini_handler.vbini import Ini


mock_ini_data = 'test=wizard\ncastSpell=True\npunch=1\n\n[section]\nghost=False\n'


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

    def test_add_setting_with_section(self):
        ini_file = Ini()
        ini_file['test'] = ('people', 'wizard')
        self.assertEqual(ini_file['test'], 'wizard')
        self.assertEqual(ini_file.get_setting_section('test'), 'people')

    def test_add_setting_with_key_type_error(self):
        ini_file = Ini()
        with self.assertRaises(TypeError):
            ini_file[564] = 'wizard'

    def test_get_setting(self):
        ini_file = Ini()
        ini_file['test'] = 'wizard'
        self.assertEqual(ini_file['test'], 'wizard')

    def test_get_setting_section(self):
        ini_file = Ini()
        ini_file['test'] = ['magicPeople', 'wizard']
        self.assertEqual(ini_file.get_setting_section('test'), 'magicPeople')

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

    def test_iteration(self):
        ini_file = Ini()
        ini_file['set1'] = 'data'
        ini_file['set2'] = 'great'
        ini_file['set3'] = 'help'
        ini_file['set4'] = 'info'
        ini_file['bob'] = ['wizards', True]

        settings_list = {}
        for setting in ini_file:
            settings_list[setting[0]] = setting[1]

        expected_result = dict([('set1', 'data'), ('set2', 'great'),
                                ('set3', 'help'), ('set4', 'info'),
                                ('bob', True)])
        self.assertEqual(settings_list, expected_result)

    @mock.patch('builtins.open')
    def test_load(self, open_mock):
        context_manager_mock = mock.Mock()
        open_mock.return_value = context_manager_mock
        file_mock = mock.Mock()
        iter_mock = mock.Mock()
        iter_mock.return_value = iter(self._split_but_keep_seperated(mock_ini_data,
                                                                     '\n'))
        enter_mock = mock.Mock()
        enter_mock.return_value = file_mock
        exit_mock = mock.Mock()
        setattr(context_manager_mock, '__enter__', enter_mock)
        setattr(context_manager_mock, '__exit__', exit_mock)
        setattr(file_mock, '__iter__', iter_mock)

        ini_file = Ini()
        ini_file.load()
        result = {}
        result['test'] = [None, 'wizard']
        result['castSpell'] = [None, True]
        result['punch'] = [None, 1]
        result['ghost'] = ['section', False]
        result_sections = {}
        result_sections['section'] = set()
        result_sections['section'].add('ghost')

        self.assertEqual(ini_file._settings, result)
        self.assertEqual(ini_file._sections._sections, result_sections)

    def _split_but_keep_seperated(self, s, sep):
        return functools.reduce(lambda acc,
                                i: acc[:-1] + [acc[-1] + i] if i == sep else acc + [i],
                                re.split("(%s)" % re.escape(sep), s),
                                [])

if __name__ == '__main__':
    unittest.main()
