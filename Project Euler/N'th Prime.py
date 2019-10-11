def prime(a):
    i = 2
    while i * i <= a :
        if a % i == 0:
            return 0
        i += 1
    return 1

a = 10001
n = 2
loopCount = 0
count = 0
while True :
    loopCount += 1
    if prime(n) :
        count += 1
    if count == a:
        print (n)
        break
    n += 1
print ("loopCount=",loopCount)
# prints the n'th prime number