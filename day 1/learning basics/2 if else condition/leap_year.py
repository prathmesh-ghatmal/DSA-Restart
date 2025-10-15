def check_leap_year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        print("it's a leap year")
    else:
        print("isn't a leap year")

year=int(input("enter a valid year"))
check_leap_year(year)
