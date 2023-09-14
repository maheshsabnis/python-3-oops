from stringutilities import getStringLength, reverseString, changeCase
str = 'My Name is Bond, James Bond'
print(f'Length = { getStringLength(str)}')

print('Reverse = ' + reverseString(str))

print('Upper case = ' + changeCase(str, 'U'))

print('Lower case = ' + changeCase(str, 'L'))
