# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math
from functools import reduce
primes = [2,3,5]

def isDivisibleByAnyOneOfTheKnownPrimes (targetNumber):
    for prime in primes:
        if targetNumber%prime==0:
            return True

def isKnownPrime(targetNumber):
    return targetNumber in primes

def isPrime (targetNumber):
    if(isKnownPrime(targetNumber)):
        return True
    if(_is(targetNumber)(divisibleByAnyOneOfTheKnownPrimes)):
        return False
    limit = getMaxFactorLimit(targetNumber)
    divider=getLast(primes)
    while divider <=limit:
        if(targetNumber%divider==0):
            return False
        divider=getNextPrime(divider)
    return True

def _is(element):
    return lambda hasQuality:hasQuality(element)

def divisibleByAnyOneOfTheKnownPrimes(element):
    return isDivisibleByAnyOneOfTheKnownPrimes(element)

def getMaxFactorLimit(targetNumber):
    return math.ceil(targetNumber**0.5)

def getLast(primes):
    return primes[len(primes)-1]

def getNextPrime (prime):
    if(prime == 2): return 3
    nextOddNumber=prime+2
    while isPrime(nextOddNumber)==False:
        nextOddNumber+=2
    primes.append(nextOddNumber)
    return nextOddNumber

def getAListOfPrimesLessThan(maxLimit):
    listOfPrimes=[2,3,5]
    nextPrime=getNextPrime(getLast(listOfPrimes))
    while nextPrime<maxLimit:
        listOfPrimes.append(nextPrime)
        nextPrime=getNextPrime(nextPrime)
    return listOfPrimes

def getFirstnPrimes (n):
    listOfPrimes=[2,3,5]
    nextPrime=getLast(listOfPrimes)
    for index in range(n-3):
        nextPrime=getNextPrime(nextPrime)
        listOfPrimes.append(nextPrime)
    return listOfPrimes

def getPrimeFactors(targetNumber):
    factorCandidates = getAListOfPrimesLessThan(getMaxFactorLimit(targetNumber))
    factors=[]
    for factorCandidate in factorCandidates:
        if(targetNumber%factorCandidate==0):
            factors.append(factorCandidate)
    return factors

def pro3():
    print('problem 3')
    print(getPrimeFactors(13195))
    print(getPrimeFactors(600851475143)) # 8 minutes

####################
def pro5 ():
    print('problem 5')
    print('theLeastCommonMultipleOf(first(10)(naturalNumbers)))',
    theLeastCommonMultipleOf(first(10)(naturalNumbers)))
    print('theLeastCommonMultipleOf(first(20)(naturalNumbers)))',
    theLeastCommonMultipleOf(first(20)(naturalNumbers)))

def theLeastCommonMultipleOf (factors):
    lCM=theProductOf(factors)
    for factor in factors:
        isMagicWorking= lambda magicalNumber : isCommonMultiple(magicalNumber,factors)
        lCM=magic(lCM,factor,isMagicWorking)
    return (int)(lCM)

def first(n):
    return lambda series: series(n)

def naturalNumbers(upto):
    return list(range(1,upto+1))

def theProductOf(listOfNumbers):
    product=1
    for number in listOfNumbers:
        product*=number
    return product

def magic(lCM,factor,isCool):
    magicalNumber=lCM/factor
    if(factor>1 and divisibleBy(lCM,factor) and isCool(magicalNumber)):
        return magic(magicalNumber,factor,isCool)
    return lCM;

def divisibleBy(product,factor):
    return product%factor==0

def isCommonMultiple(product,factors):
    for factor in factors:
        if(not(divisibleBy(product,factor))):
            return False
    return True

################
def pro6():
    print('problem 6')
    print('theDifferenceBetween(theSumOf(theSquaresOf(theFirst(10)(naturalNumbers))), theSquareOf(theSumOf(theFirst(10)(naturalNumbers))))) ',
    theDifferenceBetween(theSumOf(theSquaresOf(theFirst(10)(naturalNumbers))), theSquareOf(theSumOf(theFirst(10)(naturalNumbers)))))
    print('theDifferenceBetween(theSumOf(theSquaresOf(theFirst(100)(naturalNumbers))), theSquareOf(theSumOf(theFirst(100)(naturalNumbers))))) ',
    theDifferenceBetween(theSumOf(theSquaresOf(theFirst(100)(naturalNumbers))), theSquareOf(theSumOf(theFirst(100)(naturalNumbers)))))

def theFirst(n):
    return first(n)

def theDifferenceBetween(a,b):

    if(a>b): return a-b
    return b-a

def theSumOf(numbers):
    return sum(numbers)

def theSquaresOf(numbers):
    return map(theSquareOf,numbers)

def theSquareOf(n):
    return n**2

################
def pro7():
    print('problem 7')
    print('the6thPrimeis',getFirstnPrimes(6)[5])
    print('the10001stPrimeis',getFirstnPrimes(10001)[10000])

