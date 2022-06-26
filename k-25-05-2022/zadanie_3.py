"""
y = [
    [x * i for x in range(1,11)]
    for i in range (1,11)
    ]

print(y)

"""
liczby = [1, 11, 2, 15, 4, 8, 11, 21, 34, 3]

liczby_pierwsze = []

for n in liczby:
    if n <= 1:
        continue
    #    elif n == 2: liczby_pierwsze.append(n)
    else:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            liczby_pierwsze.append(n)
print(liczby_pierwsze)
