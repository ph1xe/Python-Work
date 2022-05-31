class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def getPerimeter(self):
        perimeter = (2 * self.length) + (2 * self.width)
        return perimeter
    def getArea(self):
        area = self.length * self.width
        return area
    def __str__(self):
        s = ""
        w = "* " * self.width + "\n"
        s += w
        for i in range(self.length -2):
            s += "* "
            s += "  " * (self.width -2)
            s +="* \n"
        s += w
        return s

class Square(Rectangle):
    def __init__(self, length):
        Rectangle.__init__(self, length, length)

def display(r):
    print("Perimeter", r.getPerimeter())
    print("Area:", r.getArea())
    print(r)

def main():
    print("Rectangle Calculator")
    print()

    again = "y"
    while again.lower() == "y":
        shape = input("Rectangle or square? (r/s): ")
        if shape == "r":
            length = int(input("Enter length: "))
            width = int(input("Enter width: "))
            rectangle = Rectangle(length, width)
            display(rectangle)
        elif shape == "s":
            length = int(input("Enter length: "))
            square = Square(length)
            display(square)
        else:
            print("Invalid entry. Try again.")
            continue
        again = input("Continue? (y/n):").lower()
        print()
    print("Bye!")

if __name__ == "__main__":
    main()