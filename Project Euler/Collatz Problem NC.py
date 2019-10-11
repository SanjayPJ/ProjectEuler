def nextnum(n):
    if n%2 == 0:
        return int(n/2)
    return (3*n+1)
n=1000000
count=[]
while n!=1    :
    elementList=[]
    print (n)
    t=n
    while t>0:
        elementList.append(t)
        t=nextnum(t)
        if t == 1 :
            elementList.append(t)
            break
    count.append(len(elementList))
    n-=1
print (count)
print (max(count))








# not completed









"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
"""