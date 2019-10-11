def prime(number):
    if number == 1 or number % 2 == 0 and number != 2 :
        return False
    loopVar=2
    while loopVar*loopVar <= number :
        if number % loopVar == 0:
            return False
        loopVar += 1
    return True
start = 2000
end = 4500
loopCount = 0
primeList = []
for i in range(start,end) :
    loopCount += 1
    if prime(i) :
        primeList.append(i)
print ("loopCount=",loopCount)
print (primeList)


