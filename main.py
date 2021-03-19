# ======================= Calculator ======================= #
# ======================= Calculator ======================= #

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        print(self.x + self.y)

    def subtract(self):
        print(self.x - self.y)

    def multiply(self):
        print(self.x * self.y)

    def divide(self):
        print(self.x / self.y)


# a = Calculator(10, 5)
# a.add()
# a.subtract()
# a.multiply()
# a.divide()


# ======================= Rectangle ======================= #
# ======================= Rectangle ======================= #


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        print("area - " + f'{self.width * self.length}')

    def perimeter(self):
        print("perimeter - " + f'{2 * (self.width + self.length)}')

    def print_info(self):
        print("width - " + f'{self.width}')
        print("length - " + f'{self.length}')
        print("area - " + f'{self.width * self.length}')
        print("perimeter - " + f'{2 * (self.width + self.length)}')


# b = Rectangle(5, 10)
# b.print_info()

