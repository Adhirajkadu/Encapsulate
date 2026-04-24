class Circle():



    def __init__(self):
        self.radius = (float(input("Enter a radius of a Circle :")))



    def perimeter(self):
        return 2 * 3.14 * self.radius
    


    def area(self):
        return 3.14 * self.radius ** 2
    


Circle = Circle ()



print(f"The Circumference of the circle is {Circle.perimeter()}")
print(f"The Area of the circle is {Circle.area()}")