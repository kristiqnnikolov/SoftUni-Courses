# Create a class Circle. In the __init__ method, the circle should only receive one parameter - its diameter.
# Create a class attribute called __pi that is equal to 3.14. The class should also have the following methods:
# •	calculate_circumference() - returns the circumference of the circle
# •	calculate_area() - returns the area of the circle
# •	calculate_area_of_sector(angle) - gives the central angle in degrees, returns the area that fills the sector
# Notes: Search the formulas on the internet. Name your methods and variables exactly as in the description!
# Submit only the class. Test your class before submitting it!
class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        return self.radius * Circle.__pi * 2

    def calculate_area(self):
        return self.radius ** 2 * Circle.__pi

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * Circle.__pi * self.radius ** 2


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
