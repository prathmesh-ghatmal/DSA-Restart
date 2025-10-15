def remove_duplicates(numbers):
    temp=[]
    for i in numbers:
        if i not in temp:
            temp.append(i)

    return temp

n=int(input("enter size oF a list"))

numbers=[int(input(f"enter no {i+1}")) for i in range (n)]

result=remove_duplicates(numbers)

print("after removal of duplicates")

for i in result:
    print(i,end=" ")