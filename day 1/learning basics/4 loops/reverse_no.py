# 19. Reverse a number using a while loop. 

def reverse(no):
    reverse=0
    while no>0:
        rem=no%10
        reverse=reverse*10+rem
        no=no//10

    print(reverse)

reverse(123)
    
