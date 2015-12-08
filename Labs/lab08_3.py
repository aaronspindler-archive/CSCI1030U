#Description: Part three of lab 8 which invovles taking the classes from the
#first two parts of the lab and modifying them to inherit the Shape class

#Importing math
import math

#                           ==== Part 3 ====

#Defining the Shape class
class Shape:
    #Initializing the shape class
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getArea(self):
        return 0

    def getPerimeter(self):
        return 0

#Defining the Rectangle class which inherits from Shape
class Rectangle(Shape):
    #Initializing the Rectangle class
    def __init__(self, width, height):
        self.x = width
        self.y = height
    #Calculating the area of a rectangle
    def getArea(self):
        return self.x * self.y
    #Calculating the perimeter of a rectangle
    def getPerimeter(self):
        return self.x * 2 + self.y * 2
#Defining the Circle class which inherits from Shape
class Circle(Shape):
    #Initializing the Circle class
    def __init__(self,radius):
        self.x = radius
    #Calculating the area of a circle
    def getArea(self):
        return math.pi * pow(self.x,2)
    #Calculating the perimeter of a circle
    def getPerimeter(self):
        return 2 * math.pi * self.x

#Main function
def main():
    #Creating a list of shapes
    shapesList = list()

    #Adding a bunch of Rectangles to the list
    shapesList.append(Rectangle(10.00,20.00))
    shapesList.append(Rectangle(30.00,20.00))
    shapesList.append(Rectangle(60.00,20.00))
    shapesList.append(Rectangle(1.00,3.00))
    shapesList.append(Rectangle(123.00,32.00))
    shapesList.append(Rectangle(4.00,12.00))
    shapesList.append(Rectangle(89.00,10000.00))
    shapesList.append(Rectangle(120.00,220.00))

    #Adding a bunch of Circles to the list
    shapesList.append(Circle(120.00))
    shapesList.append(Circle(32.00))
    shapesList.append(Circle(1.00))
    shapesList.append(Circle(90.00))
    shapesList.append(Circle(1420.00))
    shapesList.append(Circle(41.00))
    shapesList.append(Circle(89.00))
    shapesList.append(Circle(126.00))

    #Looping through the list of shapes and printing the area and perimeter of
    #them
    for shape in shapesList:
        print("Area: ",shape.getArea())
        print("Perimeter: ",shape.getPerimeter())

#Defining the entrypoint of the program
if __name__ == "__main__":
    main()
