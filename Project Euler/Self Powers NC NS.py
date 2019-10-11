def power(number,toPower) :
    result = 1
    loopVar = 0
    while loopVar < toPower :
        result *= number
        loopVar += 1
    return  result
def selfPowSum(number) :
    sum = 0
    for loopVar in range(1,number + 1) :
        sum += power(loopVar,loopVar)
    return sum
number = 1000
sum = selfPowSum(number)
sum = str(sum)[::-1]
result = ""
for loopVar in range(10) :
    result += sum[loopVar]
print ("Result=(str)",result)
print ("Result=(int)",int(result))
#print ("Sum=",sum)


# Not yet submitted

# not completed
"""


The series, 1(1) + 2(2) + 3(3) + ... + 10(10) = 10405071317.

Find the last ten digits of the series, 1(1) + 2(2) + 3(3) + ... + 1000(1000).

"""