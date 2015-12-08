#Description: Part one and two of lab 8 which is focused on OOP

#Importing math
import math
#                           ==== Part 1 ====
#Defining the Rectangle Class
class Rectangle:
    #Initializing the Rectangle class
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #Calculating the area of a rectangle
    def getArea(self):
        return self.width * self.height
    #Calculating the perimeter of a rectangle
    def getPerimeter(self):
        return self.width * 2 + self.height * 2

#                           ==== Part 2 ====
#Defining the Circle Class
class Circle:
    #Initializing the Circle class
    def __init__(self,radius):
        self.radius = radius
    #Calculating the area of a circle
    def getArea(self):
        return math.pi * pow(self.radius,2)
    #Calculating the perimeter of a circle
    def getPerimeter(self):
        return 2 * math.pi * self.radius

#Main function
def main():
    #Testing rectangle class
    testRectangle = Rectangle(10.00,20.00)

    print(testRectangle.getArea())
    print(testRectangle.getPerimeter())

    #Testing circle class
    testCircle = Circle(20.00)

    print(testCircle.getArea())
    print(testCircle.getPerimeter())

#Defining the entrypoint of the program
if __name__ == "__main__":
    main()
