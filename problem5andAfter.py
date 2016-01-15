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
    import re
    return list(map(int,re.findall('\w',stringifiedNumber)))

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
    for lessRowsGrid in iter(getRowWiseIterator(numberOfAdjacents,grid),None):
        for lessRowsAndLessColumnsGrid in iter(getColumnWiseIterator(numberOfAdjacents,lessRowsGrid),None):
            action(lessRowsAndLessColumnsGrid)
    return True

def getGrid(stringGrid):
    return list(map(lambda stringLine: list(map(int,stringLine.split())),stringGrid.splitlines()))

# def getRowWiseIterator(numberOfRowsAtATime,grid):
#     startingIndex=0
#     def iterator():
#         nonlocal startingIndex
#         rowLevelSelection=grid[startingIndex:startingIndex+numberOfRowsAtATime]
#         if(len(rowLevelSelection)!=numberOfRowsAtATime): return None
#         startingIndex+=1
#         return rowLevelSelection
#     return iterator
def getRowWiseIterator(numberOfRowsAtATime,grid):
    startingIndex=0
    def infiniteIterator():
        nonlocal startingIndex
        rowLevelSelection=grid[startingIndex:startingIndex+numberOfRowsAtATime]
        startingIndex+=1
        return rowLevelSelection
    def toBeHalted(rowLevelSelection):
        return len(rowLevelSelection)!=numberOfRowsAtATime
    return generateIterator(infiniteIterator,toBeHalted)

# def getColumnWiseIterator(numberOfColumnsAtATime,grid):
#     startingIndex=0
#     def iterator():
#         nonlocal startingIndex
#         selector=lambda row:row[startingIndex:startingIndex+numberOfColumnsAtATime]
#         columnLevelSelection=list(map(selector,grid))
#         if(any(map(lambda row:len(row)!=numberOfColumnsAtATime,columnLevelSelection))): return None
#         startingIndex+=1
#         return columnLevelSelection
#     return iterator
#
def getColumnWiseIterator(numberOfColumnsAtATime,grid):
    startingIndex=0
    def infiniteIterator():
        nonlocal startingIndex
        selector=lambda row:row[startingIndex:startingIndex+numberOfColumnsAtATime]
        columnLevelSelection=list(map(selector,grid))
        startingIndex+=1
        return columnLevelSelection

    def toBeHalted(columnLevelSelection):
        return any(map(lambda row:len(row)!=numberOfColumnsAtATime,columnLevelSelection))

    return generateIterator(infiniteIterator,toBeHalted)

def generateIterator(infiniteSequenceGenerator,toBeHalted):
    def iterator():
        next=infiniteSequenceGenerator()
        return None if (toBeHalted(next)==True) else next
    return iterator
#############
def pro12():
    print("problem 12")
    print(getTraingleNumberWhoHasOver500Divisors())
    # print(len(getAllFactors(76564125)))
    # print(len(getAllFactors(76576500)))

def getTraingleNumberWhoHasOver500Divisors():
    trianlgeNumber=1
    allFactors=[]
    getNextTriangleNumber=getInfiterTriangleNumberSeriesIterator()
    while(len(allFactors)<500):
        trianlgeNumber=getNextTriangleNumber()
        allFactors=getAllFactors(trianlgeNumber)
    return trianlgeNumber

def getInfiterTriangleNumberSeriesIterator():
    startingIndex=0
    triangleNumber=0
    def infiniteIterator():
        nonlocal startingIndex,triangleNumber
        startingIndex+=1
        triangleNumber+=startingIndex
        return triangleNumber
    return infiniteIterator

def getAllFactors(targetNumber):
    upperLimit=targetNumber
    divisor=1
    allFactors=[]
    while(divisor<upperLimit):
        if(divisibleBy(targetNumber,divisor)):
            upperLimit=targetNumber/divisor
            allFactors.append(divisor)
            if(divisor<upperLimit): allFactors.append(upperLimit)
        divisor+=1
    return allFactors

