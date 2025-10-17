# 37. Replace all vowels in a string with *. 

text=input("enter a string").lower()
result=""
for ch in text:
    if ch in "aeiou":
        result=result+"*"
    else:
        result=result+ch

print (result)
