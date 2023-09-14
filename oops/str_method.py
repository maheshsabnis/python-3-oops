# Sometimes, it’s useful to have a string representation of 
# an instance of a class. To customize the string 
# representation of a class instance, the class needs 
# to implement the __str__ magic method.

# Internally, Python will call the __str__ 
# method automatically when an instance calls the str() 
# method.

# Note that the print() function converts
# all non-keyword arguments to strings by passing 
# them to the str() before displaying the string values.

class MyClass:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __str__(self):
        return f" id = {self.id} name = {self.name}"        
    
    
obj = MyClass(101, 'Mahesh')
print(obj)    