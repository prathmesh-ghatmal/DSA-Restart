def print_grade(marks):
    if marks<0 or marks>100:
        print("Invalid marks")
    elif marks>=90:
        print("A")
    elif marks>=80:
        print("B")
    elif marks>=70:
        print("C")
    elif marks>=60:
        print("D")
    else:
        print("F")

marks=int(input("enter marks between 1 to 100"))
print_grade(marks)