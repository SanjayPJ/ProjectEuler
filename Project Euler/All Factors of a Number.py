import math
number = 1000
start = 1
factor = []
loopCount = 0
while start<= math.sqrt(number) :
    if number%start == 0:
        if number/start == start :
            factor.append(start)
        else:
            factor.append(start)
            factor.append(int(number/start))
    start += 1
    loopCount += 1
factor.sort()
print ("Factors=",factor)
print ("FactorCount=",len(factor))
print ("loopCount=",loopCount)


# completed
# list all the factors of a number