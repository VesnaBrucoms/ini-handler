""" Ini Handler main Ini object """
import re
import sys
import os

from ini_handler.sections import Sections
from ini_handler.utilities import validate_key_type


class Ini(object):
    """Ini(filename, directory)

    Representation of the ini file.

    Stores all settings and sections; handles all loading and saving.
    """

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
        for key in self._settings:
            yield (key, self[key])

    def __len__(self):
        return len(self._settings)

    def __setitem__(self, key, value):
        validate_key_type(key)

        if type(value) in [list, tuple, set]:
            self._settings[key] = [value[0], value[1]]
            if value[0] is not None:
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
        """Returns the section the setting is assigned to.

        Args:
            key(str):   setting key
        """
        validate_key_type(key)

        return self._settings[key][0]

    def set_setting_section(self, key, section):
        """Sets the section the setting is assigned to.

        Args:
            key(str):       setting key
            section(str):   section name
        """
        validate_key_type(key)

        self[key] = [section, self[key]]

    def load(self):
        """Read the .ini file.
        """
        with open(self._filepath, 'rt') as ini_file:
            current_section = None
            for line in ini_file:
                if line == '\n':
                    continue
                if line.startswith('[') and line[:-1].endswith(']'):
                    current_section = line[1:-2]
                    continue

                line = line[:-1].split('=')
                line[1] = self._check_and_convert_type(line[1])
                self[line[0]] = [current_section, line[1]]

    def save(self):
        """Write the .ini file.
        """
        with open(self._filepath, 'wt') as ini_file:
            for key in self._settings:
                if self.get_setting_section(key) is None:
                    ini_file.write('{}={}\n'.format(key, str(self[key])))

            for section in self._sections:
                ini_file.write('\n')
                ini_file.write('[{}]\n'.format(section))
                for setting_key in self._sections[section]:
                    ini_file.write('{}={}\n'.format(setting_key,
                                                    str(self[setting_key])))

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
