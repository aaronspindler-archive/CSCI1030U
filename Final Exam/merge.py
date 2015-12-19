def merge(left, right):
    result = []
    i,j = 0,0
    
    while i < len(left) and j < len(right):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
    
def mergeSort(myList):
    if(len(myList) < 2):
        return myList[:]
    else:
        middle = len(myList)//2
        left = mergeSort(myList[:middle])
        right = mergeSort(myList[middle:])
        return merge(left, right)
        
print mergeSort([15,6,34,19,2,45,31,26,8,39])