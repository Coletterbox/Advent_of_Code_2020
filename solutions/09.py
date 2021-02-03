import os
import queue
import collections

def IsNumberValid(num, numberDict):
    for key, value in numberDict.items():
        if (num - key) in numberDict.keys():
            if (num - key) == key and numberDict[key] <= 1:
                continue
            return True
    return False

# Find first number that doesn't obey rule of previous 25
# To do this we keep a queue and a set
# the queue tells us what the most recent values are, the set allows us to quickly check if a pair exists that sums to n
def FindFirstInvalidNumber(numList):
    numQueue = queue.Queue()
    numDict = collections.defaultdict(int)

    # Load first 25
    for x in range(0,25):
        numQueue.put(numList[x])
        numDict[numList[x]] += 1
    
    for num in numList[25:]:
        if not IsNumberValid(num, numDict):
            return num
        numQueue.put(num)
        numDict[num] += 1

        lastNum = numQueue.get()
        numDict[lastNum] -= 1
        if (numDict[lastNum] == 0):
            del numDict[lastNum]

    return -1

def FindRangeSummingToNumber(num, sequence):
    start = end = 0
    currentSum = sequence[0]

    while end < len(sequence):
        if currentSum == num:
            return (start, end)
        elif currentSum < num:
            end += 1
            currentSum += sequence[end]
        elif currentSum > num:
            currentSum -= sequence[start]
            start += 1 
    
    return (sequence[start], sequence[end])

# Returns list of ints
def ParseInput(filename):
    dataFile = open(filename, "r")    
    output = list(map(int, dataFile.readlines()))
    return output

def main():
    os.chdir(os.getcwd() + '\\solutions\\')
    numList = ParseInput("09_input.txt")
    
    # Part One 
    num = FindFirstInvalidNumber(numList)
    print(num)

    # Part Two
    start, end = FindRangeSummingToNumber(num, numList)
    subSequence = numList[start:end + 1]
    print(min(subSequence) + max(subSequence))

main()