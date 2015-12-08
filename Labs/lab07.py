#Date: 10/28/2015

#A constant investment calculation function that uses a for loop to calculate
#the final amount after a defined number of years
def constantInvestmentI(principal, annualContrib, growthRate, years):
    #Saving the amount outside to loop so that each time the loop runs it can
    #modify a variable with the new intrest
    finalAmount = 0.0
    for y in range(years):
        #Calculating the new amount of money that will be used for the next
        #iteration
        finalAmount = (finalAmount + annualContrib) * (1 + growthRate)
    #Finally print the finalAmount
    print(finalAmount)

#Testing constantInvestmentI
constantInvestmentI(0, 10000, 0.05, 5)

#A constant investment calculation function that uses recursion to calculate the
#final amount after a defined number of years
def constantInvestmentR(principal, annualContrib, growthRate, years):
    #The exit case for the recursion
    if(years <= 0):
        print(principal)
    else:
        #Call the same constantInvestmentR function with a new principal amount and reduce the number of years by 1
        constantInvestmentR((principal + annualContrib)*(1 + growthRate), annualContrib, growthRate, years = years - 1)

#Testing constantInvestmentR
constantInvestmentR(0, 10000, 0.05, 5)

#A variable rate investment calculation function that uses a for loop to
#calculate the final amount after a defined number of years
def variableInvestmentI(principal, annualContrib, growthRates, years):
    #Saving the amount outside to loop so that each time the loop runs it can
    #modify a variable with the new intrest
    finalAmount = 0.0
    for y in range(years):
        #Calculate the final amount of money using a new intrest rate each year
        finalAmount = (finalAmount + annualContrib) * (1 + growthRates[y])
    #Finally print the finalAmount
    print(finalAmount)

#Testing variableInvestmentI
variableInvestmentI(0, 10000, [0.05,0.03,0.015,0.045,0.06], 5)

#A variable rate investment calculation function that uses recursion to
#calculate the final amount after a defined number of years
def variableInvestmentR(principal, annualContrib, growthRates, years):
    #The exit case for the recursion
    if(years <= 0):
        print(principal)
    else:
        #Set the growth rate for the current iteration of the function
        growthRate = growthRates[0]
        #Then remove the growthRate from the list of rates so that the next time
        #the function runs it will have the correct rate in the [0] position
        #of the growth rate list
        growthRates.pop(0)
        #Decrement years by 1
        years =  years - 1
        #Recursively call the function variableInvestmentR with the new principal
        variableInvestmentR((principal + annualContrib)*(1 + growthRate),annualContrib,growthRates,years)

#Testing variableInvestmentR
variableInvestmentR(0, 10000, [0.05,0.03,0.015,0.045,0.06], 5)
