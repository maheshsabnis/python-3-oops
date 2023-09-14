#A static method is not bound to a class or any 
# instances of the class. In Python, you use static 
# methods to group logically related functions in a class. 

class Utilities:
     @staticmethod
     def reverseString(str):
         return ''.join(reversed(str))

 
str = 'My Name is Bond, James Bond'

print(Utilities.reverseString(str))

