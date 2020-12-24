# Not even going to bother putting the whole problem statement here...

import os
import math
import collections

# Take list of strings representing a group's customs entries, return unique char count
def CountGroup(group):
    seenChars = set()
    for line in group:
        for char in line:
            seenChars.add(char)

    return len(seenChars)

def SumGroupCounts(groups):
    return sum(list(map(CountGroup, groups)))


def CountGroupPartTwo(group):
    requiredCount = len(group)
    seenChars = collections.defaultdict(int)

    for line in group:
        for char in line:
                seenChars[char] += 1

    result = 0
    for key, value in seenChars.items():
        if value == requiredCount:
            result += 1
    return result

def SumGroupCountsPartTwo(groups):
    results = list(map(CountGroupPartTwo, groups))
    return sum(results)

# Returns a list of lists of strings (i.e. a list of groups)
def ParseInput(filename):
    dataFile = open(filename, "r")
    dataAsString = ""
    for line in dataFile:
        dataAsString += line

    groupLists = []
    
    for string in dataAsString.split("\n\n"):
        groupLists.append(string.split("\n"))

    print(groupLists[len(groupLists)-1])
    return groupLists
        

def main():
    
    os.chdir(os.getcwd() + '\\solutions\\')
    groups = ParseInput("06_input.txt")

    print(SumGroupCounts(groups))
    print(SumGroupCountsPartTwo(groups))

main()