n=5
for i in range(2*n):
    if i<n:
        print("*"*(n-i)+" "*(2*i)+"*"*(n-i))
    else:
        print("*"*(i-n+1)+" "*((2*n)-(2*(i-n+1)))+"*"*(i-n+1))
    
