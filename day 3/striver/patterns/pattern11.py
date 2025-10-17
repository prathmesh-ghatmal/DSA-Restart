n=5

flag=0
for i in range(1,n+1):
    if flag==0:
        flag=1
        temp=1
    else:
        flag=0
        temp=0
    for j in range(i):
        print(temp,end=" ")
        if temp==0:
            
            temp=1
        else:
            temp=0
    print()

    