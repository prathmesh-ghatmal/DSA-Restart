for i in range(5,0,-1):
    for j in range(5-i):
        print(end=" ")
    for k in range(i+(i-1)):
        print("*",end="")
    print()