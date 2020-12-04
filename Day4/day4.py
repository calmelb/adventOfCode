# Required Fields:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
import ast

file = open("input.txt","r")
text = file.readlines()
plain_text = []
dict_text = []
tmplst=[]
list_req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
           # , "cid"] -> As per spec, country ID is ignored
category_counter = 0

correct_passports = []

for i in text:
    tmp = i.strip()
    if tmp != '':
        tmplst.extend(tmp.split(" "))
    if tmp == '' or i == text[-1]:
        plain_text.append((tmplst))
        tmplst = []


for passport in plain_text:
    category_counter = 0
    # print(passport)

    for category in passport:
        for req in list_req:
            if req in category:
                category_counter = category_counter + 1
    if category_counter == len(list_req):
        correct_passports.append(passport)

print(len(correct_passports))
