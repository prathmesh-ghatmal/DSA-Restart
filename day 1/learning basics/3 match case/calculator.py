def calculator(n1,n2,opp):
    match opp:
        case "+":
            print("sum = ",n1+n2)
        case "-":
            print("diff = ",n1-n2)
        case "/":
            print("Div = ",n1/n2)
        case "*":
            print("prod = ",n1*n2)
        case _:
            print("invalid operator")


n1=int(input("enter first no "))
n2= int (input("enter second no "))
opp=input("enter a valid operator + - / * ")
calculator(n1,n2,opp)