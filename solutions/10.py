import os
import queue
import collections

# Takes list of adapter ratings and builds a valid chain to the target
# Recap: a valid chain is a list of joltages where each joltage has a difference of no more than three from the previous joltage
def BuildAdapterChain(adapters, target):
    chain = []
    currentJoltage = 0
    while currentJoltage != targetJoltage

# Returns list of ints
def ParseInput(filename):
    dataFile = open(filename, "r")    
    output = list(map(int, dataFile.readlines()))
    return output

def main():
    os.chdir(os.getcwd())
    numList = ParseInput("10_input.txt")
    targetJoltage = max(numList) + 3

    # Part One - Find product of number of 1-jolt differences and 3-jolt differences. 


main()