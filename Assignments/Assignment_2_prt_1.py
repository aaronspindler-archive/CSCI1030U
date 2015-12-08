#Description: Create two functions that search a list for a number. Done using
# a recursive and an iterative method

#Sorting Algorithm from Lab 09
def insertionSort(listIn):
    for x in range(1,len(listIn)):
        currentValue = listIn[x]
        position = x

        while position > 0 and listIn[position - 1] > currentValue:
            listIn[position] = listIn[position - 1]
            position = position - 1

        listIn[position] = currentValue

#Binary Search Iterative
def binarySearchIter(value, data, start, end):
    #If the list has 0 elements return False because the list is empty
    if(len(data) == 0):
        return False
    #Make sure the list is in sorted order
    insertionSort(data)

    #While the start number is less then or equal to the end number continue
    while(start <= end):
        #Find the midpoint of the list by finding the floored average
        mid = (start+end)//2
        #If the data at the midpoint is the value you are looking for, return
        # true
        if(data[mid] == value):
            return True
        else:
            #If the data at the midpoint is greater than the value, change the
            # end number to be the midpoint minus 1
            if(data[mid] > value):
                end = mid-1
            else:
                #Otherwise make the start value the midpoint plus 1
                start = mid+1
    return False

#Binary Search Recursive
def binarySearchRec(value, data, start, end):
    #If the list has 0 elements return False because the list is empty
    if(len(data) == 0):
        return False
    #Make sure the list is in sorted order
    insertionSort(data)

    #If the start somehow becomes greater than the end value return False
    if(start > end):
        return False
    #Calculate the midpoint of the list by finding the floored average
    mid = (start + end)//2

    #If the data at the midpoint is the value you are looking for, return
    # true
    if data[mid]==value:
        return True
    #If the value at the midpoint is greater than the value you are looking for
    # recursively call the function binarySearchRec with the end value changed
    # to the midpoint minus 1
    elif data[mid] > value:
        return binarySearchRec(value,data,start,mid-1)
    #If the value at the midpoint is less than the value you are looking for
    # recursively call the function binarySearchRec with the start value changed
    # to the midpoint plus 1
    elif data[mid] < value:
        return binarySearchRec(value,data,mid+1,end)

#Defining the test list
testList = [10,2,3,4,1,23,41,2,3,1,2,3,1,4,1,23,1]

#Testing Recursive Binary Search Function
print("Should be True:",binarySearchRec(1,testList,0,len(testList)-1))
print("Should be True:",binarySearchRec(2,testList,0,len(testList)-1))
print("Should be True:",binarySearchRec(23,testList,0,len(testList)-1))
print("Should be False:",binarySearchRec(97,testList,0,len(testList)-1))
print("Should be False:",binarySearchRec(1000,testList,0,len(testList)-1))

#Testing Iterative Binary Search Function
print("Should be True:",binarySearchIter(1,testList,0,len(testList)-1))
print("Should be True:",binarySearchIter(2,testList,0,len(testList)-1))
print("Should be True:",binarySearchIter(23,testList,0,len(testList)-1))
print("Should be False:",binarySearchIter(97,testList,0,len(testList)-1))
print("Should be False:",binarySearchIter(1000,testList,0,len(testList)-1))
