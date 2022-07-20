import math


class Circle:
    def __init__(self, radius=None):
        self.diameter = 2
        self.radius = 1
        self.area = math.pi

        if radius:
            self.radius = radius
            # self.diameter = radius * 2
            # self.area = math.pi * (radius ** 2)

    def __repr__(self):
        return f"Promień koła: {self.radius}"

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius < 0: raise ValueError("Promien ujemny?")
        self.__radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return self.radius * math.pi

    @area.setter
    def area(self, area):
        self.__radius = area / math.pi


c = Circle(1)
# c.diameter = 4
c.area = 5
print(c.radius)

################ POPRAW
