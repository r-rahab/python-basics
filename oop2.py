#
class Circle:
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        return 22/7 * self.radius**2

    def get_perimeter(self):
        return 22/7 * self.radius* 2

    def print_details(self):
        print("Radius", self.radius)
        print("Perimeter", self.get_perimeter())
        print("Area", self.get_area())

c1 = Circle(14)
c2 = Circle(19.77)

c1.print_details()
print(c1.get_area())