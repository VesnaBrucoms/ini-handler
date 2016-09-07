# Ini Handler

[![Version](https://img.shields.io/badge/version-0.3.1-green.svg)](https://github.com/VesnaBrucoms/ini-handler/tree/master)

Ini Handler is a simple and small Python library for reading and writing .ini
setting files.

Ini Handler makes implementing user customisable settings painless and simple. It
achieves this by limiting the number of methods you have to remember to be able to
do what you want to do.

For example:

    from ini_handler.vbini import Ini

    ini_file = Ini()
    ini_file['NewSetting'] = 'Simple!'

    print(ini_file['NewSetting'])

Output:

    'Simple!'

Just like that we have created and retrieved a new setting!

## Testing

To run the unit tests (with vbini.py as an example):

    python tests\unit-tests\test_vbini.py -v
