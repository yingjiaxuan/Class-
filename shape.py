import math
from abc import abstractmethod
import os
import sys
import re

class Shape(object):
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getVolume(self):
        pass


class Point(Shape):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._name = "Point"

    def setName(self, name):
        self._name = self._name + ": " + str(name)

    def getName(self):
        return self._name

    def __str__(self):
        return "[" + str(self._x) + "," + str(self._y) + "]"

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getArea(self):
        return 0

    def getVolume(self):
        return 0

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y


class Circle(Point):
    def __init__ (self, x, y, r):
        super().__init__(x, y)
        self._r = 0
        self._name = "Circle"
        self.setRadius(r)

    def getArea(self):
        return math.pi*self._r*self._r

    def __str__(self):
        return "C = " + super().__str__() + "; R = " + str(self._r)

    def getRadius(self):  # get/set radius methods
        return self._r

    def setRadius(self, r):
        if r > 0:
            self._r = r


class Cylinder(Circle):
    def __init__(self, x, y, r, h):
        super().__init__(x, y, r)
        self._h = 0
        self.setHeight(h)
        self._name = "Cylinder"

    def getArea(self):
        return 2.*super().getArea()+2.*math.pi*self.getRadius()*self._h

    def getVolume(self):
        return super().getArea()*self._h

    def __str__(self):
        return super().__str__() + "; H = " + str(self._h)

    def getHeight(self):  # get/set height methods
        return self._h

    def setHeight(self, h):
        if h > 0:
            self._h = h


class Sphere(Circle):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
        self._name = "Sphere"

    def getArea(self):
        return math.pow(math.pi * self._r, 2) * 4

    def getVolume(self):
        return math.pow(math.pi * self._r, 3) * 4 / 3

    def __str__(self):
        return super().__str__()


class Rectangle(Point):
    def __init__(self, x, y, length, height):
        super().__init__(x, y)
        self._len = length
        self._h = height
        self._name = "Rectangle"

    def getArea(self):
        return self._len * self._h

    def __str__(self):
        return "C = " + super().__str__() + "; len = " + str(self._len) + "; height = " + str(self._h)

    def getLength(self):
        return self._len

    def getHeight(self):
        return self._h

    def setLength(self, length):
        if length > 0:
            self._len = length

    def setHeight(self, height):
        if height > 0:
            self._h = height


class Square(Point):
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self._len = length
        self._name = "Square"

    def getArea(self):
        return math.pow(self._len, 2)

    def __str__(self):
        return "C = " + super().__str__() + "; len = " + str(self._len)

    def getLength(self):
        return self._len

    def setLength(self, length):
        if length > 0:
            self._len = length


class Cube(Square):
    def __init__(self, x, y, length):
        super().__init__(x, y, length)
        self._name = "Cube"

    def getArea(self):
        return math.pow(self._len, 2) * 6

    def getVolume(self):
        return math.pow(self._len, 3)

    def __str__(self):
        return "C = " + super().__str__() + "; len = " + str(self._len)




