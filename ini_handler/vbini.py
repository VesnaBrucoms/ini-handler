"""Ini Handler Ini object"""
import re
import sys
import os

from ini_handler.sections import Sections
from ini_handler.utilities import validate_key_type


class Ini(object):

    def __init__(self, filename='settings', directory=None):
        self._settings = {}
        self._sections = Sections()

        if filename.endswith('.ini'):
            self._filename = filename[:-4]
        else:
            self._filename = filename

        if directory is None:
            self._directory = os.path.expanduser('~')
            if sys.platform == 'win32':
                self._directory += '\\My Documents'
        else:
            self._directory = directory

        self._filepath = self._join_path()

    def __delitem__(self, key):
        validate_key_type(key)

        try:
            self._sections.remove_setting(self._settings[key][0], key)
            self._settings.pop(key)
        except KeyError:
            raise KeyError('{} not found'.format(key))

    def __getitem__(self, key):
        validate_key_type(key)

        try:
            return self._settings[key][1]
        except KeyError:
            raise KeyError('{} not found'.format(key))

    def __iter__(self):
        pass

    def __len__(self):
        return len(self._settings)

    def __setitem__(self, key, value):
        validate_key_type(key)

        if type(value) in [list, tuple, set]:
            self._settings[key] = [value[0], value[1]]
            self._sections[value[0]] = key
        elif key in self._settings:
            self._settings[key] = [self._settings[key][0], value]
        else:
            self._settings[key] = [None, value]

    def __str__(self):
        return self._filepath

    @property
    def filename(self):
        return self._filename

    @property
    def directory(self):
        return self._directory

    @property
    def filepath(self):
        return self._filepath

    def get_setting_section(self, key):
        validate_key_type(key)

        return self._settings[key][0]

    def set_setting_section(self, key, section):
        validate_key_type(key)

        self[key] = [section, self[key]]

    def load(self):
        with open(self._filepath, 'rt') as ini_file:
            for line in ini_file:
                line = line[:-1].split('=')
                line[1] = self._check_and_convert_type(line[1])
                self[line[0]] = line[1]

    def save(self):
        with open(self._filepath, 'wt') as ini_file:
            for key in self._settings:
                ini_file.write('{}={}\n'.format(key, str(self._settings[key])))

    def _join_path(self):
        if sys.platform == 'win32':
            return self._directory + '\\' + self._filename + '.ini'
        else:
            return self._directory + '/' + self._filename + '.ini'

    def _check_and_convert_type(self, value):
        if value == 'True' or value == 'true':
            return True
        elif value == 'False' or value == 'false':
            return False

        number = re.match(r'^[0-9]+$', value)
        if number:
            return int(number.group())

        return value
