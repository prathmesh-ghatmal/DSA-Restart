n=5
for i in range(n):
    ch=ord("A")+(n-i-1)
    for j in range(i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()
