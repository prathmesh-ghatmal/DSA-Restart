#check no is armstrong or not
def armstrong(no):
    temp=no
    sum=0
    k=len(str(no))
    while temp>0:
        rem=temp%10
        sum=sum+rem**k
        temp=temp//10
    return "armstrong" if sum==no else "no armstrong"

print(armstrong(153))