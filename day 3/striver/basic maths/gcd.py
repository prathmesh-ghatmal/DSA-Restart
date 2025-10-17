# brute
import math
def gcd(n1,n2):
    mini=min(n1,n2)
    result=1
    for i in range(2,mini+1):
        if n1%i==0 and n2%i==0:
            result=i
    return result

print(gcd(12,6))

# better

def gcd_better(n1,n2):
    mini=min(n1,n2)
    for i in range(mini,0,-1):
        if n1%i==0 and n2%i==0:
            return i
print(gcd_better(12,6))

#optimal

def gcd_optimal(n1,n2):
    while n1>0 and n2>0:
        if n1>n2:
            n1=n1&n2
        else:
            n2=n2%n1

    if n1==0:
        return n2
    else:
        return n1
    
print(gcd_optimal(6,12))