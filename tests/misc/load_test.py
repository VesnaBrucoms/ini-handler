from ini_handler.vbini import Ini


if __name__ == '__main__':
    ini_file = Ini()
    ini_file.load()
    print(ini_file._settings)
    print(ini_file['testKey'])
