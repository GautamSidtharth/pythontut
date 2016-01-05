nMinus1thTerm=1
nMinus2thTerm=1
nthTerm=0
total=0

maxNumber= 4000000

while nthTerm<maxNumber:
    if nthTerm%2==0:
        total+=nthTerm
    nthTerm=nMinus2thTerm+nMinus1thTerm
    nMinus1thTerm=nMinus2thTerm
    nMinus2thTerm=nthTerm
print(total)
