from mathematica.geometry.figures import square_area, triangle_area


def test_square_area():
    assert square_area(2) == 4


def test_triangle_area():
    assert triangle_area(6, 5) == 15.00
