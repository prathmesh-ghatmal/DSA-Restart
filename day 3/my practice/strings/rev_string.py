# 35. Reverse a string without using built-in functions. 

text=input("enter a string")

rev=""
for ch in text:
    rev=ch+rev
print(rev)