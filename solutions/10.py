import os
import queue
import collections

# Takes list of adapter ratings and count all valid chains to the target
def CountAllAdapterChains(adapterList, targetJoltage, currentIndex = 0):

    possiblePaths = 0

    print("currentIndex: " + str(currentIndex))
    if (targetJoltage - adapterList[currentIndex]) <= 3:
        possiblePaths += 1

    for i in range(currentIndex + 1, currentIndex + 4):
        if (i >= len(adapterList)):
            break
        if (adapterList[i] - adapterList[currentIndex]) <= 3:
            possiblePaths += CountAllAdapterChains(adapterList, targetJoltage, i)
    
    return possiblePaths


def CountJumps(adapters):
    jumpCount = collections.defaultdict(int)
    for i in range(1,len(adapters)):
        gap = (adapters[i] - adapters[i-1])
        jumpCount[gap] += 1
    return jumpCount

# Returns list of ints
def ParseInput(filename):
    dataFile = open(filename, "r")    
    output = list(map(int, dataFile.readlines()))
    return output

def main():
    os.chdir(os.getcwd() + '\\solutions\\')
    adapterList = sorted(ParseInput("10_input.txt"))
    targetJoltage = max(adapterList) + 3

    # Part One - Find product of number of 1-jolt differences and 3-jolt differences when using all adapters
    chain = [0] + adapterList + [targetJoltage]
    jumps = CountJumps(chain)
    print(jumps[1] * jumps[3])

    # Part Two - Count all possible joltage adapter combinations
    print(CountAllAdapterChains(adapterList, targetJoltage, 0))

main()