class employee:
    def __init__(self,Name,id,salary):
              self.Name = Name
              self.id = id
              self.salary = salary
    def showDetails(self):
        print("Name:",self.Name)
        print("ID:",self.id)
        print("Salary:",self.salary)
emp1 = employee("John Doe", 1, 50000)
emp2 = employee("Jane Smith", 2, 60000)
emp2.showDetails()