n=5
for i in range(n):
    for k in range(n-i):
        print(end=" ")
    ch=ord("A")
    for j in range(2*i+1):
        print(chr(ch),end="")
        if j<i:
            ch+=1
        else:
            ch=ch-1
    print()
            
