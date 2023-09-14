class Person:
    def __init__(self, id,name):
        self.id = id
        self.name = name

    def printInfo(self):    
        print(f"id = {self.id} name = {self.name}")


person = Person(1,'A')

person.printInfo()