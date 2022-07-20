from kalkulator_03 import suma, odejmowanie

with open("data.txt") as f:
    data = f.read().splitlines()

    for d in data:
        a, b = d.split()
        a, b = int(a), int(b)
        print(suma(a, b))
        print(odejmowanie(a, b))
