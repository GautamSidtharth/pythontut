sum = lambda a, b: a+b
def calc (operator,operands):
    return operator(operands[0],operands[1])
print(calc(sum,[2,3]))
