# Open the file in read mode
file = open("wordleSolver\wordBank.txt", "r")

# Read the entire content of the file
WBList = file.read().split()
# WBList = ['awake','awful','bacon','admin','blurt','hello']
removeList = []

greenChar = []
greenCharNum = []

for _ in range(5):
    currWord = list(input("Guess?: "))

    if len(currWord) == 1:
        break
    
    currScore = list(input("Score? G/Y/B: "))


    for i in range(len(currWord)):
        curChar = currWord[i]
        curColor = currScore[i]


        if curColor == "G":
            if curChar in greenChar:
                k = greenChar.index(curChar)
                if i != k:
                    greenChar.append(curChar)
                    greenCharNum.append(i)
            else:
                greenChar.append(curChar)
                greenCharNum.append(i)

            for cW in WBList:
                if cW[i] != curChar:
                    removeList.append(cW)
        elif curColor == "Y":
            for cW in WBList:
                if cW[i] == curChar or (curChar in cW) == False:
                    removeList.append(cW)
        else:
            for cW in WBList:
                if curChar in cW:
                    if curChar in greenChar:
                        k = greenChar.index(curChar)
                        if cW[greenCharNum[k]] != curChar:
                            removeList.append(cW)
                    else:
                        removeList.append(cW)

    removeList = list(set(removeList))

    for invalid in removeList:
        WBList.remove(invalid)
    removeList.clear()

    print("Remaining words " + str(WBList))

