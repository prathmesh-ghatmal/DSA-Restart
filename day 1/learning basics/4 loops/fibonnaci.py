def print_fibo(n):
    a=0
    b=1
    if n > 1:
        print(0)
        print(1)
    
    while b<=n:
        print(a+b)
        temp=b
        
        b=a+b
        a=temp

print_fibo(15)

