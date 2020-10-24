def encodeLetters(firstLetter, secondLetter):
    matrixDimensions = 5
    firstLetterCoordinates = getCharacterCoordinates(firstLetter)
    firstLetterRow = firstLetterCoordinates[0]
    firstLetterCol = firstLetterCoordinates[1]

    secondLetterCoordinates = getCharacterCoordinates(secondLetter)
    secondLetterRow = secondLetterCoordinates[0]
    secondLetterCol = secondLetterCoordinates[1]

    # Case same Col for both letters
    if firstLetterCol == secondLetterCol:
        encodedFirstLetter = theMatrix[(firstLetterRow + 1) % matrixDimensions][firstLetterCol]
        encodedSecondLetter = theMatrix[(secondLetterRow + 1) % matrixDimensions][secondLetterCol]
        return encodedFirstLetter + encodedSecondLetter

    # Case same Row for both letters
    if firstLetterRow == secondLetterRow:
        encodedFirstLetter = theMatrix[firstLetterRow][(firstLetterCol + 1) % matrixDimensions]
        encodedSecondLetter = theMatrix[secondLetterRow][(secondLetterCol + 1) % matrixDimensions]
        return encodedFirstLetter + encodedSecondLetter

    # Case different Rows and different Cols
    encodedFirstLetter = theMatrix[firstLetterRow][secondLetterCol]
    encodedSecondLetter = theMatrix[secondLetterRow][firstLetterCol]
    return encodedFirstLetter + encodedSecondLetter


# End of encodeLetters function

def getCharacterCoordinates(character):
    print("getting coordinates for ->" + character)
    searchRowIndex = 0
    for searchRow in theMatrix:
        searchColIndex = 0
        for targetLetter in searchRow:
            if (character in targetLetter) | (character == targetLetter):
                print("[searchRowIndex, searchColIndex]" + str(searchRowIndex) + "," + str(searchColIndex))
                return [searchRowIndex, searchColIndex]
            searchColIndex += 1

        searchRowIndex += 1

# end of getCharacterCoordinates function


# Initialize the alphabets list
alphabets = ["a", "b", "c", "d", "e",
             "f", "g", "h", "i/j",
             "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y",
             "z"]

# Process the key
key = "tutorials"
originalKey = key
key = key.lower()
key = "".join(dict.fromkeys(key))

# Process the plain text
plainText = "hide money"
originalPlainText = plainText
plainText = plainText.lower()
plainText = plainText.replace(" ", "")

# initialize the matrix with "0"
rowsCount, colCount = 5, 5
theMatrix = [["0" for x in range(rowsCount)] for y in range(colCount)]

# Process the key to be stored in the matrix
keyIndex = 0
alphabetsIndex = 0
for rowIndex in range(rowsCount):
    for colIndex in range(colCount):
        if keyIndex < len(key):
            #tuorials
            theMatrix[rowIndex][colIndex] = key[keyIndex]
            if (key[keyIndex] == "i") | (key[keyIndex] == "j"):
                alphabets.remove("i/j")
            else:
                alphabets.remove(key[keyIndex])
            keyIndex = keyIndex + 1
        else:
            theMatrix[rowIndex][colIndex] = alphabets[alphabetsIndex][0]
            alphabetsIndex = alphabetsIndex + 1

# Print the matrix
for rowLine in range(rowsCount):
    print(theMatrix[rowLine])

# Add any needed fillers in the plain text.
needFiller = True
plainTextIndex = 0
while plainTextIndex < len(plainText):
    if (plainTextIndex % 2 == 0) & (plainTextIndex + 1 < len(plainText)):
        if plainText[plainTextIndex] == plainText[plainTextIndex + 1]:
            plainText = plainText[:(plainTextIndex + 1)] + "x" + plainText[(plainTextIndex + 1):]
    plainTextIndex = plainTextIndex + 1

if len(plainText) % 2 == 1:
    plainText = plainText + "z"
print(plainText)

# Store the plain text into pairs
processedPlainTextPairs = []
processedPlainTextIndex = 0
while processedPlainTextIndex < len(plainText):
    processedPlainTextPairs.append(plainText[processedPlainTextIndex:processedPlainTextIndex + 2])
    processedPlainTextIndex += 2

print(processedPlainTextPairs)

# Encode the processed message pairs
encodeText = ""

for pair in processedPlainTextPairs:
    firstCharacter = pair[0]
    secondCharacter = pair[1]

    encodeText += encodeLetters(firstCharacter, secondCharacter)

print("The Encryption of [" + originalPlainText + "] Using the key [" + originalKey + "] is equals to [" + encodeText + "]")
