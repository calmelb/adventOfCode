file = open("input.txt","r")
text = file.readlines()
plain_text = []

seatIDs = {}

largestID = 0
largestSeat = ""

mySeat = ""
mySeatID = 0
mainIDs = []

for i in text:
    plain_text.append(i.strip())


def getRow(input):
    rowRange = list(range(0, 128))

    row = input[:-3]
    for letter in row:
        halfway = (len(rowRange)/2)
        if letter == "B":
            rowRange = rowRange[int(halfway):]
        elif letter == "F":
            rowRange = rowRange[:int(halfway)]
    return rowRange[0]


def getColumn(input):
    colRange = list(range(0, 8))

    col = input[-3:]
    for letter in col:
        halfway = (len(colRange)/2)
        if letter == "R":
            colRange = colRange[int(halfway):]
        elif letter == "L":
            colRange = colRange[:int(halfway)]
    return colRange[0]


for seat in plain_text:
    row = getRow(seat)
    column = getColumn(seat)
    seatID = (row * 8) + column

    seatIDs[seat] = seatID

# print(seatIDs)
## Part 1

# for seat in plain_text:
#     if seatIDs.get(seat) > largestID:
#         largestID = seatIDs.get(seat)
#         largestSeat = seat
#
# # Results Printing:
#
# print("\n---RESULTS---\nLargest Seat Location: " + largestSeat)
# print("Largest Seat ID: " + str(largestID))

## Part 2

for seatMap in seatIDs:
    mainIDs.append(seatIDs.get(seatMap))
mainIDs.sort()

for seatIndex in range(0, len(mainIDs)-1):
    if mainIDs[seatIndex] != mainIDs[seatIndex+1]-1:
        mySeatID = mainIDs[seatIndex] + 1
        # largestSeat = seat

# Results Printing:

print("\n---RESULTS---\nMy Seat Location: " + mySeat)
print("My Seat ID: " + str(mySeatID))