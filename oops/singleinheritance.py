# The Base class

class Employee:
    __salary=0
    __name=''
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def calculateSalary(self):
       if self.__salary <= 10000:
          return self.__salary+(self.__salary * 0.2)  
       if self.__salary <= 50000:
          return self.__salary+(self.__salary * 0.25) 
       else:
          return self.__salary+(self.__salary * 0.3)   
       
# The derived class

class Manager(Employee):
      __ta = 0
      __da = 0
      def __init__(self,name,salary, ta, da):
          super().__init__(name,salary)
          self.__ta = ta
          self.__da = da  

      # Override the  calculateSalary() method
      def calculateSalary(self):
          return super().calculateSalary() + self.__ta + self.__da   
         
manager = Manager('Mahesh',200000,20000,3000)
          
salary = manager.calculateSalary()

print(f"Salary : {salary}")