from pracownik_klasa import Employee, PremiumEmployee, ValueBonus, PercentBonus, max_c


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