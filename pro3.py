# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math

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

print(getPrimeFactors(13195))
# print(getPrimeFactors(600851475143)) # 8 minutes
