#__pycache__ is a directory that is created by 
# the Python interpreter when it imports a module. 
# It contains the compiled bytecode of the module, 
# which can be used to speed up subsequent imports 
# of the same module.

import stringutilities

length = stringutilities.getStringLength('Mahesh')

print(length)

reverse = stringutilities.reverseString('Leena Mahesh Sabnis')

print(reverse)

upper = stringutilities.changeCase('james bond', 'u')

print(upper)

lower  =stringutilities.changeCase('james bond', 'l')

print(lower)