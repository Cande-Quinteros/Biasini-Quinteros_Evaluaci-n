def convertInputString():
    rawInput = input("Por favor ingrese una palabra, frase u oración \ para verificar si es un palíndromo: ")
    rawString = rawInput.lower()
    rawList = list(rawString)
    return rawList

def stripAnalphabetics(dirtyList):
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    for character in analphabeticList:
        if character in dirtyList:
            dirtyList.remove(character)
            return stripAnalphabetics(dirtyList)
    return dirtyList

def ejemplo(frase):
    cont = 0
    for ca in frase:
        print(f"{ca} ", end=" ")
        cont = cont +1
    print(cont)

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1]
    if reversedList == straightList:
        print("¡El texto que ha introducido es un palíndromo!")
    else:
        print("El texto que ha introducido no es un palíndromo.")

def main():
    print("Comprobador de palíndromos")
    originalList = convertInputString()
    originalList = stripAnalphabetics(originalList)
    ejemplo(originalList)
    runPalindromeCheck(originalList)

main()
