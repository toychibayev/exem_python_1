class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        print(f"Yangi Xodim yaratildi, ism: {self.name}, maosh: {self.salary}")
    def get_details(self) -> str:
        return f"Xodim: {self.name}, Maosh: {self.salary}"
    def calculate_bonus(self) -> float:
        return 0.0

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department
        print(f"Yangi Manager yaratildi, ism: {self.name}, maosh: {self.salary}, bo'lim: {self.department}")
    def get_details(self) -> str:
        return f"Manager: {self.name}, Department: {self.department}, Salary: {self.salary}"
    def calculate_bonus(self) -> float:
        bonus = self.salary * 0.10
        print(f"Manager uchun bonus: {bonus} so'm 10%")
        return bonus

class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language
        print(f"Yangi Developer yaratildi, ism: {self.name}, maosh: {self.salary}, dasturlash tili: {self.programming_language}")
    def get_details(self) -> str:
        return f"Developer: {self.name}, Programming Language: {self.programming_language}, Salary: {self.salary}"
    def calculate_bonus(self) -> float:
        bonus = self.salary * 0.05
        print(f"Developer uchun bonus: {bonus} so'm 5%")
        return bonus

manager = Manager(name="Alice", salary=120000, department="Sales")
developer = Developer(name="Bob", salary=100000, programming_language="Python")
print(manager.get_details())
print(developer.get_details())
manager.calculate_bonus()
developer.calculate_bonus()
