"""
OOP: Object Oriented Programming
    - class/object
    - attributes/methods
    - encapsulation/abstraction
    - inheritence
    - overriding/polymorphism

"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Shape = super class / abstract class
    """
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass
    def toString(self): pass


class Square(Shape):
    "square class"

    def __init__(self, edge):
        self.__edge = edge

    def area(self):
        result = self.__edge ** 2
        print("Square Area: ", result)

    def perimeter(self):
        result = self.__edge * 4
        print("Square Perimeter: ", result)

    def toString(self):
        print("Square edge: ", self.__edge)


class Circle(Shape):
    "circle class"
    PI = 3.14

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        result = self.__radius ** 2 * self.PI
        print("Circle Area: ", result)

    def perimeter(self):
        result = self.__radius * 2 * self.PI
        print("Circle Perimeter: ", result)

    def toString(self):
        print("Circle radius: ", self.__radius)


c = Circle(5)
c.area()
c.perimeter()
c.toString()


s = Square(5)
s.area()
s.perimeter()
s.toString()