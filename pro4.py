def stringReverse (sourceString):
    index=len(sourceString)-1
    reversedString=''

    while(-1<index):
        reversedString+=sourceString[index]
        index-=1

    return reversedString

def isPalindrome (sourceString):
    lengthOfString=len(sourceString)
    for index in range((int)(lengthOfString/2)):
        matchingCharacterIndex=lengthOfString-1-index
        if(sourceString[index]!=sourceString[matchingCharacterIndex]):
            return False
    return True

def gatAListOfPalindromeOfDigits (numberOfFactorDigits):
    ceilingLimit=10**numberOfFactorDigits
    floorLimit=10**(numberOfFactorDigits-1)
    factor1=ceilingLimit-1
    factor2=ceilingLimit-1

    allPalidromes=[]
    while(floorLimit<=factor1<ceilingLimit):
        while(floorLimit<=factor2<ceilingLimit):
            product=factor1*factor2
            if(isPalindrome(str(product))):
                allPalidromes.append(product)
            factor2-=1
        factor2=ceilingLimit-1
        factor1-=1
    return allPalidromes

print (max(gatAListOfPalindromeOfDigits(1)))
print (max(gatAListOfPalindromeOfDigits(2)))
print (max(gatAListOfPalindromeOfDigits(3)))
