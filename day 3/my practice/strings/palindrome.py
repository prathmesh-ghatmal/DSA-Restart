# 36. Check if a string is a palindrome. 

text=input("enter a string")

print("palindrome" if text==text[::-1] else "not palindrome") 