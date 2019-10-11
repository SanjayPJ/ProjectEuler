import itertools
def prime(number) :
    if number == 1 or number % 2 == 0 and number != 2 :
        return False
    loopVar = 2
    while loopVar * loopVar <= number :
        if number % loopVar == 0 :
            return False
        loopVar += 1
    return True
l = [1,22,30,5,54,45]
m=list(map(prime,l))
if True in m :
    print(m)
    print (m.index(True))
    print (l[m.index(True)])
else :
    print ("dsfdsfsdfdsfsdf")