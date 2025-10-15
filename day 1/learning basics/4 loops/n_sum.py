def print_sum():
    no=int(input("enter no "))
    sum=0
    while no!=0:
        sum=sum+no
        no=int(input("enter no for continue enter 0 if you want to stop"))
    print(sum)

print_sum()
