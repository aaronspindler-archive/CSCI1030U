"""
Description: Lab that is used to practice defining and using functions in python
Functions in File: approximatePi, getMembersInRange, and removeEven
"""

#Importing the library needed for this program
import math
import sys

#A function to approximate the value of pi using Archimedes method.
def approximatePi(epsilon):
    #Estimating Pi using Archimedes method / formula
    piEstimate = 0

    for x in range(3,1000000):
        piEstimate = x*(math.sin(math.radians(180.00)/x))
        #If the approximation is within the error margin break the loop so that it does not continue
        #to print numbers that are more exact
        if(math.pi - epsilon <= piEstimate <= math.pi + epsilon):
            break

    print("A polygon of with",int(x),"sides approximates Pi as:",piEstimate)
    return piEstimate

#A function to only return the numbers from a list that are within the upper and
#lower bounds.
def getMembersInRange(listNums, lowerLimit, upperLimit):
    #Creating a list to store members that fit within the limits
    memberNums = []
    #Looping through the original list
    for x in listNums:
        #If the number is within the bounds add it to the list of numbers that
        #will be returned.
        if(x >= lowerLimit and x <= upperLimit):
            memberNums.append(x)
    #Return the list of numbers that fit within a range
    return memberNums

#A function to return only the odd numbers from a list by removing all even
#numbers.
def removeEven(listNums):
    #Creating a list to store the odd numbers
    numsToReturn = []
    #Looping through the original list
    for x in listNums:
        #If the number is not even add it to the list of numbers that
        #will be returned.
        if(x%2 != 0):
            numsToReturn.append(x)
    #Return the list of odd numbers
    return numsToReturn

#Main function used for testing all functions defined above
def main():
    #Testing approximatePi function
    approximatePi(0.0000001)

    #Testing getMembersInRange
    print(getMembersInRange([8,3,11,5,2,21,38,1,7], 3, 10))
    print(getMembersInRange([8,3,11,5,2,21,38,1,7], 1, 20))

    #Testing removeEven
    print(removeEven([8,3,11,5,2,21,38,1,7]))

#Defining the entrypoint of the program
if __name__ == "__main__":
    main()
