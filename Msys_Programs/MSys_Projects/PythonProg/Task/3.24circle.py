class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        area = 3.14*self.radius**2
        return f"Area of given circle is: {area}"
    
    def diameter(self):
        diameter = self.radius*2
        return f"Diameter of given circle is: {diameter}"
    
a = Circle(10)
print(a.diameter())
print(a.area())