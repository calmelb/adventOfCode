debug = 1

if debug == 0:
    file = open("input.txt","r")
else:
    file = open("test.txt","r")

text = file.readlines()
bagList = {}
tmplist = {}
fullCode = []

accumulator = 0
programPointer = 0
listProgramPointer = []

for i in text:
    fullCode.append(i.strip().split(" "))


for line in fullCode:
    accumulator
    command = line[0]
    change = [line[1][:1], int(line[1][1:])]

    if command == "acc":
        if change[0] == "+":
            accumulator = accumulator + change[1]
        elif change[0] == "-":
            accumulator = accumulator - change[1]
    elif command == "jmp":
        print(command)
    else:
        print("Nothing")

    print(line)

print(fullCode)
print(accumulator)
