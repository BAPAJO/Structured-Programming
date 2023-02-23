numChar = 0
numVow = 0
numCon = 0
numNotLetter = 0

fo = open("Chapter 8 - readme_English.txt", "r")
while True:
    data = fo.read(1)
    # numChar
    numChar += 1

    # numVow
    if data.upper() in ['A', 'I', 'U', 'E', 'O']:
        numVow += 1

    # numCon
    if data.upper() in ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']:
        numCon += 1
    
    if not data:
        break

# numNotLetter
numNotLetter = numChar - (numCon + numVow)

print(numChar)
print(numVow)
print(numCon)
print(numNotLetter)