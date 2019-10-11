import math
def prime(number) :
    loop=2
    while  loop*loop<=number :
        if number%loop == 0:
            return False
        loop += 1
    return True
def primeNumbers(start, end) :
    primeList = []
    for i in range(start,end) :
        if prime(i) :
            primeList.append(i)
    return primeList
def checkCircular(number) :
    count = len(str(number))
    while True :
        if int(((math.pow(10, count - 1)) * (number % 10))+ (number / 10) ) == number : 
            return True
    return False
start = 2
end = 1000000
loopCount = 0
circularPrime = []
primeList = primeNumbers(start,end)
print (primeList)
"""
for i in primeList :
    if checkCircular(i) :
        circularPrime.append(i)
print ("loopCount=",loopCount)
print (circularPrime)
print (len(circularPrime))
print (primeList)
# not completed
"""
"""


The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

# Test case , might work
"""
import math
def prime(number) :
    loop=2
    while  loop*loop<=number :
        if number%loop == 0:
            return False
        loop += 1
    return True
def primeNumbers(start, end) :
    primeList = []
    for i in range(start,end) :
        if prime(i) :
            primeList.append(i)
    return primeList
	
# Function to check if the number is 
# circular prime or not. 
def checkCircular(N) :
    #Count digits. 
	count = 0
	temp = N 
	while (temp > 0) : 
		count = count + 1
		temp = temp / 10
    num = N
	while True : 
		
		# Following three lines generate the 
		# next circular permutation of a 
		# number. We move last digit to 
		# first position. 
		rem = num % 10
		div = num / 10
		num = int(((math.pow(10, count - 1)) * rem)+ div )

		# If all the permutations are checked 
		# and we obtain original number exit 
		# from loop. 
		if (num == N) : 
			return True
	
	return False
	
# Driver Program 
N = primeNumbers(1,100)
count = 0
for i in N :
    if (checkCircular(i)) : 
        count += 1
print (count)
# This code is contributed by Nikita Tiwari 
"""