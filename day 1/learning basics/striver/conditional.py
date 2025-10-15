def predict_grade(marks):
    if marks>=90:
        print("A")
    elif marks>=80:
        print("B")
    elif marks>=70:
        print("c")
    else:
        print("d")
    
marks=int(input("enter marks"))
predict_grade(marks)