def shape_choice():
    if len(shape_list) == 0:
        return
    shape_num = get_input("Please Select One Shape to Operate:", (1, len(shape_list)))
    shape = shape_list[shape_num - 1]
    shape_name = shape_list[shape_num - 1].getName()
    shape_species = str(shape_name[0:shape_name.rfind(':')])
    if shape_species == "Point":
        print("Please Select One Choice to Operate the Point:")
        input_data = get_input("1.setName     2.getName       3.getX\n4.getY    5.getArea    6.getVolume\n7.setX      "
                               "8.setY \n 9.Back to higher menu"
                               , (1, 9))
        if input_data == 1:
            name = input("Please input Name")
            shape.setName(name)
        elif input_data == 2:
            print(shape.getName())
        elif input_data == 3:
            print(shape.getX())
        elif input_data == 4:
            print(shape.getY())
        elif input_data == 5:
            print(shape.getArea())
        elif input_data == 6:
            print(shape.getVolume())
        elif input_data == 7:
            x = get_input("Please type in x: ", (-100000, 100000), True)
            shape.setX(x)
        elif input_data == 8:
            y = get_input("Please type in y: ", (-100000, 100000), True)
            shape.setY(y)
        elif input_data == 9:
            view_shape_menu()
            return
        shape_choice()
    elif shape_species == "Circle":
        print("Please Select One Choice to Operate the Circle:")
        input_data = get_input("1.setName     2.getName       3.getX\n4.getY    5.getArea    6.getVolume\n7.setX      "
                               "8.setY     9.getRadius\n10.setRadius     11.Back to higher menu"
                               , (1, 11))
        if input_data == 1:
            name = input("Please input Name")
            shape.setName(name)
        elif input_data == 2:
            print(shape.getName())
        elif input_data == 3:
            print(shape.getX())
        elif input_data == 4:
            print(shape.getY())
        elif input_data == 5:
            print(shape.getArea())
        elif input_data == 6:
            print(shape.getVolume())
        elif input_data == 7:
            x = get_input("Please type in x: ", (-100000, 100000), True)
            shape.setX(x)
        elif input_data == 8:
            y = get_input("Please type in y: ", (-100000, 100000), True)
            shape.setY(y)
        elif input_data == 9:
            print(shape.getRadius())
        elif input_data == 10:
            r = get_input("Please type in radius: ", (0, 100000))
            shape.setRadius(r)
        elif input_data == 11:
            view_shape_menu()
            return
        shape_choice()
    elif shape_species == "Cylinder":
        print("Please Select One Choice to Operate the Cylinder:")
        input_data = get_input("1.setName     2.getName       3.getX\n4.getY    5.getArea    6.getVolume\n7.setX      "
                               "8.setY     9.getRadius\n10.setRadius     11.getHeight   12.setHeight\n13.Back to "
                               "higher menu "
                               , (1, 13))
        if input_data == 1:
            name = input("Please input Name")
            shape.setName(name)
        elif input_data == 2:
            print(shape.getName())
        elif input_data == 3:
            print(shape.getX())
        elif input_data == 4:
            print(shape.getY())
        elif input_data == 5:
            print(shape.getArea())
        elif input_data == 6:
            print(shape.getVolume())
        elif input_data == 7:
            x = get_input("Please type in x: ", (-100000, 100000), True)
            shape.setX(x)
        elif input_data == 8:
            y = get_input("Please type in y: ", (-100000, 100000), True)
            shape.setY(y)
        elif input_data == 9:
            print(shape.getRadius())
        elif input_data == 10:
            r = get_input("Please type in radius: ", (0, 100000))
            shape.setRadius(r)
        elif input_data == 11:
            print(shape.getHeight())
        elif input_data == 12:
            h = get_input("Please type in height: ", (0, 100000))
            shape.setHeight(h)
        elif input_data == 13:
            view_shape_menu()
            return
        shape_choice()
    elif shape_species == "Rectangle":
        print("Please Select One Choice to Operate the Rectangle:")
        input_data = get_input("1.setName     2.getName       3.getX\n4.getY    5.getArea    6.getVolume\n7.setX      "
                               "8.setY \n 9.Back to higher menu"
                               , (1, 9))
        if input_data == 1:
            name = input("Please input Name")
            shape.setName(name)
        elif input_data == 2:
            print(shape.getName())
        elif input_data == 3:
            print(shape.getX())
        elif input_data == 4:
            print(shape.getY())
        elif input_data == 5:
            print(shape.getArea())
        elif input_data == 6:
            print(shape.getVolume())
        elif input_data == 7:
            x = get_input("Please type in x: ", (-100000, 100000), True)
            shape.setX(x)
        elif input_data == 8:
            y = get_input("Please type in y: ", (-100000, 100000), True)
            shape.setY(y)
        elif input_data == 9:
            view_shape_menu()
            return
        shape_choice()
    elif shape_species == "Square":
        print("Please Select One Choice to Operate the Point:")
        input_data = get_input("1.setName     2.getName       3.getX\n4.getY    5.getArea    6.getVolume\n7.setX      "
                               "8.setY \n 9.Back to higher menu"
                               , (1, 9))
        if input_data == 1:
            name = input("Please input Name")
            shape.setName(name)
        elif input_data == 2:
            print(shape.getName())
        elif input_data == 3:
            print(shape.getX())
        elif input_data == 4:
            print(shape.getY())
        elif input_data == 5:
            print(shape.getArea())
        elif input_data == 6:
            print(shape.getVolume())
        elif input_data == 7:
            x = get_input("Please type in x: ", (-100000, 100000), True)
            shape.setX(x)
        elif input_data == 8:
            y = get_input("Please type in y: ", (-100000, 100000), True)
            shape.setY(y)
        elif input_data == 9:
            view_shape_menu()
            return
        shape_choice()
    elif shape_species == "Cube":
        print("Please Select One Choice to Operate the Point:")
        input_data = get_input("1.setName     2.getName       3.getX\n4.getY    5.getArea    6.getVolume\n7.setX      "
                               "8.setY \n 9.Back to higher menu"
                               , (1, 9))
        if input_data == 1:
            name = input("Please input Name")
            shape.setName(name)
        elif input_data == 2:
            print(shape.getName())
        elif input_data == 3:
            print(shape.getX())
        elif input_data == 4:
            print(shape.getY())
        elif input_data == 5:
            print(shape.getArea())
        elif input_data == 6:
            print(shape.getVolume())
        elif input_data == 7:
            x = get_input("Please type in x: ", (-100000, 100000), True)
            shape.setX(x)
        elif input_data == 8:
            y = get_input("Please type in y: ", (-100000, 100000), True)
            shape.setY(y)
        elif input_data == 9:
            view_shape_menu()
            return
        shape_choice()
    else:
        return



