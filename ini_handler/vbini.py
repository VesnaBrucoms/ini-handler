"""The main object for Ini Handler"""
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
        return self._directory + '\\' + self._filename + '.ini'

    @property
    def filename(self):
        return self._filename

    @property
    def directory(self):
        return self._directory

    def load(self):
        pass

    def save(self):
        pass
