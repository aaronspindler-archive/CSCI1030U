#Description: Assignment number 1 which includes functions to determine if a
# number is prime, determine the prime factors of a number, reverse complement
# a nucleotide sequence, estimate the value of Pi using a different method than
# used in the labs, and determine if there are any intersections between two lists.

import math
import sys

#                           ---- Part 1 ----
#A function that determines if a number is prime or not.
def isPrime(numIn):
    #If the number is less than two it is not prime so return false
    if(numIn < 2):
        return False
    #If the number divisible by 2 with no remaineder the number is not prime,
    #so return false
    elif(numIn % 2 == 0):
        return False
    #Check the last options for the number by finding the divisors of a number
    #If any of the divisors go into the number without a remained the number is
    #not prime so return false
    squareRoot = int(math.sqrt(numIn))
    for div in range(3,squareRoot,2):
        if(numIn % div == 0):
            return False
    #If the functions has not returned false yet then the number must be prime,
    #so return true
    return True

#Testing isPrime
print(isPrime(8))
print(isPrime(7))
print(isPrime(0))

#A function to find the prime factors of a number
def primeFactors(numIn):
    #If the number is prime return the number as a list that was inputted
    if(isPrime(numIn)):
        return list(numIn)
    factor = 2
    primeFactors = []
    #Loop through until the factor squared is greater than numIn
    while factor * factor <= numIn:
        if numIn % factor:
            factor += 1
        else:
            #Floor divide numIn by the factor
            numIn //= factor
            #Add the factor to the prime factors list
            primeFactors.append(factor)
    if numIn > 1:
        primeFactors.append(numIn)
    #Make sure that there are no duplicates in the list
    primeFactors = removeDuplicates(primeFactors)
    #Return the prime factors
    return primeFactors

#Remove any duplicates from the list
def removeDuplicates(arrIn):
    return list(set(arrIn))

#Testing primeFactors
print(primeFactors(2))
print(primeFactors(187))
print(primeFactors(2058))



#                           ---- Part 2 ----
#A function that takes in a nucleotide sequence and returns the reverse
# complemented version of it.
def reverseComplement(inputNuc):
    #Return the inputted sequence after passing it to the complement and the
    #reverse function
    return reverseSequence(complementSequence(inputNuc))

#A function that returns a nucleotide sequence that has been complemented
def complementSequence(inputNuc):
    #Passing the input to a local list to be manipulated
    nucleotideList = list(inputNuc)
    #Loop through the list
    for x in range(len(nucleotideList)):
        #Call the complement complementSingleNucleotide for each char in the]
        #list
        nucleotideList[x] = complementSingleNucleotide(nucleotideList[x])
    #Return the list as a string
    return(''.join(nucleotideList))

#A function that complements a single nucleotide based on the table given in the
#assignment description
def complementSingleNucleotide(inChar):
    if(inChar == 'G'):
        return 'C'
    elif(inChar == 'C'):
        return 'G'
    elif(inChar == 'A'):
        return 'T'
    elif(inChar == 'T'):
        return 'A'

#A function that returns a reversed nucleotide sequence
def reverseSequence(inputNuc):
    #Converting the string into a list so that each char can be manipulated
    #individually
    reversedSequence = list()
    for x in range(len(inputNuc)):
        #Add the chars to reversedSequence in reverse order of how they were
        #inputted
        reversedSequence.append(inputNuc[-(x+1)])
    #Return the reversedSequence as a string
    return(''.join(reversedSequence))

#Testing reverseComplement
print(reverseComplement('TTGAGCTATCGACTAG'))
print(reverseComplement('CGAATGGC'))
print(reverseComplement('CGGTCCAATAGATTCGAA'))



#                           ---- Part 3 ----
#A function using the Gregory-Liebniz series to approximate Pi
def gregoryLiebniz(numIterations):
    piApprox = 0
    #Loop through the number of times that are passed to the function
    for x in range(numIterations):
        #Calculate the sum of the previous iterations plus the current iteration
        piApprox = piApprox + ((4*pow(-1,x))/((2*x)+1))
    return piApprox

#Testing the gregoryLiebniz function
print(gregoryLiebniz(10000000))
print(gregoryLiebniz(10))
print(gregoryLiebniz(123))



#                           ---- Part 4 ----
#Finding intersections in lists
def intersect(list1,list2):
    intersections = []
    #Loop through the first list so that all numbers are covered in the first
    for x in range(len(list1)):
        #Loop through the second list for every element in the first list
        for y in range(len(list2)):
            #Compare the values of the first list at position x to the value of
            #the second list at position y thus detecting a collision
            if(list1[x] == list2[y]):
                #If a collision happens add it to the intersections list
                intersections.append(list1[x])
    #Finally return the intersections once all of the loops are done
    return intersections

#Testing intersections function
print(intersect([1,3,5,7,9,11,13,15,17,19,21,23,25], [1,4,9,16,25]))
print(intersect([1,3,5,7,25], [4,9,16]))
print(intersect([1], [1,4,9,16,25]))
