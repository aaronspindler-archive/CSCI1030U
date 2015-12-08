#Part 1 - Celsius to Fahrenheit Calculator
#Input for the celcius variable
celsius = float(input("Temperature in Celsius: "))
#Fahrenheit calculation
fahrenheit = (celsius * 9.0/5.0) + 32
#Printing out the fahrenheit value
print("Temperature in Fahrenheit:",fahrenheit)

#Printing out a blank line so there is a line gap
print("")

#Voting Decision Statement

#Variables
name = "Rachel"
#Printing the persons name
print("Hi there,", name)

age = 18
#If statment deciding if the person is of the correct age to vote
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you will need to wait.")

#Printing out a blank line so there is a line gap
print("")

#Part 2 - Intrest Calculator
#Getting input for the principle amount and the intrest rate
principleAmount = float(input("Principal amount:" ))
intrestRate = float(input("Intrest rate: "))

#for-loop to run the calculation 5 times
for x in [1,2,3,4,5]:
    principleAmount = principleAmount * (1 + intrestRate)

#Outputting the final principle amount after the calculation
print("New Principal:", principleAmount)

#Printing out a blank line so there is a line gap
print("")
