n=6

for i in range(1,2*n+1):
    if i<=n:
        print("*"*i)
    else:
        print("*"*(n-(i-n)))