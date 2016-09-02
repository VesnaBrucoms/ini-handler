from ini_handler.vbini import Ini


if __name__ == '__main__':
    ini_file = Ini()
    print(ini_file)
    print(ini_file.filename)
    print(ini_file.directory)

    print('Items:', len(ini_file))

    ini_file['testKey'] = 'test string'
    ini_file['Another'] = 'True'
    ini_file['setting'] = 1993
    ini_file['FinalSetting'] = 'bob'
    print('')
    print('Items:', len(ini_file))
    print('Item 1:', ini_file['testKey'])

    # del ini_file['testKey']
    # print('')
    # print('Items:', len(ini_file))
    # del ini_file['testKey']

    ini2 = Ini(filename='testing.ini')
    print(ini2.filename)
    print(ini2)

    ini_file.save()

    # print('')
    # print('KeyError:')
    # print('Item 1:', ini_file['tesey'])

    # print('')
    # print('TypeError:')
    # print('Item 1:', ini_file[1])
