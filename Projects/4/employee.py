# Name 1: Ryan Schlimme
# EID 1: rjs4499

# Name 2: Elliot Ylagan
# EID 2:epy82

'''
Calculates salary for many different types of employees using
inheritance class structure.
'''


class Employee:
    '''
    Implements the parent Employee class.
    Attributes: Name, ID, Salary
    '''

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.identifier = kwargs.get("id") if "id" in kwargs else None
        self.identifier = (kwargs.get("identifier") if "identifier" in kwargs
                           else self.identifier)
        self.salary = kwargs.get("salary") if "salary" in kwargs else None

    def formatting_method(self):
        '''
        Necessary to have enough public methods without changing class 
        structure
        '''
        return None

    def __str__(self):
        return f"{self.__class__.__name__} \n{self.name}, {self.identifier}, {self.salary}"

############################################################
############################################################
############################################################


class PermanentEmployee(Employee):
    '''
    Implements the Permanent Employee class.
    Attributes: Name, ID, Salary, benefits
    Method: cal_salary
    '''

    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.benefits = kwargs.get("benefits")
        self.new_salary = 0

    def cal_salary(self):
        '''
        Calculates salary. If benefits = health_insurance,
        then salary = base_salary * 0.9. If benefits = retirement,
        salary = base_salary * 0.8. If benefits is both, salary =
        base_salary * 0.7.
        '''
        if "health_insurance" in self.benefits and "retirement" in self.benefits:
            return self.salary * .7
        elif "health_insurance" in self.benefits:
            return self.salary * 0.9
        elif "retirement" in self.benefits:
            return self.salary * 0.8
        else: 
            return self.salary

    def __str__(self):
        return f"{Employee.__str__(self)}, {self.benefits}"


############################################################
############################################################
############################################################
class Manager(Employee):
    '''
    Implements the manager Employee class.
    Attributes: Name, ID, Salary, Bonus
    Method: cal_salary
    '''

    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.bonus = kwargs.get("bonus")

    def cal_salary(self):
        '''
        Calculates salary as base + bonus
        '''
        return float(self.salary + self.bonus)

    def __str__(self):
        return f"{Employee.__str__(self)}, {self.bonus}"

############################################################
############################################################
############################################################


class TemporaryEmployee(Employee):
    '''
    Implements the temporary Employee class.
    Attributes: Name, ID, Salary, Hours
    Method: cal_salary
    '''

    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.hours = kwargs.get("hours")

    def cal_salary(self):
        '''
        Calculates salary as base times hours
        '''
        return float(self.salary * self.hours)

    def __str__(self):
        return f"{Employee.__str__(self)}, {self.salary}"

############################################################
############################################################
############################################################


class Consultant(TemporaryEmployee):
    '''
    Implements the consultant Employee class.
    Attributes: Name, ID, Salary, Travel
    Method: cal_salary
    '''

    def __init__(self, **kwargs):
        TemporaryEmployee.__init__(self, **kwargs)
        self.trips = kwargs.get("travel")

    def cal_salary(self):
        '''
        Calculates salary as base*hourts + trips*1000
        '''
        return float(self.salary * self.hours + self.trips * 1000)

    def __str__(self):
        return f"{TemporaryEmployee.__str__(self)}, {self.trips}"

############################################################
############################################################
############################################################


class ConsultantManager(Consultant, Manager):
    '''
    Implements the consultant manager Employee class.
    Attributes: Name, ID, Salary, Bonus, Travel
    Method: cal_salary
    '''

    def __init__(self,  **kwargs):
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)

    def cal_salary(self):
        '''
        Calculates salary as base * hours + trips * 1000 + bonus
        '''
        return float(self.salary * self.hours + self.trips * 1000 + self.bonus)

    def __str__(self):
        return f"{Consultant.__str__(self)}, {Manager.__str__(self)}"

############################################################
############################################################
############################################################


def main():
    ''' ##### DRIVER CODE #####
        ##### Do not change. '''

    # create employees
    chris = Employee(name="Chris", id="UT1")
    emma = PermanentEmployee(name="Emma", id="UT2",
                             salary=100000, benefits=["health_insurance"])
    sam = TemporaryEmployee(name="Sam", id="UT3", salary=100,  hours=40)
    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    charlotte = Manager(name="Charlotte", id="UT5",
                        salary=1000000, bonus=100000)
    matt = ConsultantManager(name="Matt", id="UT6",
                             salary=1000, hours=40, travel=4, bonus=10000)

    # print employees
    print(chris, "\n")
    print(emma, "\n")
    print(sam, "\n")
    print(john, "\n")
    print(charlotte, "\n")
    print(matt, "\n")

    # calculate and print salaries
    print("Check Salaries")
    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]
    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]
    print("Emma's Salary is:", emma.cal_salary())
    print("Sam's Salary is:", sam.cal_salary())
    print("John's Salary is:", john.cal_salary())
    print("Charlotte's Salary is:", charlotte.cal_salary())
    print("Matt's Salary is:",  matt.cal_salary())


if __name__ == "__main__":
    main()
