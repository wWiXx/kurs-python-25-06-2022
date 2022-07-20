import math
from abc import ABC, abstractmethod


class Employee:
    def __init__(self, name, rate_per_hour):
        self.worked_time = 0
        self.name = name
        self.rate_per_hour = rate_per_hour

    def register_time(self, worked_time):
        self.worked_time = worked_time

    def pay_salary(self):
        if self.worked_time > 8:
            salary = 8 * self.rate_per_hour + ((self.worked_time - 8) * self.rate_per_hour) * 2
        else:
            salary = self.worked_time * self.rate_per_hour
        self.worked_time = 0
        return salary

class IBonus(ABC):
    @abstractmethod
    def calculate(self): pass

class Bonus:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.__class__(self.value + other.value)


class ValueBonus(Bonus):
    order = 2

    def calculate(self, salary: int):
        return salary + self.value

    def __repr__(self):
        return f"{self.__class__} v: {self.value}"


class PercentBonus(Bonus):
    order = 1

    def calculate(self, salary: int):
        return salary + (salary * self.value / 100)


class PremiumEmployee(Employee):
    def __init__(self, name, surname, rate_per_hour):
        super().__init__(name, rate_per_hour)
        self.bonus = None
        self.surname = surname
        self.bonuses = {}

    def pay_salary(self):
        salary = super().pay_salary()

        for bonus in sorted(self.bonuses.values(), key=lambda x: x.order):
            salary = bonus.calculate(salary)
        return salary

    def give_bonus(self, bonus: Bonus):
        if bonus.__class__ in self.bonuses:
            self.bonuses[bonus.__class__] += bonus
        else:
            self.bonuses[bonus.__class__] = bonus



robert = Employee("Robert", 200)
robert.register_time(10)
print(robert.pay_salary())
print(robert.pay_salary())

max_c = PremiumEmployee("max", "czyz", 200)
print(max_c.name)
print(max_c.rate_per_hour)
print(max_c.surname)
max_c.register_time(10)

b1 = ValueBonus(200)
max_c.give_bonus(b1)
print(max_c.pay_salary())
b2 = PercentBonus(10)
e = PremiumEmployee("MaxC", "czyz", 100)
e.register_time(5)
e.give_bonus(b2)


def test_percent_bonus():
    b1 = ValueBonus(200)
    max_c.give_bonus(b1)

    b2 = PercentBonus(10)
    e = PremiumEmployee("MaxC", "czyz", 100)
    e.register_time(5)
    e.give_bonus(b2)

    b = PercentBonus(10)
    assert b.calculate(100) == 110


def test_add_bonuses_together():
    b1 = ValueBonus(100)
    b2 = ValueBonus(200)

    b3 = b1 + b2
    assert b3.value == 300
    assert isinstance(b3, ValueBonus)

    b1 = PercentBonus(10)
    b2 = PercentBonus(20)

    b3 = b1 + b2
    assert b3.value == 30
    assert isinstance(b3, PercentBonus)
