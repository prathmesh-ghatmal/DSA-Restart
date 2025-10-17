# 31. Count the occurrence of an element in a list. 
def count_occurances(n,numbers):
    cnt=0
    for i in numbers:
        if i==n:
            cnt+=1
    return cnt

print(count_occurances(3,[2,3,4,5,3,3]))