def print_months(month):
    match month:
        case 1:
            print("January")
        case 2:
            print("February")
        case 3:
            print("March")
        case 4:
            print("April")
        case 5:
            print("May")
        case 6:
            print("June")
        case 7:
            print("July")
        case 8:
            print("August")
        case 9:
            print("september")
        case 10:
            print("October")
        case 11:
            print("November")
        case 12:
            print("December")
        case _:
            print("invalid input")

month=int(input("enter valid int from 1 to 12"))
print_months(month)