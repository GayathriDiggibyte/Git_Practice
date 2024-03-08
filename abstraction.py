from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")

    def area(self):
        return 3.14 * self.radius * self.radius


my_circle = Circle(radius=5)


my_circle.draw()
print("Area:", my_circle.area())
