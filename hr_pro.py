


from ast import Return
from optparse import Option


class Employee:
    def __init__(self, name, age, salary, employee_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employee_years = employee_years

        def get_annual_salary(self, salary):
            return self.salary *12 #!!!!


   #Employee class here


class Manager(Employee):
    bonus_percentage = 0.15
    
    def __init__(self, name, age, salary, employee_years):
        super().__init__(name, age, salary, employee_years)



    def get_bonus(self, salary, bonus_percentage):
        return bonus_percentage * salary #!!!!

    
    
    
    #Manager class here

def __str__(self): 
        return (self., self.) #Here!!!!!!!!!!!


Employee = [ 'name' , 'age' , 'salary' , 'employment_years' ]
Manager = [ 'name' , 'age' , 'salary' , 'employment_years' , 'bonus_percentage' ]

Option=[ '1. Show Employees' , '2. Show Mangr' , '3. Add An Employee' , '4. Add A manger' , '5. Exit' ]

print(*Option, sep = "\n")

print ('what would you like to do?')
    user_input[]
    if user_input == 1 :
        print(*Employee, sep = "\n")
        elif user_input == 2 :
            print(*Manager, sep = "\n")
            elif user_input == 3 :
                def add_emploee(self,name, age, salary, employee_years):
                    self.name += name
                    self.age += age
                    self.salary += salary
                    self.employee_years += employee_years
                    print (f"this is the new employee{self.name}")
                    elif user_input == 4 :
                         def add_manger(self,name, age, salary, employee_years , bonus_percentage)
                         self.name += name 
                         self.age += age 
                         self.salary += salary
                         self.employee_years += employee_years 
                         self.bonus_percentage += bonus_percentage 
                         print (f"this is the new employee{self.name}")
                         else user_input == 5
                         Return 0 


            







#def main():
	# main code here

#if __name__ == '__main__':
	#main()
