# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:31:40 2015

@author: 100539147
"""

# Conditionals

"""
	Threshold of pain                - 130dB
	Possible hearing damage          - 120dB
	Jack hammer at 1m                - 100dB
	Traffic on a busy roadway at 10m -  90dB
	Normal conversation              -  30dB
	Light leaf rustling              -   0dB
"""
# Question 1
def closestNoise(decibels):
    if decibels < 15:
        return "Light leaf rustling"
    elif decibels < 60:
        return "Normal conversation"
    elif decibels < 95:
        return "Traffic on a busy roadway at 10m"
    elif decibels < 110:
        return "Jack jammer at 1m"
    elif decibels < 125:
        return "Possible hearing damage"
    else:
        return "Threshold of pain"

print "  0 decibels is most similar to ", closestNoise(0)
print " 14 decibels is most similar to ", closestNoise(14)
print " 15 decibels is most similar to ", closestNoise(15)
print " 30 decibels is most similar to ", closestNoise(30)
print " 60 decibels is most similar to ", closestNoise(60)
print " 75 decibels is most similar to ", closestNoise(75)
print " 95 decibels is most similar to ", closestNoise(95)
print "103 decibels is most similar to ", closestNoise(103)
print "110 decibels is most similar to ", closestNoise(110)
print "120 decibels is most similar to ", closestNoise(120)
print "125 decibels is most similar to ", closestNoise(125)
print "190 decibels is most similar to ", closestNoise(190)

"""
	divisible by   4 - leap year, except:
	divisible by 100 - not a leap year, except:
	divisible by 400 - leap year
"""
# Question 2
def leapYear(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

print "is 2015 a leap year?", leapYear(2015) # False
print "is 2016 a leap year?", leapYear(2016) # True
print "is 2000 a leap year?", leapYear(2000) # True
print "is 2100 a leap year?", leapYear(2100) # False

# Loops

# Question 3
def sumOfSquares(min, max):
    sum = 0
    for num in range(min, max + 1):
        sum += num**2
    return sum

print "sum of squares between 1 and 10:"
print sumOfSquares(1,10)  # 385

print "sum of squares between 1 and 5:"
print sumOfSquares(1,5)  # 55

# Question 4
def factors(n):
    factors = []
    for i in range(1, n + 1):
        if (n % i) == 0:
            factors.append(i)
    return factors

print "Factors of 12:", factors(12)
print "Factors of 20:", factors(20)
print "Factors of 100:", factors(100)

# Lists

# Question 5
def powersOf2(n):
    powers = []
    for i in range(n+1):
        powers.append(2**i)
    return powers

print "2^0 .. 2^4:  ", powersOf2(4)
print "2^0 .. 2^10: ", powersOf2(10)


# Question 6
def areEqual(list1, list2):
    if subset(list1, list2) and subset(list2, list1):
        return True
    else:
        return False

def subset(list1, list2):
    for elem1 in list1:
        if elem1 not in list2:
            return False
    return True

print areEqual([1,2,3], [3,1,2])
# True
print areEqual([1,2,3], [4,1,3])
# False
print areEqual([1,8,15], [1,15,8])
# True


# Question 7
def filterPrimes(list):
    primes = []
    for elem in list:
        if isPrime(elem):
            primes.append(elem)
    return primes

def isPrime(n):
    for div in range(2,n):
        if (n % div) == 0:
            return False
    return True

print filterPrimes(range(20))
# [0, 1, 2, 3, 5, 7, 11, 13, 17, 19]
print filterPrimes(range(100,200))
# [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

# Classes

# Question 8
class Pet:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return

class Dog(Pet):
    def speak(self):
        print self.name, "- Woof!"

class Cat(Pet):
    def speak(self):
        print self.name, "- Meow!"

class Bird(Pet):
    def speak(self):
        print self.name, "- Cheep!"

bird1 = Bird("Pete")
bird2 = Bird("Yappy")
cat1 = Cat("Boots")
cat2 = Cat("Mr. Fluffington")
cat3 = Cat("Sylvester")
dog1 = Dog("Spot")
dog2 = Dog("Odie")
dog3 = Dog("Charles Wellington III")
pets = [cat1, dog1, dog2, bird1, cat2, bird1, dog3, cat3]
for pet in pets:
    pet.speak()

# Question 9
import math

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distanceTo(self, otherPoint):
        dx = self.x - otherPoint.x
        dy = self.y - otherPoint.y
        dz = self.z - otherPoint.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

p1 = Point3D(2.0, 2.0, 4.0)
p2 = Point3D(3.0, 1.0, 2.0)
print "distance between p1 and p2:", p1.distanceTo(p2)


# Question 10 (Extra challenging)
def solveHanoi(source, dest, temp, count):
   if count == 0:
      return

   solveHanoi(source, temp, dest, count-1)
   move1(source, dest)
   solveHanoi(temp, dest, source, count-1)

def move1(source, dest):
   print "Move top ring from peg", source, "to peg", dest

solveHanoi(1, 3, 2, 3)