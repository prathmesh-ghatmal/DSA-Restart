def find_largest(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        print(f"{n1} is largest")
    elif n2>=n1 and n2>=n3:
        print(f"{n2} is largest")
    else:
        print(f"{n3} is largest")

n1=int(input("enter first no  = "))
n2=int(input("enter second no = "))
n3=int(input("enter third no  = "))

find_largest(n1,n2,n3)