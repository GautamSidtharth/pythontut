three=3
five=5
maxNumber=1000
total=0

for number in range(maxNumber):
    if number%3==0 or number%5==0:
        total+=number
print (total)
