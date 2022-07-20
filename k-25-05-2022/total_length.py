import timeit
from time import process_time

lista = [4, 5]
tupla = (6, 7)
slownik = {"1": "jeden", "2": "dwa", "da": "dasa"}
numbers = [4, 6, 8, 9]
generator_liczb = [n for n in numbers if n % 2 == 0]


def total_length(*args, ):
    length = 0
    if not len(args):
        for _ in args:
            length += 1
    for a in args:
        length += len(a)

    return length


print(total_length(lista, tupla, "ada", "adam", slownik, numbers, generator_liczb))

"""
assert total_length([4, 5], (6, 7)) == 4
assert total_length('hello', {'red': 50, 'purple': 100}) == 7
"""

#timeit((total_length(list(range(1000)), list(range(1000)))))
