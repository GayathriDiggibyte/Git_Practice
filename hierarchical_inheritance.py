class Shape:
    def __init__(self,size):
        self.size=size
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def __init__(self,size):
        super().__init__(size)
    def draw(self):
        print("Drawing a circle with radius",self.size)

class Square(Shape):
    def __init__(self,size):
        super().__init__(size)
    def draw(self):
        print("Drawing a square with radius ",self.size)

circle = Circle(4)
square = Square(4)

circle.draw()
square.draw()

