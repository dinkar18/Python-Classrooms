def wordFrequencies(myList):
    #dinkarTaneja 1911380
    Dictionary = {}
    for x in myList:
        Dictionary[x] = myList.count(x)  
    return (Dictionary)    
#dinkarTaneja 1911380

myList = ["Hi","This","is","python","Hi","This","is","scripting","language"]
#dinkarTaneja 1911380
print("Original list: ",myList)
#dinkarTaneja 1911380
myDict = wordFrequencies(myList)
print("Dictionary with word frequencies : ",myDict)



