def count_digits(no):
    cnt=0
    while no>0:
        cnt+=1
        no//=10

    return cnt

print(count_digits(1))