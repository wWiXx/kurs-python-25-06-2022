from typing import Callable, List, Union

lista = [1, 2, 3, 4, 5, 6, 7, 8]


def cut(lista, start, stop):
    result = []
    can_add_element = False

    for element in lista:
        if start(element) and can_add_element == False:
            can_add_element = True
        if can_add_element:
            result.append(element)
            if stop(element):
                break

    return result


print(cut([1, 2, 3, 4, 5, 6, 7, 8], start=lambda x: x > 3, stop=lambda x: x < 7))

# def test_cut():
#     assert cut(
#         [1, 2, 3, 4, 5, 6, 7, 8], start=lambda x: x > 3, stop=lambda x: x == 7
#     ) == [
#         4,
#         5,
#         6,
#         7,
#     ]
#
#
# def test_cut2():
#     assert cut(
#         [1, 2, 3, 4, 5, 6, 7, 8], start=lambda x: x > 3, stop=lambda x: x < 7
#     ) == [4]
#
#
# def test_cut3():
#     assert cut(
#         [1, 2, 3, 4, 8, 8, 8, 8, 6], start=lambda x: x > 3, stop=lambda x: x < 4
#     ) == [4, 8, 8, 8, 8, 6]
#
#
# def test_cut4():
#     assert cut(
#         ["x", "y", "z", "zz"], start=lambda x: x == "y", stop=lambda x: x == "zz"
#     ) == ["y", "z", "zz"]
#
#

