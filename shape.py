import math
from abc import abstractmethod


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


def print_shape(list):
    for i in list:
        i.getName()


def print_secondary_menu(dataType):
    if dataType == 1:
        print("Please input operation number")
        print("1.getX  2.getY  3.getArea  4.getVolume  5.setX  6.setY")
    elif dataType == 2:
        print("")
    elif dataType == 3:
        print("")
    elif dataType == 4:
        print("")
    elif dataType == 5:
        print("")
    elif dataType == 6:
        print("")
    elif dataType == 7:
        print("")
    else:
        return False


def get_input(inputStr: str, input_range: tuple = (1,100), can_be_minus = False):
    input_data = input(inputStr)
    if not can_be_minus:
        if float(input_data) % 1 != 0 or int(input_data) < input_range[0] or int(input_data) > input_range[1]:
            print("Input Data must be an integer, > 0 and < " + str(input_range[1] + 1))
            get_input(inputStr, input_range)
        else:
            return int(input_data)
    else:
        if not input_data.isdigit():
            print("Input Data must be a number")
            get_input(inputStr, input_range)
        else:
            return input_data
    pass


def create_shape_menu():
    print("Please Select One Choice to Create a Shape")
    input_data = get_input("1.Point     2.Circle    3.Cylinder\n4.Sphere    5.Rectangle    6.Cube\n7.Back to higher "
                           "menu\n", (1, 7))
    if input_data == 1:
        x = get_input("Please type in x: ", (-100000, 100000), True)
        y = get_input("Please type in y: ", (-100000, 100000), True)
        name = input("Please type in Shape Name:")
        new_point = Point(x, y)
        new_point.setName(name)
        shape_list.append(new_point)

    elif input_data == 2:
        print("")
    elif input_data == 3:
        print("")
    elif input_data == 4:
        print("")
    elif input_data == 5:
        print("")
    elif input_data == 6:
        print("")
    elif input_data == 7:
        level_one_menu()
    else:
        return


def view_shape_menu():
    print("Did view menu")
    shape_list.append("22243")
    print(shape_list)


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



    # print("Please input number as following to create shapes")
    # print("1.Point     2.Circle    3.Cylinder   4.Sphere    5.Rectangle")
    # print("6.Square    7.Cube   8.Exit")
    # shape_list = []
    # loop_flag = True
    # while loop_flag:
    #     print("Please input number:")
    #     data = int(input())
    #     if data % 1 != 0 or data < 1 or data > 8:
    #         print("number should be >= 1 , <= 8 and an integer")
    #         continue
    #     if data == 8:
    #         print("Thank you for using")
    #         break
    #     # --------
    #     # 自己补充一下用户自由操作部分的内容，需要实现用户新建对象，支持对对象进行操作（getArea等）
    #     if data == 1:
    #         print("")
    #     elif data == 2:
    #         print("")
    #     elif data == 3:
    #         print("")
    #     elif data == 4:
    #         print("")
    #     elif data == 5:
    #         print("")
    #     elif data == 6:
    #         print("")
    #     elif data == 7:
    #         print("")

        # --------



