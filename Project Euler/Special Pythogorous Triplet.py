import math
def pythogon(a,b,c):
    if a*a+b*b == c*c :
        return True
    return False
a=3
for i in range(1,1000):
    for k in range(1,1000):
        b=a+k
        c=int(math.sqrt(a*a+b*b))
        if pythogon(a,b,c) :
            if int((math.sqrt(a*a+b*b))*10)%10 == 0 :
                #print (a,b,c)
                #print (pythogon(a,b,c))
                #print (a,a*a,b,b*b,c,c*c)
                if a+b+c == 1000:
                    print (a,b,c,"=",a*b*c)
                    exit()
    a+=1



#   There exists exactly one Pythagorean triplet for which a + b + c = 1000.product of abc.