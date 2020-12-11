debug = 0

if debug == 0:
    file = open("input.txt","r")
elif debug == 2:
    file = open("test2.txt","r")
else:
    file = open("test.txt","r")

text = file.readlines()
bagList = {}
tmplist = {}
fullListBag = []

for i in text:

    tmpContentsDict = {}
    words = i.split()
    contents = ' '.join(words[4:]).split(", ")
    itemJoined = ' '.join(' '.join(words[:3]).split(" ")[:2])
    for item in contents:
        if item == "no other bags.":
            tmpContentsDict["None"] = 0
        else:
            joined = ' '.join(item[2:].split()[:2])
            tmpContentsDict[joined] = item[:1]
    if "no other bags." in contents:
        tmplist[' '.join(words[:3])] = tmpContentsDict
    else:
        tmplist[itemJoined] = tmpContentsDict
    bagList = tmplist


def getSupportingBags(bagRequest):
    listOfBags = []

    for item in bagList:
        for bag in bagList.get(item):
            if bag == bagRequest:
                listOfBags.append(item)
                listOfBags.append(getSupportingBags(item))
    return listOfBags

def inList(item):
    if item not in fullListBag:
        fullListBag.append(item)
    # else:
    #     print("Already In!")

def listOrganisation(bagrequest):
    listBag = getSupportingBags(bagrequest)
    for i in listBag:
        if isinstance(i, list):
            listExplosion(i)
            # print(i)
        else:
            inList(i)

def listExplosion(listIn):
    if isinstance(listIn, list):
        for j in listIn:
            listExplosion(j)
    else:
        inList(listIn)

    # for j in listIn:
    #     if isinstance(j, list):
    #         for i in j:
    #             listExplosion(i)
    #     else:
    #         inList(j)



listOrganisation("shiny gold")
print(fullListBag)

print("\nLength: " + str(len(fullListBag))+"\n")
print(bagList)

# /---Part 2---\
print("\n ------ PART 2 ------\n")

newBags = []
newBagCount = 0

def bagContents(bagrequest):
    global newBagCount
    # {'dark olive': '1', 'vibrant plum': '2'}
    bagInside = bagList.get(bagrequest)
    if bagInside is None:
        print("End of chain!")
        return 0
    else:
        for item in bagInside:
            print(item)
            newBags.append(item)
            noBags = int(bagInside.get(item))
            for num in range(0, noBags):
                bagContents(item)
            newBagCount = newBagCount + noBags




bagContents('shiny gold')
# bagContents('faded blue')
print(newBags)
print(newBagCount)

