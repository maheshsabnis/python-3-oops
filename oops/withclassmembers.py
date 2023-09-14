class Person:
    id=1
    name='Mahesh'

    def __init__(self):
        print(f"id={self.id} and name = {self.name}")

    def printInfo(self):
        print(f"In Method id={self.id} and name = {self.name}")   
        self.id=800 
    
person = Person()
person.printInfo()
person.id =100
person.printInfo() # Here id will be 100
person.printInfo() # Here the id will be 800


