file = open("input.txt","r")
text = file.readlines()
plain_text = []
tmplst = []

groupList = []
groupListNumber = []

totalNum = 0

for i in text:
    tmp = i.strip()
    if tmp != '':
        tmplst.extend(tmp.split(" "))
    if tmp == '' or i == text[-1]:
        plain_text.append((tmplst))
        tmplst = []


for group in plain_text:
    groupTempList = []
    for person in group:
        for item in person:
            if item not in groupTempList:
                groupTempList.append(item)
    groupList.append(groupTempList)
    groupListNumber.append(len(groupTempList))

for num in groupListNumber:
    totalNum = totalNum + num

print(groupList)
print(groupListNumber)