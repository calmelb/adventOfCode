file = open("input.txt","r")
text = file.readlines()
plain_text = []
met = []
for i in text:
    tmp = i.strip()
    plain_text.append((tmp.split(":")))

for pw in plain_text:
    char1 = pw[0].split(" ")[1]
    count = (pw[0].split(" ")[0].split("-"))
    count_char = str(pw[1].count(char1))
    binary_flag = 0
    pwWord = pw[1].strip()
    #
    # print(pw[1])
    # print(pw[1][int(count[0])+1])

    # print(pwWord)
    # print(len(pw[1]))
    # print(len(pwWord))
    # if int(count[1]) == len()

    if pwWord[int(count[0])-1] == char1:
        binary_flag = binary_flag + 1

    if pwWord[int(count[1])-1] == char1:
        binary_flag = binary_flag + 1



    # print(binary_flag)

    if binary_flag == 1:
        met.append(pw)
        print("Password: " + pwWord + ", Requirements: " + pw[0] + ", Binary: "+str(binary_flag))

    ## Part 1
    # if int(count[0]) <= int(count_char) and int(count_char) <= int(count[1]):
    #     print("Password: " + pw[1] + " ,Requirements: " + pw[0])
    #     print("Count of Character: " + count_char)
    #     met.append(pw)

print(len(met))

