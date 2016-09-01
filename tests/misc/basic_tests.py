from ini_handler.vbini import Ini


ini_file = Ini()

print('Items:', len(ini_file))

ini_file['testKey'] = 'test string'
print('')
print('Items:', len(ini_file))
print('Item 1:', ini_file['testKey'])

print(ini_file)
print(str(ini_file))

del ini_file['testKey']
print('')
print('Items:', len(ini_file))
del ini_file['testKey']

# print('')
# print('KeyError:')
# print('Item 1:', ini_file['tesey'])

# print('')
# print('TypeError:')
# print('Item 1:', ini_file[1])
