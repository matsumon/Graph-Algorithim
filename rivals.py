import sys
#creates the groups by flipping back and forth between groups depending on what
#layer of the "tree" the search is in. IE 0 goes in group 0 and then its children
#go in group 1 and the children of the children go in group 0
def CreateGroups(array,parentIndex,toggle):
    if len(queue)==0:
        return
    length = len(array)
    for index in range(length):
        if(array[index][1]==parentIndex):
            group[toggle].append(array[index][0])
            newParent= array[index][0]
            newArray = array.copy()
            newArray.remove(array[index])
            newToggle = toggle
            newToggle ^= 1
            CreateGroups(newArray,newParent,newToggle)
#grabbing all the children and stuffing it into a queue to be looked at
def branch():
    visited=[0]*numberPeople
    x=queue[0][0]
    while(x < len(queue)):
        i=queue[x][0]
        j=0
        while j < numberPeople:
            if(array[i][j]==1 and visited[j] == 0):
                queue.append((j,i))
                visited[i]=1
            j=j+1
        x=x+1
# open input file
cap = str(sys.argv[1])
file = open(cap,"r")
# read in every line into an array
allLines = file.readlines()
# get the number of people
numberPeople = int(allLines[0].strip())
# get the number of rivalries
numberRivals = int(allLines[0 + numberPeople + 1].strip())
# make array to hold the connections
array = []
flattenedArray = []
for i in range(numberPeople):
    array.append([0]*numberPeople)
# array to Hold people
peopleArray = []
for people in range(numberPeople):
    peopleArray.append(allLines[people+1].strip())
# array to hold rival connections
rivalryArray = []
for rivals in range(numberRivals):
    rivalList = allLines[rivals+2+numberPeople].split()
    rivalryArray.append((rivalList[0],rivalList[1]))
    flattenedArray.append(rivalList[0])
    flattenedArray.append(rivalList[1])
index = peopleArray.index(rivalryArray[0][0])
# intializing array with rivalries
for rivals in range(numberRivals):
    indexOne = peopleArray.index(rivalryArray[rivals][0])
    indexTwo = peopleArray.index(rivalryArray[rivals][1])
    array[indexOne][indexTwo] = 1
    array[indexTwo][indexOne] = 1
#queue is the queue for the different elements of the tree to walkthrough 
#the first element represents the name, the 2nd element represents the parent index
# the first element added to the queue is the intial starting one
# visited reprents whether element has been visited or not 0-no 1-yes
queue = [(0,-1)]
branch()

group = [[],[]]
CreateGroups(queue,-1,0)
entireGroup=group[0]+group[1]
checkDiff= list(set(range(numberPeople))-set(entireGroup))
while(len(checkDiff)!=0):
    queue.append((checkDiff[0],-1))
    branch()
    CreateGroups(queue,-1,0)
    entireGroup=group[0]+group[1]
    checkDiff= list(set(range(numberPeople))-set(entireGroup))
possible = True
for e1 in group[0]:
    for e2 in group[1]:
        if e1 == e2:
            possible = False
if(possible):
    groupOneArray = []
    groupTwoArray = []
    for index in set(group[0]):
        groupOneArray.append(peopleArray[index])
    for index in set(group[1]):
        groupTwoArray.append(peopleArray[index])
    print("Beavers", groupOneArray)
    print("Ducks", groupTwoArray)
else:
    print("Groups Can't Be Made")


