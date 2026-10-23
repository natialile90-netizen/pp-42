class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >0:
            self.__salary = new_salary
        else: 
            print ("salary must be possitive!!!")

    @salary.deleter
    def salary(self):
        del self.__salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        return f"name : {self.name}, department : {self.department} , salary : {self.salary}"

manager = Manager ("Natia", 2000, "Teacher")
print (manager.get_info())

manager.salary = 2500
print (manager.get_info())

manager.salary = -200

del manager.salary

print (manager.name)
print (manager.department)