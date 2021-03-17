
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = round(self.radius ** 2 * Circle.pi, 2)
        return area

    def get_circumference(self):
        circumference = round(2 * self.radius * Circle.pi, 2)
        return circumference


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())



