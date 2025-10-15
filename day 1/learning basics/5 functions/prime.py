# 21. Write a function to check if a number is prime.
import math
def check_is_prime(no):
    if no<=1:
        return "not prime"
    if no==2:
        return "prime"
    
    if no%2==0:
        return "not prime"
    
    for i in range(3,int(math.sqrt(no))+1,2):
        if no%i==0:
            return "not prime"
        
    return "prime"


print(check_is_prime(11))