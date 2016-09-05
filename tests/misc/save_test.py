from ini_handler.vbini import Ini


if __name__ == '__main__':
    ini_file = Ini()
    ini_file['test'] = 'at top of file'
    ini_file['set1'] = ['newSection', 'in newSection']
    ini_file['set2'] = ('newSection', 'also newSection')
    ini_file['bob'] = ['wizards', True]
    ini_file['will'] = ['wizards', False]
    ini_file.save()
    print(ini_file._settings)
    print(ini_file._sections)
