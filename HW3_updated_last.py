class Employee: 

  def __init__(self, name, salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

  def work(self):
      return f'I come to the office'

  def dict_my(self) -> dict:
      dict_my1 = {self.name : self.salary_per_day}
      return dict_my1

  def salary(self,days):
      salary = self.salary_per_day*days
      return salary


class Recruiter(Employee):
    def __init__(self, name, salary_per_day):
        return super().__init__(name, salary_per_day)
        
    def __str__(self) -> str:
        return f'Recruiter: {self.name}'
        
    def work(self):
        return super().work() + f' and start to hiring'


class Developer(Employee):
    def __init__(self, name, salary_per_day,tech_stack):
        super().__init__(name, salary_per_day)
        self.tech_stack = tech_stack
        
    def work(self):
        return super().work() + f' and start to coding'
        
    def __str__(self) -> str:
        tech_stack_humanized= ', '.join(self.tech_stack)
        return f'Developer: {self.name}, {self.salary_per_day}, {tech_stack_humanized}'
        
    def compare_tech_stack(self, other):
        if len(self.tech_stack) > len(other.tech_stack):
            print(f'{self.name} has more skills')
        if len(self.tech_stack) < len(other.tech_stack):
           print(f'{other.name} has more skills')
        if len(self.tech_stack) == len(other.tech_stack):
           print(f'Developers have the same number of  skills')
            
    def adding_devs(self, other):
        name = self.name + ' ' +  other.name
        added_skills = set(self.tech_stack+other.tech_stack)
        bigger_salary = max(self.salary_per_day,other.salary_per_day)
        return Developer(name,bigger_salary,added_skills)


#creation of objects 
developer1 = Developer('Yuliia', 200, [ 'GO','C','Python'])
developer2 = Developer('Nika', 180, ['Java','C'])
recruiter1 = Recruiter('Roman', 50)

#creation of a dictionary that contains all employees
dict_common = Developer.dict_my(developer1) | Recruiter.dict_my(recruiter1) | Developer.dict_my(developer2) 


print(developer1.work())
print(developer2.work())
print(recruiter1.work())
print(developer1.__str__())
print(developer2.__str__())
print(recruiter1.__str__())


employee_with_max_salary = max(dict_common, key = dict_common.get)
max_salary = max(dict_common.values()) 

print(f'The biggest salary in this company is {max_salary}')
print(f'{employee_with_max_salary} has the biggest salary  in this company. If you develop your skills your salary also will rise! Good luck.')

days = 10
print(f'Salary of {developer1.name} for {days} days is {developer1.salary(days)}')
print(f'Salary of {developer2.name} for {days} days is {developer2.salary(days)}')

print(f'Salary of {recruiter1.name} for {days} days is {recruiter1.salary(days)}')

developer1.compare_tech_stack(developer2)

developer3 =developer1.adding_devs(developer2)
print(developer3)
