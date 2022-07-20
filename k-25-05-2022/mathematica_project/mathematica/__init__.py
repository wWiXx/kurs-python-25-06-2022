"""
def format_number(number):
    number_list = [x for x in str(number)]
    print(number_list)
    if number >= 1000 and number < 10000:
        number_list.insert(1, ",")
        print(number_list)
        print("".join(number_list))
    elif number >= 10000 and number < 100000:
        number_list.insert(2,",")
        print(number_list)
        print("".join(number_list))
    elif number >= 100000 and number < 1000000:
        number_list.insert(3, ",")
        print(number_list)
        print("".join(number_list))
    elif number >= 1000000 and number < 10000000:
        number_list.insert(1, ",")
        number_list.insert(5, ",")
        print(number_list)
        print("".join(number_list))



format_number(1000000)
"""