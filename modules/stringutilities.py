# Define some string methods

def getStringLength(str):
    return len(str)

def reverseString(str):
    return ''.join(reversed(str))

def changeCase(str,c):
    if c == 'u' or c == 'U':
       return str.upper() 
    if c == 'l' or c == 'L':
       return str.lower() 

