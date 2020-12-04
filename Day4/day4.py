import string

file = open("input.txt","r")
text = file.readlines()
plain_text = []
dict_text = []
tmplst=[]
list_req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
           # , "cid"] -> As per spec, country ID is ignored
category_counter = 0

correct_passports = []

def passport_requirements(req):
    switcher = {
        "byr": [1920, 2002, 4], # Year from, Year to, number of digits
        "iyr": [2010, 2020, 4],
        "eyr": [2020, 2030, 4],
        "hgt": [["cm", "in"], [150, 193], [59, 76]],
        "hcl": ["#", 6],  # Start with a # then 6 characters
        "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": [9]
    }
    return switcher.get(req, "Invalid Requirement!")

def checkPassPort(category, requirement):
    cat_details = category.split(":")
    curr_req = passport_requirements(requirement)

    if requirement == "byr" or requirement == "iyr" or requirement == "eyr":
        if len(cat_details[1]) == curr_req[2]:
            if curr_req[0] <= int(cat_details[1]) <= curr_req[1]:
                return True
            else:
                return False
        else:
            return False
    elif requirement == "hgt":
        return height_check(cat_details[1], curr_req)
    elif requirement == "pid":
        if len(cat_details[1]) == curr_req[0]:
            return True
        else:
            return False
    elif requirement == "ecl":
        for i in curr_req:
            if i == cat_details[1]:
                return True
        return False
    elif requirement == "hcl":
        if cat_details[1][:1] == curr_req[0]:
            if len(cat_details[1][1:]) == curr_req[1]:
                return all(c in string.hexdigits for c in cat_details[1][1:])
            else:
                return False
        else:
            return False
    else:
        return False


def height_check(hgt, req):
    if hgt[-2:] == 'cm':
        if req[1][0] <= int(hgt[:-2]) <= req[1][1]:
            return True
        else:
            return False
    elif hgt[-2:] == 'in':
        if req[2][0] <= int(hgt[:-2]) <= req[2][1]:
            return True
        else:
            return False
    else:
        return False


for i in text:
    tmp = i.strip()
    if tmp != '':
        tmplst.extend(tmp.split(" "))
    if tmp == '' or i == text[-1]:
        plain_text.append((tmplst))
        tmplst = []


for passport in plain_text:
    category_counter = 0
    for category in passport:
        for req in list_req:
            if req in category:
                # Split string based on :
                # Check which req
                # Follow sanity check
                if checkPassPort(category, req):
                    category_counter = category_counter + 1
    if category_counter == len(list_req):
        correct_passports.append(passport)

print("\nCorrect Passports: " + str(len(correct_passports)) + "\n")
