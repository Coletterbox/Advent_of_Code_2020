import os

def FindRepeatInstruction(instructions):
    accum = 0
    previousLine = 0
    currentLine = 0
    visitedLines = set()
    
    while currentLine not in visitedLines and currentLine != len(instructions):
        previousLine = currentLine
        visitedLines.add(currentLine)
        currentInstruction = instructions[currentLine]["instruction"]
        currentValue = instructions[currentLine]["count"]

        if currentInstruction == "nop":
            currentLine += 1

        elif currentInstruction == "acc":
            accum += currentValue
            currentLine += 1
        
        elif currentInstruction == "jmp":
            currentLine += currentValue

    return (accum, previousLine, currentLine < len(instructions))


def TryRepairInstructions(instructions):
    newInstructions = instructions.copy()
    for x in range(0,len(newInstructions)):
        if newInstructions[x]["instruction"] == "jmp":
            newInstructions[x]["instruction"] = "nop"
            test = FindRepeatInstruction(newInstructions)
            if (not test[2]):
                return test[0]
            newInstructions[x]["instruction"] = "jmp"

        elif newInstructions[x]["instruction"] == "nop" and newInstructions[x]["count"] != 0:
            newInstructions[x]["instruction"] = "jmp"
            test = FindRepeatInstruction(newInstructions)
            if not test[2]:
                return test[0]
            newInstructions[x]["instruction"] = "nop"

# Returns list of 2-tuples of instruction and their associated count
def ParseInput(filename):
    dataFile = open(filename, "r")    
    output = []
    for line in dataFile:
        instruction = line[0:3]
        count = int(line[3:])
        output.append({"instruction": instruction, "count" : count})
    
    return output

def main():
    os.chdir(os.getcwd() + '\\solutions\\')
    instructionList = ParseInput("08_input.txt")

    print(TryRepairInstructions(instructionList))

main()