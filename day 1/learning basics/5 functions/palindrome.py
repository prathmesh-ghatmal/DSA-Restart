def check_palindrome(str):
    if str==str[::-1]:
        return "palindrome"
    else:
        return "not palindrome"
    

print(check_palindrome("madam"))