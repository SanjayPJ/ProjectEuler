def even(a):
    if a%2 == 0 :
        return 1
    else:
        return 0
n=4000000
sum=0
a=-1
b=1
c=0
while(c<n):
    c=a+b
    a=b
    b=c
    if(even(c)):
        sum+=c
print (sum)

# printf the sum of the all the even fibnocci numbers under number 'n'