


# from ast import Return
# from optparse import Option


# class Employee:
#     def __init__(self, name, age, salary, employee_years):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.employee_years = employee_years

#         def get_annual_salary(self, salary):
#             return self.salary *12 #!!!!


#    #Employee class here


# class Manager(Employee):
#     bonus_percentage = 0.15
    
#     def __init__(self, name, age, salary, employee_years):
#         super().__init__(name, age, salary, employee_years)



#     def get_bonus(self, salary, bonus_percentage):
#         return bonus_percentage * salary #!!!!

    
    
    
#     #Manager class here

# def __str__(self): 
#         return (self., self.) #Here!!!!!!!!!!!


# Employee = [ 'name' , 'age' , 'salary' , 'employment_years' ]
# Manager = [ 'name' , 'age' , 'salary' , 'employment_years' , 'bonus_percentage' ]

# Option=[ '1. Show Employees' , '2. Show Mangr' , '3. Add An Employee' , '4. Add A manger' , '5. Exit' ]

# print(*Option, sep = "\n")

# print ('what would you like to do?')
#     user_input[]
#     if user_input == 1 :
#         print(*Employee, sep = "\n")
#         elif user_input == 2 :
#             print(*Manager, sep = "\n")
#             elif user_input == 3 :
#                 def add_emploee(self,name, age, salary, employee_years):
#                     self.name += name
#                     self.age += age
#                     self.salary += salary
#                     self.employee_years += employee_years
#                     print (f"this is the new employee{self.name}")
#                     elif user_input == 4 :
#                          def add_manger(self,name, age, salary, employee_years , bonus_percentage)
#                          self.name += name 
#                          self.age += age 
#                          self.salary += salary
#                          self.employee_years += employee_years 
#                          self.bonus_percentage += bonus_percentage 
#                          print (f"this is the new employee{self.name}")
#                          else user_input == 5
#                          Return 0 


            







# #def main():
# 	# main code here

# #if __name__ == '__main__':
# 	#main()


class Employee():
    def __init__(self,name,age,salary,employment_years):
        self.name=name
        self.age=age
        self.salary=salary
        self.employment_years=employment_years
    def get_annual_salary(self):
        return self.salary12
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years:{self.employment_years}'
class Manager(Employee):
    def ___init__(self,name,age,salary,employment_years,bonus_percentage):
        super().__init__(name,age,salary,employment_years)
        self.bonus_percentage=bonus_percentage
    def get_bonus(self):
        return self.bonus_percentageself.salary
    def str(self):
        return f'{super().str()}, Bonus: {self.get_bonus()}'
def main():
    employees=[]
    managers=[]
    while True:
        print(" Options:")
        print("     1. Show Employees")
        print("     2. Show Managers")
        print("     3. Add An Employees")
        print("     4. Add A Manager")
        print("     5. Exit")
        print()
        option=eval(input (" What would you like to do? "))
        print(" -----------------")
        if option==1:
            print(" Employees")
            print()
            for emp in employees:
                print(emp)
            print(" -----------------")
        elif option==2:
            print(" Managers")
            print()
            for mang in managers:
                print(mang)
            print()
            print(" -----------------")
        elif option==3:
            name=input(" Name: ")
            age=eval(input(" Age: "))
            salary=eval(input(" Salary: "))
            employement_years=eval(input(" Employement years: "))
            emp=Employee(name,age,salary,employement_years)
            employees.append(emp)
            print(f' name: {emp.name}, age: {emp.age}, salary: {emp.salary} and employement years: {emp.employment_years} was added')
            print()
        elif option==4:
            name=input(" Name: ")
            age=eval(input(" Age: "))
            salary=eval(input(" Salary: "))
            employement_years=eval(input(" Employement years: "))
            bonus=eval(input(" Bonus Percentage: "))
            mang=Manager(name,age,salary,employement_years,bonus)
            managers.append(mang)
            print(" Manager added successfully")
            print(f' {mang}')
            print()
        elif option==5:
            print(" Thank You ... exit")
            break
        else:
            print(" Invalid option")
            print()

if __name__=='__main__':
    main()