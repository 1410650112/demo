class Ellipse():
    pi = 3.14159
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b         
    @property
    def area(self):
        return self.a * self.b * self.pi

class Circle(Ellipse):
    def __init__(self, r=0):
        super().__init__(r, r)

class Rectangle():
    def __init__(self, width=0, length=0):
        self.width=width
        self.length=length        
    @property
    def area(self):
        return self.width * self.length

class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side, side)

shapes = [Ellipse(10,20), Square(15), Circle(5), Rectangle(20,15)]
areas = [object.area for object in shapes]
total_area = sum(areas)
print('areas: ', areas,'total_area: ', total_area)