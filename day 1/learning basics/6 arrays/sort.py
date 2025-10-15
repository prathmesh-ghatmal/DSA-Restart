def sort(numbers):
    print("before sorting")
    for i in numbers:
        print(i,end=" ")
    
    numbers=sorted(numbers)
    print("\nascending order")
    for i in numbers:
        print(i,end=" ")

    numbers.reverse()
    print("\ndescending order")
    for i in numbers:
        print(i,end=" ")

n=int(input("enter size of list"))

numbers=[int(input(f"enter no {i+1} ")) for i in range(n)]

sort(numbers)