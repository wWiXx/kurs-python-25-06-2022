from mathematica.algebra.matrices import add_matrices, sub_matrices


def test_add_matrices():
    m1 = [
        [1, 3],
        [5, 7],
    ]

    m2 = [
        [2, 4],
        [6, 8],
    ]
    m3 = [
        [3, 7],
        [11, 15]
    ]
    assert add_matrices(m1, m2) == m3

def test_sub_matrices():
    m1 = [
        [1, 3],
        [5, 7],
    ]

    m2 = [
        [2, 4],
        [6, 8],
    ]
    m3 = [
        [-1, -1],
        [-1, -1]
    ]
    assert sub_matrices(m1, m2) == m3
