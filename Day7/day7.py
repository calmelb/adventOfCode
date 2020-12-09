debug = 1

if debug == 0:
    file = open("input.txt","r")
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

newBags = []
newBagCount = 0

def bagContents(bagrequest):
    # {'dark olive': '1', 'vibrant plum': '2'}
    bagInside = bagList.get(bagrequest)
    for item in bagrequest



