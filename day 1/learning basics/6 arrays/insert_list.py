def list_operation(n):
    list=[]
    for i in range(n):
        no=int(input("enter a no= "))
        list.append(no)
    print(f"sum of elements in list={sum(list)}")
    print(f"average of elements in list={(sum(list))/n}")


n=int(input("enter the size of list= "))
list_operation(n)