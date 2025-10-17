n=5
ch=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(ch+i),end=" ")
    print()