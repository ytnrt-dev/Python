import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def volume(self):
        pass

    def display(self):
        print(f"  Volume = {self.volume()}")

class Cube(Shape):
    def __init__(self, s):        self.s = s
    def volume(self):             return self.s ** 3

class Sphere(Shape):
    def __init__(self, r):        self.r = r
    def volume(self):             return (4/3) * math.pi * self.r ** 3

class Cylinder(Shape):
    def __init__(self, r, h):     self.r, self.h = r, h
    def volume(self):             return math.pi * self.r ** 2 * self.h

class Cone(Shape):
    def __init__(self, r, h):     self.r, self.h = r, h
    def volume(self):             return (1/3) * math.pi * self.r ** 2 * self.h

class Box(Shape):
    def __init__(self, l, w, h):  self.l, self.w, self.h = l, w, h
    def volume(self):             return self.l * self.w * self.h


def ask(prompt):
    while True:
        try: return float(input(f"  {prompt}: "))
        except ValueError: print("  Enter a number!")


def main():
    while True:
        print("\n==== VOLUME CALCULATOR ====")
        print("1. Cube\n2. Sphere\n3. Cylinder\n4. Cone\n5. Box\n0. Exit")

        match input("\nChoose: "):
            case "1": Cube(ask("Side")).display()
            case "2": Sphere(ask("Radius")).display()
            case "3": Cylinder(ask("Radius"), ask("Height")).display()
            case "4": Cone(ask("Radius"), ask("Height")).display()
            case "5": Box(ask("Length"), ask("Width"), ask("Height")).display()
            case "0": print("Goodbye!"); break
            case  _:  print("  Invalid choice.")

if __name__ == "__main__":
    main()