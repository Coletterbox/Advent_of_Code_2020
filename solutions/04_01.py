# The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.
# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:
# Part 2
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

import os

def IsValidEyeColour(string):
    validCols = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return string in validCols

def IsValidHex(code):

    charSet = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}

    if len(code) != 7:
        return False
    if code[0] != '#':
        return False
    for char in code[1:len(code)]:
        if char not in charSet:
            return False 
    return True

def IsNumber(string):
    if len(string) == 0:
        return False
    if string[0] == '0' and len(string) > 0:
        return False
    for char in string:
        if not char.isdigit():
            return False
    return True

def IsDigitSequence(string):
    if len(string) == 0:
        return False
    for char in string:
        if not char.isdigit():
            return False
    return True

def IsNumberInRange(num, min, max):
    return num >= min and num <= max

def StripZeroes(num):
    output = ""
    start = False
    for char in num:
        if int(char) > 0 or start:
            output += char
            start = True
    return output

# Very clumsily-architected solution because I don't have the willpower to do something more generalised 
def ValidateDataField(datafield, contents):
    if datafield == "byr":
        return IsNumber(contents) and IsNumberInRange(int(contents), 1920, 2002)
    
    if datafield == "iyr":
        return IsNumber(contents) and IsNumberInRange(int(contents), 2010, 2020)
    
    if datafield == "eyr":
        return IsNumber(contents) and IsNumberInRange(int(contents), 2020, 2030)

    if datafield == "hgt":
        
        value = contents[0:len(contents) - 2]
        if not IsNumber(value):
            return False
        if "cm" in contents:
            return IsNumberInRange(int(value), 150, 193)
        elif "in" in contents:
            return IsNumberInRange(int(value), 59, 76)
        else:
            return False

    if datafield == "hcl":
        return IsValidHex(contents)
    
    if datafield == "ecl":
        return IsValidEyeColour(contents)

    if datafield == "pid":
        return IsDigitSequence(contents) and len(contents) == 9    
        
    return False

def ParseDataField(field):
    return field.split(':')

def ValidatePassport(passportdata, requiredfields):
    for field in passportdata:
        parsedField = ParseDataField(field)
        if parsedField[0] in requiredfields:
            if not ValidateDataField(parsedField[0], parsedField[1]):
                return False
    return True

def ParsePassportData(filename: str):
    dataFile = open(filename, "r")
    fileAsString = ""
    for line in dataFile:
        fileAsString += line
    
    passportStrings = fileAsString.split("\n\n")
    
    for passport in passportData

    return passportData

def main():
    os.chdir('C:\\Users\\benfc\\Documents\\GitHub\\Advent_of_Code_2020\\solutions\\')
    requiredPassportFields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    ]

    validPassports = 0
    passportData = ParsePassportData("04_input.txt")
    #passportData = ParsePassportData("04_test.txt")
    for passport in passportData:
        if (ValidatePassport(passport, requiredPassportFields)):
            validPassports += 1
    return validPassports

print(main())
