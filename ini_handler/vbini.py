"""The main object for Ini Handler"""


class Ini(object):

    def __init__(self, filename='settings', location=None):
        self._filename = filename
        self._location = location
        self._settings = {}

    def __delitem__(self, key):
        if not type(key) == str:
            raise TypeError('Key must be of type string')

        if key in self._settings:
            self._settings.pop(key)
        else:
            raise KeyError('{} not found'.format(key))

    def __getitem__(self, key):
        if not type(key) == str:
            raise TypeError('Key must be of type string')

        if key in self._settings:
            return self._settings[key]
        else:
            raise KeyError('{} not found'.format(key))

    def __len__(self):
        return len(self._settings)

    def __setitem__(self, key, value):
        if not type(key) == str:
            raise TypeError('Key must be of type string')

        self._settings[key] = value

    def __str__(self):
        return str(self._settings)
