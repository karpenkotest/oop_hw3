class Employee: 

    def __init__(self, name: str, salary_per_day: int):
        self.name = name
        self.salary_per_day = salary_per_day

    def work(self) -> str:
        return 'I come to the office'

    def dict_my(self) -> dict:
        dict_my1 = {self.name: self.salary_per_day}
        return dict_my1

    def check_salary(self, days: int):
        salary = self.salary_per_day * days
        return salary


class Recruiter(Employee):
    def __init__(self, name, salary_per_day):
        return super().__init__(name, salary_per_day)
        
    def __str__(self) -> str:
        return f'Recruiter: {self.name}'
        
    def work(self) -> str:
        return super().work() + f' and start to hiring'


class Developer(Employee):
    def __init__(self, name, salary_per_day, tech_stack):
        super().__init__(name, salary_per_day)
        self.tech_stack = tech_stack
        
    def work(self) -> str:
        return super().work() + f' and start to coding'
        
    def __str__(self) -> str:
        tech_stack_humanized = ', '.join(self.tech_stack)
        return f'Developer: {self.name}, {self.salary_per_day}, {tech_stack_humanized}'
        
    def compare_tech_stack(self, other):
        if len(self.tech_stack) > len(other.tech_stack):
            print(f'{self.name} has more skills')
        if len(self.tech_stack) < len(other.tech_stack):
            print(f'{other.name} has more skills')
        if len(self.tech_stack) == len(other.tech_stack):
            print(f'Developers have the same number of  skills')
            
    def adding_devs(self, other):
        name = self.name + ' ' + other.name
        added_skills = set(self.tech_stack + other.tech_stack)
        bigger_salary = max(self.salary_per_day, other.salary_per_day)
        return Developer(name, bigger_salary, added_skills)


developer1 = Developer('Yulia', 200, ['GO', 'C', 'Python'])
developer2 = Developer('Nika', 180, ['Java', 'C'])
recruiter1 = Recruiter('Roman', 50)

dict_common = Developer.dict_my(developer1) | Recruiter.dict_my(recruiter1) | Developer.dict_my(developer2) 

print(developer1.work())
print(developer2.work())
print(recruiter1.work())
print(developer1)
print(developer2)
print(recruiter1)

employee_with_max_salary = max(dict_common, key=dict_common.get)
max_salary = max(dict_common.values()) 

print(f'The biggest salary in this company is {max_salary}')
print(f'{employee_with_max_salary} has the biggest salary.')

days = 10
print(f'Salary of {developer1.name} for {days} days is {developer1.check_salary(days)}')
print(f'Salary of {developer2.name} for {days} days is {developer2.check_salary(days)}')
print(f'Salary of {recruiter1.name} for {days} days is {recruiter1.check_salary(days)}')

developer1.compare_tech_stack(developer2)
developer3 = developer1.adding_devs(developer2)
print(developer3)
