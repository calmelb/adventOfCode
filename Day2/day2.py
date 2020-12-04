file = open("input.txt","r")
text = file.readlines()
plain_text = []
met = []
for i in text:
    tmp = i.strip()
    plain_text.append((tmp.split(":")))

for pw in plain_text:
    count = []


    char1 = pw[0].split(" ")[1]
    count = (pw[0].split(" ")[0].split("-"))
    count_char = str(pw[1].count(char1))


    if int(count[0]) <= int(count_char) and int(count_char) <= int(count[1]):
        print("Password: " + pw[1] + " ,Requirements: " + pw[0])
        print("Count of Character: " + count_char)
        met.append(pw)

print(len(met))

