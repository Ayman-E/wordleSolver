# Open the file in read mode
file = open("wordleSolver\wordBank.txt", "r")

# Reads the entire content of the file and puts it in a list
WBList = file.read().split()

# WBList = ['awake','awful','bacon','admin','blurt','hello','ashen','hatch','lachd']

# List of lists that we need
removeList = []
greenChar = []
greenCharIndex = []
remainingWordsScore = []
letterScore = []

# Maps letters to indices
letterMap = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}

# 6 guesses in wordle
for _ in range(6):
    # Input for the guess, lowercase
    currWord = list(input("Guess?: "))

    # Exits program
    if len(currWord) == 1:
        break
    
    # Input for the score from the guess, options are (G)reen (Y)ellow (B)lack, uppercase
    currScore = list(input("Score? G/Y/B: "))

    # Parses through each letter of the word
    for i in range(len(currWord)):
        curChar = currWord[i]
        curColor = currScore[i]

        # Green Case
        if curColor == "G":
            # Adds green character to a list to prevent issues with duplicate letters
            if curChar in greenChar:
                k = greenChar.index(curChar)
                if i != k:
                    greenChar.append(curChar)
                    greenCharIndex.append(i)
            else:
                greenChar.append(curChar)
                greenCharIndex.append(i)
            
            # Adds any words that don't have the letter in the specific spot to the remove list
            for cW in WBList:
                if cW[i] != curChar:
                    removeList.append(cW)
        elif curColor == "Y": # Yellow case
            # Adds any words that have the yellow character in the same spot to the remove list
            # Same goes for any words that don't have the character in it
            for cW in WBList:
                if cW[i] == curChar or (curChar in cW) == False:
                    removeList.append(cW)
        else: # Black case
            for cW in WBList:
                if curChar in cW:
                    if curChar in greenChar:
                        k = greenChar.index(curChar)
                        if cW[greenCharIndex[k]] != curChar:
                            removeList.append(cW)
                    else:
                        listCW = list(cW)
                        skip = True
                        for temp in range(len(listCW)):
                            if listCW[temp] == curChar and currScore[temp] != "B" and i == temp:
                                skip = False
                                break
                        if skip:
                            removeList.append(cW)

    removeList = list(set(removeList))

    for invalid in removeList:
        WBList.remove(invalid)
    removeList.clear()

    print("Remaining words " + str(WBList))

    letterScore.clear()
    for _ in range(26):
        letterScore.append(0)

    for cW in WBList:
        cWSplit = list(cW)
        for char in cWSplit:
            letterScore[letterMap.get(char)] += 1

    remainingWordsScore.clear()
    for _ in range(len(WBList)):
        remainingWordsScore.append(0)

    for l in range(len(WBList)):
        cWSplit = list(WBList[l])
        for char in cWSplit:
            remainingWordsScore[l] += letterScore[letterMap.get(char)]

    print("Recommended Word: " + WBList[remainingWordsScore.index(max(remainingWordsScore))])


#satin