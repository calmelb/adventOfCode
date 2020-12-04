file = open("input.txt","r")
numbers = file.readlines()
plain_num = []
for i in numbers:
    plain_num.append(i.strip())

for num1 in plain_num:
    for num2 in plain_num:
        for num3 in plain_num:
            if (int(num1) + int(num2) + int(num3)) == 2020:
                print("Number 1: " +num1)
                print("Number 2: " + num2)
                print("Number 3:" + num3)
                print("Multiplied: "+ str(int(num1) * int(num2) * int(num3)))

# for i in range(,len(plain_num)):
#     if i != 0:
#         if (int(plain_num[i-1])+ int(plain_num[i]) == 2020):
#             print("Number 1: " + plain_num[i-1])
#             print("Number 2: " + plain_num[i])

file.close()