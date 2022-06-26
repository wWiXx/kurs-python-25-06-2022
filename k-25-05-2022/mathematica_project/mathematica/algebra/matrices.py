m1 = [
    [1, 3],
    [5, 7],
]

m2 = [
    [2, 4],
    [6, 8],
]
# print(m1[0][0]) - 2




def add_matrices(m1, m2):
    m3 = []
    for i, j in zip(m1, m2):
        m4 = []
        for m, n in zip(i, j):
            m4.append(m+n)
        m3.append(m4)
    return m3

def sub_matrices(m1, m2):
    m3 = []
    for i, j in zip(m1, m2):
        m4 = []
        for m, n in zip(i,j):
            m4.append(m-n)
        m3.append(m4)
    return m3


print(add_matrices(m1, m2))
print(sub_matrices(m1, m2))
