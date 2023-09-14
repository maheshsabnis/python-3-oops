# The class methods are shared across instances of the class
# The class method accepts a pre-defined 'cls' parameter

class Person:
    id=0
    name=''
    def __init__(self,id,name):
        self.id = id
        self.name = name
        print(f"in init id = {self.id} and name = {self.name}")

    def printInfo(self):
        print(f"in instance method id = {self.id} and name = {self.name}")    

    # defining the class method 
    @classmethod
    def create_object(cls):
        return Person(1001,'Mahesh')   
    
person = Person(1,'A')
person.printInfo()

# Get the person object
p1 = Person.create_object()
p1.printInfo()
