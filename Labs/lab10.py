#Description: Create a function called calculate which takes in a reverse polish
# notation string and returns the calculated answer

#A function to check if a number is an integer
def isInteger(str):
   for chr in str:
      if (chr < '0') or (chr > '9'):
         return False
   return True

#A function to conver a string into an integer
def toInteger(str):
   return int(str)

#The function that calculates the result of a reverse polish notation string
# and returns the result
def calculate(rpnString):
    #Create an empty list, that we will use like a stack
    workStack = []
    #Loop through all of the characters in the rpnString that was passed to the
    # function
    for token in rpnString.split(' '):
        #If the token is an integer just append it to the list
        if(isInteger(token)):
            workStack.append(toInteger(token))
        #Otherwise pop two numbers off of the stack
        else:
            num1 = workStack.pop()
            num2 = workStack.pop()
            #Then check which operator the token is and append the result of the
            # operator on the two numbers
            if(token == "+"):
                workStack.append(num2 + num1)
            elif(token == "-"):
                workStack.append(num2 - num1)
            elif(token == "*"):
                workStack.append(num2 * num1)
            elif(token == "/"):
                workStack.append(num2 / num1)
    #Finally return the result
    return workStack.pop()

#Testing the function
print(calculate("8 4 * 7 2 / + 4 1 + -"))
