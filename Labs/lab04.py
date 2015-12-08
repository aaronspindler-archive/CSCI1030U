#Date: October 8th 2015

#Practising printing the statment testing 1 2 3...
print("testing 1 2 3...")

#Printing numbers, variables, and num equations
x=8
print(x)
print(x*2)

#Defining other variable types
name = "Carla Rodriguez Mendoza"
length = 14.5
width = 7.25

#Printing statments
print("X: ")
print(x)
print("Name:", name)

#Printing nums attached to words
print("length:" + str(length))
print("width:",)

#Defining more variables
firstName = "Maya"
lastName = "Pandit"
age = 20
birthMonth = "December"

#Printing longer statments with multiple data types
print(firstName, lastName, "is", age, "years old. Her next birthday is in",birthMonth + ".")

#Inputing a number and then using if statments to determine what to print
num = int(input("Enter a number:"))
secretNum = 6
if(num > secretNum):
    print("Lower")
elif(num < secretNum):
    print("Higher")
elif(num == secretNum):
    print("You got it!")


num = int(input("Enter a number:"))
if num >= 5 and num <= 10:
	print "This number is between 5 and 10"
elif num < 5 or num >10:
	print "This number is not between 5 and 10"



#Inputing a grade number and determining what grade letter is corresponds to
#using if statements
gradeNum = int(input("Enter a grade number:"))
if(gradeNum < 50):
    print("F")
elif(gradeNum > 49 and gradeNum < 60):
    print("D")
elif(gradeNum > 59 and gradeNum < 70):
    print("C")
elif(gradeNum > 69 and gradeNum < 80):
    print("B")
elif(gradeNum > 79):
    print("A")
