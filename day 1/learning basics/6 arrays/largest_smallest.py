def find_largest_smallest(numbers):
    print("largest elememt in a list=",max(numbers))
    print("smallest element in a list= ",min(numbers))

no=int(input("enter the size of a list"))
numbers=[]
for i in range(1,no+1):
    x=int(input(f"enter {i}th no"))
    numbers.append(x)

find_largest_smallest(numbers)