def get_input(inputStr: str, input_range: tuple = (1,100), can_be_minus = False):
    input_data = input(inputStr)
    if not can_be_minus:
        if not input_data.isdigit() or float(input_data) % 1 != 0 or int(input_data) < input_range[0] or int(input_data) > input_range[1]:
            print("Input Data must be an integer, > 0 and < " + str(input_range[1] + 1))
            return int(get_input(inputStr, input_range))
        else:
            return int(input_data)
    else:
        if not input_data.isdigit():
            print("Input Data must be a number")
            return get_input(inputStr, input_range, True)
        else:
            return input_data
    pass


def create_shape_func():
    x = get_input("Please type in x: ", (-100000, 100000), True)
    y = get_input("Please type in y: ", (-100000, 100000), True)
    name = input("Please type in Shape Name:")
    return {
        "x": x,
        "y": y,
        "name": name,
    }
    pass


def create_shape_menu():
    print("Please Select One Choice to Create a Shape")
    input_data = get_input("1.Point     2.Circle       3.Cylinder\n4.Sphere    5.Rectangle    6.Square\n7.Cube      "
                           "8.Back to higher menu \n"
                           , (1, 8))
    if input_data == 1:
        params = create_shape_func()
        new_point = Point(params["x"], params["y"])
        new_point.setName(params["name"],)
        shape_list.append(new_point)
        print("Create Point Successfully!\n")
        create_shape_menu()

    elif input_data == 2:
        r = get_input("Please type in r: ", (0, 100000))
        params = create_shape_func()
        params['r'] = r
        new_circle = Circle(params["x"], params["y"], params["r"])
        new_circle.setName(params["name"])
        shape_list.append(new_circle)
        print("Create Circle Successfully!\n")
        create_shape_menu()

    elif input_data == 3:
        r = get_input("Please type in r: ", (0, 100000))
        h = get_input("Please type in h: ", (0, 100000))
        params = create_shape_func()
        params['r'] = r
        params['h'] = h
        new_cylinder = Cylinder(params["x"], params["y"], params["r"], params["h"])
        new_cylinder.setName(params["name"])
        shape_list.append(new_cylinder)
        print("Create Cylinder Successfully!\n")
        create_shape_menu()

    elif input_data == 4:
        r = get_input("Please type in r: ", (0, 100000))
        params = create_shape_func()
        params['r'] = r
        new_sphere = Sphere(params["x"], params["y"], params["r"])
        new_sphere.setName(params["name"])
        shape_list.append(new_sphere)
        print("Create Sphere Successfully!\n")
        create_shape_menu()

    elif input_data == 5:
        length = get_input("Please type in length: ", (0, 100000))
        height = get_input("Please type in height: ", (0, 100000))
        params = create_shape_func()
        params['len'] = length
        params['h'] = height
        new_rectangle = Rectangle(params["x"], params["y"], params['len'], params['h'])
        new_rectangle.setName(params["name"])
        shape_list.append(new_rectangle)
        print("Create Rectangle Successfully!\n")
        create_shape_menu()

    elif input_data == 6:
        length = get_input("Please type in length: ", (0, 100000))
        params = create_shape_func()
        params['len'] = length
        new_square = Square(params["x"], params["y"], params["len"])
        new_square.setName(params["name"],)
        shape_list.append(new_square)
        print("Create Square Successfully!\n")
        create_shape_menu()

    elif input_data == 7:
        length = get_input("Please type in length: ", (0, 100000))
        params = create_shape_func()
        params['len'] = length
        new_cube = Cube(params["x"], params["y"], params["len"])
        new_cube.setName(params["name"],)
        shape_list.append(new_cube)
        print("Create Cube Successfully!\n")
        create_shape_menu()
    elif input_data == 8:
        level_one_menu()
    else:
        return


def view_shape_menu():
    print("Please Select One Choice to View Shapes")
    input_data = get_input("1.Select One Shape     2.View All Shapes   3.Back to higher menu \n", (1, 3))
    if input_data == 1:
        print_all_shape()
        shape_choice()
    elif input_data == 2:
        print_all_shape()
        print()
        view_shape_menu()
    elif input_data == 3:
        os.system('clear')
        level_one_menu()


def level_one_menu():
    print("Please Select One Choice")
    input_data = get_input("1.Create a Shape     2.View Shapes   3.Exit \n", (1, 3))
    if input_data == 3:
        return
    elif input_data == 1:
        create_shape_menu()
    elif input_data == 2:
        view_shape_menu()


def print_all_shape():
    print("[", end="")
    for i in range(len(shape_list)):
        if 'getName' in dir(shape_list[i]):
            print(str(i+1) + ".", end="")
            print(shape_list[i].getName(), end="")
            if i != len(shape_list) - 1:
                print(", ", end="")
    print("]")


shape_list = []

if __name__ == '__main__':

    print("#------System Start-------#")
    level_one_menu()

    print("Final Shape List:")
    print_all_shape()
    print("#------System Exit--------#")




