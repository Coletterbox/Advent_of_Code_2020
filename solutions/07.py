# Not even going to bother putting the whole problem statement here from now on....

# TL;DR: it's a breadth-first search

import os
import math
import collections
import re
import queue

# Given a starting bag, find how many bags nest within it
def CountNestedBags(startbag, bagMapping):
    visitedBags = set()
    pendingVisits = queue.Queue()

    found = 0

    for bag in bagMapping[startbag]:
        for x in range(bag["count"]):
            pendingVisits.put(bag["colour"])
        found += bag["count"]

    while (not pendingVisits.empty()):
        currentBag = pendingVisits.get()
        visitedBags.add(currentBag)
        for bag in bagMapping[currentBag]:
            for x in range(bag["count"]):
                pendingVisits.put(bag["colour"])
            found += bag["count"]
    
    return found


# Given one starting bag and our target bag, find if we can reach the target bag from the start bag
def CanReachBagFromStart(startbag, endbag, bagMapping):
    visitedBags = set()
    pendingVisits = queue.Queue()

    visitedBags.add(startbag)
    for bag in bagMapping[startbag]:
        pendingVisits.put(bag["colour"])
    
    while (not pendingVisits.empty()):
        currentBag = pendingVisits.get()
        if currentBag == endbag: 
            return True
        
        visitedBags.add(currentBag)
        for bag in bagMapping[currentBag]:
            if bag["colour"] not in visitedBags:
                pendingVisits.put(bag["colour"])
    
    return False

# Given a target bag and our dictionary of bags, find how many ways we can reach that bag.
def ReachableBags(targetbag, mapping):
    count = 0
    for key in mapping.keys():
        if CanReachBagFromStart(key, targetbag, mapping):
            count += 1
    
    return count

# Returns a dictionary mapping bag colours to lists of bag colours
def ParseInput(filename):
    dataFile = open(filename, "r")
    mapping = dict()

    for line in dataFile:
        
        parsedLine = re.sub("(no other)|(bag(s?))|\.|\n| ", "", line.replace("contain", ","))
        colours = parsedLine.split(",")
        if "" in colours:
            colours.remove("")
        
        bagCounts = []
        for col in colours[1:]:
            bagCounts.append({"count":int(col[0]), "colour":col[1:]})

        mapping[colours[0]] = bagCounts
        
    return mapping    

def main():
    
    os.chdir(os.getcwd() + '\\solutions\\')
    bagMappings = ParseInput("07_input.txt")

    #Part 1
    print(ReachableBags("shinygold",bagMappings))

    #Part 2
    print(CountNestedBags("shinygold", bagMappings))

main()