##################
def pro13():
    print("problem 13")
    print(getFirstTenDigitsOfTheSumOfAllNumbers("37107287533902102798797998220837590246510135740250\n46376937677490009712648124896970078050417018260538\n74324986199524741059474233309513058123726617309629\n91942213363574161572522430563301811072406154908250\n23067588207539346171171980310421047513778063246676\n89261670696623633820136378418383684178734361726757\n28112879812849979408065481931592621691275889832738\n44274228917432520321923589422876796487670272189318\n47451445736001306439091167216856844588711603153276\n70386486105843025439939619828917593665686757934951\n62176457141856560629502157223196586755079324193331\n64906352462741904929101432445813822663347944758178\n92575867718337217661963751590579239728245598838407\n58203565325359399008402633568948830189458628227828\n80181199384826282014278194139940567587151170094390\n35398664372827112653829987240784473053190104293586\n86515506006295864861532075273371959191420517255829\n71693888707715466499115593487603532921714970056938\n54370070576826684624621495650076471787294438377604\n53282654108756828443191190634694037855217779295145\n36123272525000296071075082563815656710885258350721\n45876576172410976447339110607218265236877223636045\n17423706905851860660448207621209813287860733969412\n81142660418086830619328460811191061556940512689692\n51934325451728388641918047049293215058642563049483\n62467221648435076201727918039944693004732956340691\n15732444386908125794514089057706229429197107928209\n55037687525678773091862540744969844508330393682126\n18336384825330154686196124348767681297534375946515\n80386287592878490201521685554828717201219257766954\n78182833757993103614740356856449095527097864797581\n16726320100436897842553539920931837441497806860984\n48403098129077791799088218795327364475675590848030\n87086987551392711854517078544161852424320693150332\n59959406895756536782107074926966537676326235447210\n69793950679652694742597709739166693763042633987085\n41052684708299085211399427365734116182760315001271\n65378607361501080857009149939512557028198746004375\n35829035317434717326932123578154982629742552737307\n94953759765105305946966067683156574377167401875275\n88902802571733229619176668713819931811048770190271\n25267680276078003013678680992525463401061632866526\n36270218540497705585629946580636237993140746255962\n24074486908231174977792365466257246923322810917141\n91430288197103288597806669760892938638285025333403\n34413065578016127815921815005561868836468420090470\n23053081172816430487623791969842487255036638784583\n11487696932154902810424020138335124462181441773470\n63783299490636259666498587618221225225512486764533\n67720186971698544312419572409913959008952310058822\n95548255300263520781532296796249481641953868218774\n76085327132285723110424803456124867697064507995236\n37774242535411291684276865538926205024910326572967\n23701913275725675285653248258265463092207058596522\n29798860272258331913126375147341994889534765745501\n18495701454879288984856827726077713721403798879715\n38298203783031473527721580348144513491373226651381\n34829543829199918180278916522431027392251122869539\n40957953066405232632538044100059654939159879593635\n29746152185502371307642255121183693803580388584903\n41698116222072977186158236678424689157993532961922\n62467957194401269043877107275048102390895523597457\n23189706772547915061505504953922979530901129967519\n86188088225875314529584099251203829009407770775672\n11306739708304724483816533873502340845647058077308\n82959174767140363198008187129011875491310547126581\n97623331044818386269515456334926366572897563400500\n42846280183517070527831839425882145521227251250327\n55121603546981200581762165212827652751691296897789\n32238195734329339946437501907836945765883352399886\n75506164965184775180738168837861091527357929701337\n62177842752192623401942399639168044983993173312731\n32924185707147349566916674687634660915035914677504\n99518671430235219628894890102423325116913619626622\n73267460800591547471830798392868535206946944540724\n76841822524674417161514036427982273348055556214818\n97142617910342598647204516893989422179826088076852\n87783646182799346313767754307809363333018982642090\n10848802521674670883215120185883543223812876952786\n71329612474782464538636993009049310363619763878039\n62184073572399794223406235393808339651327408011116\n66627891981488087797941876876144230030984490851411\n60661826293682836764744779239180335110989069790714\n85786944089552990653640447425576083659976645795096\n66024396409905389607120198219976047599490197230297\n64913982680032973156037120041377903785566085089252\n16730939319872750275468906903707539413042652315011\n94809377245048795150954100921645863754710598436791\n78639167021187492431995700641917969777599028300699\n15368713711936614952811305876380278410754449733078\n40789923115535562561142322423255033685442488917353\n44889911501440648020369068063960672322193204149535\n41503128880339536053299340368006977710650566631954\n81234880673210146739058568557934581403627822703280\n82616570773948327592232845941706525094512325230608\n22918802058777319719839450180888072429661980811197\n77158542502016545090413245809786882778948721859617\n72107838435069186155435662884062257473692284509516\n20849603980134001723930671666823555245252804609722\n53503534226472524250874054075591789781264330331690\n"))
    print("answer : 5537376230")
#     print(getFirstTenDigitsOfTheSumOfAllNumbers("3710728\n\
# 3710728\n\
# 3999728\n\
# 3710999\n\
# 5789750\n\
# 4992997\n\
# 5941799"))

def generateGrid(stringGrid,rowSelector,columnSelector,mapper):
    import re
    rows = re.findall(rowSelector,stringGrid)
    return list(map(lambda row:list(map(mapper,re.findall(columnSelector,row))),rows))

def getFirstTenDigitsOfTheSumOfAllNumbers(stringGrid):
    import re
    numbers = re.findall('\d+',stringGrid)
    numberOfDigitsToBeFound = 10
    biggestSingleDigit = 9
    numberOfDigitsForPresicion = len(str(len(numbers)*biggestSingleDigit))
    totalDigitsToBeFound = numberOfDigitsToBeFound + numberOfDigitsForPresicion

    sumationFound=0
    for digitIndex in range(len(numbers[0])):
        sumationFound = sumationFound * 10 + sum(list(map(lambda row: int(row[digitIndex]),numbers)))
        if(len(str(sumationFound))>=totalDigitsToBeFound):
            break
    result = str(sumationFound)[0:numberOfDigitsToBeFound]
    return result
pro13()
# pro12()
# pro11()
# pro10()
# pro9()
# pro8()
# pro7()
# pro6()
# pro5()
# pro3()
