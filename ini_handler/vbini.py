"""The main object for Ini Handler"""
import re
import sys
import os


class Ini(object):

    def __init__(self, filename='settings', directory=None):
        self._settings = {}

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
        if not type(key) == str:
            raise TypeError('Key must be of type string')

        try:
            self._settings.pop(key)
        except KeyError:
            raise KeyError('{} not found'.format(key))

    def __getitem__(self, key):
        if not type(key) == str:
            raise TypeError('Key must be of type string')

        try:
            return self._settings[key]
        except KeyError:
            raise KeyError('{} not found'.format(key))

    def __iter__(self):
        pass

    def __len__(self):
        return len(self._settings)

    def __setitem__(self, key, value):
        if not type(key) == str:
            raise TypeError('Key must be of type string')

        self._settings[key] = value

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
