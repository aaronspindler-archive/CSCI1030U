#Date: 10/15/2015

#Importing the math library
import math

#A function to find approximate the cube root of a number x
def cubeRoot(x):
    epsilon = 0.00001
    num = x
    guess = num / 2

    while abs(guess**3 - num) >= epsilon:
        delta = abs(guess**3 - num) / 100.0
        guess = guess - delta
        print "Guess:", guess


#Testing the function
print(cubeRoot(8.0))

#A function to approximate the value of pi using Archimedes method
def approximatePi(polygonSides):
    #Computing the estimated value of pi based on the number of sides in a polygon
    piEstimate = polygonSides*(math.sin(math.radians(180.00)/polygonSides))
    print("A polygon of with",int(polygonSides),"sides approximates Pi as:",piEstimate)
    return piEstimate

#Finding the number of sides that evaluates to pi within a certain margin of error
for x in range(3,1000000000):
    errorMargin = 0.00000000001
    #Using the function defined above
    approximation = approximatePi(float(x))
    #If the approximation is within the error margin break the loop so that it does not continue
    #to print numbers that are more exact
    if(math.pi - errorMargin <= approximation <= math.pi + errorMargin):
        break
