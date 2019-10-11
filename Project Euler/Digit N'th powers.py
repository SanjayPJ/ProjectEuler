import math
power = 5
start  = 100
end = 1000000
loopCount = 0
numberList = []
while start < end :
    i = 0
    sumpow = 0
    while i < len(str(start)) :
        loopCount += 1
        sumpow += int(math.pow(int(str(start)[i]), power))
        i += 1
    #print (start,sum)
    if int(start) == sumpow :
        #print (start)
        numberList.append(int(start))
    start += 1
print ("Loopcount=",loopCount)
print ("Numbers=",numberList)
print ("Sum=",sum(numberList))

# completed

""""


Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""