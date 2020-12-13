
def invertDict(myDict):
    Dict = {}
    for key,value in myDict.items():
        Dict[value] = key
    return Dict
#dinkarTaneja 1911380
def sortDict(Dict):
    return[(i, Dict[i]) for i in sorted(Dict.keys())]
#dinkarTaneja 1911380

def wordFrequencies(myList):
    Dictionary = {}
    for x in myList:
        Dictionary[x] = myList.count(x)  
    return (Dictionary)    
#dinkarTaneja 1911380

myList = ["Hi","This","is","python","Hi","This","is","Scripting","language"]
myDict = wordFrequencies(myList)

invertedDict = invertDict(myDict)
sortedDict = sortDict(invertedDict)

print("Sorted Dictionary: ",sortedDict)