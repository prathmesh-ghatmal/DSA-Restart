n=5

for i in range(n):
    ch=ord("A")
    for j in range(i+1):
        print(chr(ch),end="")
        ch=ch+1
    print()
