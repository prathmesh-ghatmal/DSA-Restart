def reverse(numbers):
    print("before reversal")
    for number in numbers:
        print(number,end=" ")

    
    numbers=numbers[::-1]
    print("\nafter reversal")
    for number in numbers:
        print(number,end=" ")

n=int(input("enter size of the list"))

numbers=[int(input(f"enter no {i+1} = ")) for i in range(n)]
reverse(numbers)