###############
def pro8():
    print('problem 8')
    # print('theGreatestOf(theProductOfEvery(listOfAllPossible(frameOf(4,adjacentNumbers),(theDigitsOf(
    # 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450\
    # )))))')

    print(theGreatestOf(theProductOfEvery(listOfAllPossible(frameOf(4,adjacentNumbers),(theDigitsOf(
    '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    ))))))

    print(theGreatestOf(theProductOfEvery(listOfAllPossible(frameOf(13,adjacentNumbers),(theDigitsOf(
    '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    ))))))

def theGreatestOf(listOfNumbers):
    return max(list(listOfNumbers))

def theProductOfEvery(listsOfLists):
    return map(theProductOf,listsOfLists)

def listOfAllPossible(selector,listOfNumbers):
    listOfAllPossibleSubLists=[]
    for index in range(len(listOfNumbers)):
        listOfAllPossibleSubLists.append(selector(index,listOfNumbers))
    return listOfAllPossibleSubLists

def frameOf(numberOfNumbers,frameSelector):
    return lambda startingIndex, listOfNumbers: frameSelector(startingIndex,numberOfNumbers,listOfNumbers)

def adjacentNumbers(startingIndex,numberOfNumbers,listOfNumbers):
    return list(listOfNumbers)[startingIndex:startingIndex+numberOfNumbers]

def theDigitsOf(stringifiedNumber):
    theDigits=[]
    for digit in stringifiedNumber:
        theDigits.append((int)(digit))
    return theDigits

################
def getThePythagoreanTripletWhosSumIs1000():
    sum=1000
    maxLimit=math.ceil(sum/3)
    for a in list(range(1,maxLimit)):
        for b in list(range(a+1,sum)):
            c=(a**2+b**2)**0.5
            if a+b+c==1000:
                return a*b*c

def pro9():
    print('problem 9')
    print(getThePythagoreanTripletWhosSumIs1000())

################
def pro10():
    print('problem 10')
    print(sumOfAllPrimesLessThan(10)) #17
    print(sumOfAllPrimesLessThan(2000000)) #142913828922

def sumOfAllPrimesLessThan(lessThan):
    sum=0
    nextPrime=2
    while nextPrime<lessThan:
        if(nextPrime>1000000): print(nextPrime,sum)
        sum+=nextPrime
        nextPrime=getNextPrime(nextPrime)
    return sum

#################
def pro11():
    print('problem 11')
    print(getGreatestProductOfAny4adjacentsInAnyDirectionInALine('08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n\
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n\
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n\
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n\
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n\
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n\
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n\
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n\
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n\
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n\
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n\
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n\
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n\
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n\
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n\
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n\
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n\
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n\
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n\
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48',4))
    print(getGreatestProductOfAny4adjacentsInAnyDirectionInALine(
    '08 02 22\n\
    97 38 15\n\
    00 40 00\n',2))

def getGreatestProductOfAny4adjacentsInAnyDirectionInALine(stringGrid,numberOfAdjacents):
    theGreatestProduct=0
    def findTheGreatestProduct(selectedMatrix):
        nonlocal theGreatestProduct
        productOfTheMatrix=getTheProductOfTheMatrix(selectedMatrix)
        if(productOfTheMatrix > theGreatestProduct):
            theGreatestProduct = productOfTheMatrix
    iterateGrid(getGrid(stringGrid),findTheGreatestProduct,numberOfAdjacents)
    return theGreatestProduct

def getTheProductOfTheMatrix(matrix):
    allPossibleAdjacents = flatten([getRows(matrix),getColumns(matrix),getDiagonals(matrix)])
    return max(map(product,allPossibleAdjacents))

def getRows(matrix):
    return matrix

def getColumns(matrix):
    if(len(matrix)==0): return []
    return [[row[columnIndex] for row in matrix] for columnIndex in range(len(matrix[0]))]

def getDiagonals(squareMatrix):
    size=len(squareMatrix)
    leftTopToRightBottom = [squareMatrix[index][index] for index in range(size)]
    rightTopToLeftBottom = [squareMatrix[index][size-index-1] for index in range(size)]
    return [leftTopToRightBottom,rightTopToLeftBottom]

def flatten(listOfLists):
    flattened=[]
    for aList in listOfLists: flattened.extend(aList)
    return flattened

def product(listOfNumbers):
    return reduce(lambda x, y: x*y,listOfNumbers)

def iterateGrid(grid,action,numberOfAdjacents):
    for lessRowsGrid in iter(selectAdjacentRows(numberOfAdjacents,grid),None):
        for lessRowsAndLessColumnsGrid in iter(selectAdjacentColumns(numberOfAdjacents,lessRowsGrid),None):
            action(lessRowsAndLessColumnsGrid)
    return True

def getGrid(stringGrid):
    return list(map(lambda stringLine: list(map(int,stringLine.split())),stringGrid.splitlines()))

def selectAdjacentRows(numberOfAdjacents,grid):
    startingIndex=0
    def iterator():
        nonlocal startingIndex
        selectedAdjacents=grid[startingIndex:startingIndex+numberOfAdjacents]
        if(len(selectedAdjacents)!=numberOfAdjacents): return None
        startingIndex+=1
        return selectedAdjacents
    return iterator

def selectAdjacentColumns(numberOfAdjacents,grid):
    startingIndex=0
    def iterator():
        nonlocal startingIndex
        selector=lambda row:row[startingIndex:startingIndex+numberOfAdjacents]
        columnLevelSelection=list(map(selector,grid))
        if(any(map(lambda row:len(row)!=numberOfAdjacents,columnLevelSelection))): return None
        startingIndex+=1
        return columnLevelSelection
    return iterator

pro11()
# pro10()
# pro9()
# pro8()
# pro7()
# pro6()
# pro5()
# pro3()
