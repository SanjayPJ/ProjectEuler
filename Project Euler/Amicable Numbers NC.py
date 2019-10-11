import math
def factors(n):
    i=1
    factor=[]
    while i<= math.sqrt(n) :
        if n%i == 0:
            if n/i == i :
                factor.append(i)
            else:
                factor.append(i)
                factor.append(int(n/i))
        i+=1
    return factor
n=220
l=[]
#print(sum(factors(n))-n)  
m=sum(factors(n))-n
print (m)
p=sum(factors(m))-m
print (p)


# not completed


"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""