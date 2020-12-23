#You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

#You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

#Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

#The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

import os
import math

PLANE_ROWS = 127
PLANE_COLS = 7

# Abstractifies both finding rows and finding columns
# Instructions is your char sequence
# range is either 128 or 7 (see above)
# lowerchar and higherchar are the chars that make you go towards the lower or upper half of your remaining range
def BinarySearch(instructions, rangebottom, rangetop, lowerChar, upperChar):
    upper = rangetop
    lower = rangebottom
    lastChar = ""
    for char in instructions:

        if char != lowerChar and char != upperChar:
            continue
        diff = (upper-lower)/2
        if char == upperChar:
            lower = math.ceil(lower + diff)
        if char == lowerChar:
            upper = math.floor(upper - diff)

        lastChar = char
    
    if lastChar == lowerChar:
        return int(lower)
    else:
        return int(upper)

def GetPassRow(boardingPass):
    return BinarySearch(boardingPass, 0, PLANE_ROWS, "F", "B")

def GetPassCol(boardingPass):
    return BinarySearch(boardingPass, 0, PLANE_COLS, "L", "R")

def GetBoardingPassID(boardingPass):
    return (GetPassRow(boardingPass) * 8) + GetPassCol(boardingPass)

def GetLargestBoardingPassID(boardingPassList):
    largest = 0
    for bpass in boardingPassList:
        if GetBoardingPassID(bpass) > largest:
            largest = GetBoardingPassID(bpass)
    return largest

    
def FindMissingID(boardingPassList):
    minID = 8
    maxID = 1016
    boardingPassIDs = list(map(GetBoardingPassID, boardingPassList))

    for x in range(minID, maxID):
        if x not in boardingPassIDs:
            return x


def ParseInput(filename):
    dataFile = open(filename, "r")
    result = dataFile.readlines()

    return result

def main():
    
    os.chdir(os.getcwd() + '\\solutions\\')
    seatData = ParseInput("05_input.txt")

    #Part 1 Solution
    print(GetLargestBoardingPassID(seatData))

    #Part 2 Solution
    print(FindMissingID(seatData))


main()