""" Ini Handler Sections object """
from ini_handler.utilities import validate_key_type


class Sections(object):

    def __init__(self):
        self._sections = {}

    def __getitem__(self, key):
        validate_key_type(key)

        try:
            return self._sections[key]
        except KeyError:
            raise KeyError('{} not found'.format(key))

    def __iter__(self):
        for key in self._sections:
            yield key

    def __len__(self):
        return len(self._sections)

    def __setitem__(self, key, value):
        validate_key_type(key)

        old_key = self._check_value_exists_in_key(value)
        if old_key is not None:
            self.remove_setting(old_key, value)

        if key in self._sections:
            self._sections[key].add(value)
        else:
            new_set = set()
            new_set.add(value)
            self._sections[key] = new_set

    def __str__(self):
        return str(self._sections)

    def remove_setting(self, key, value):
        if value is not None:
            self._sections[key].remove(value)

    def _check_value_exists_in_key(self, value):
        for key in self._sections:
            for item in self._sections[key]:
                if item == value:
                    return key

        return None
