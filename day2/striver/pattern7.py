for i in range(1,6):
    for j in range(5-i):
        print(end=" ")
    for k in range(i+(i-1)):
        print("*",end="")
    print()