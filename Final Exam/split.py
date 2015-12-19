def split(stringIn):
    stringList = []
    charPositions = []
    
    currentPos = 0
    lastPos = 0
    
    for char in stringIn:
        if(char == ' '):
            charPositions.append(currentPos)
            stringToAdd = stringIn[lastPos:currentPos]
            stringList.append(stringToAdd)
            lastPos = currentPos + 1
        currentPos += 1
        
    if(charPositions[-1] < len(stringIn)):
        stringList.append(stringIn[charPositions[-1] + 1:])
    print(stringList)
        
split("the quick brown fox jumped over the lazy dog")
    