file = open("input.txt","r")
text = file.readlines()
plain_text = []

seatIDs = {}

largestID = 0
largestSeat = ""

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

for seat in plain_text:
    if seatIDs.get(seat) > largestID:
        largestID = seatIDs.get(seat)
        largestSeat = seat

# Results Printing:

print("\n---RESULTS---\nLargest Seat Location: " + largestSeat)
print("Largest Seat ID: " + str(largestID))