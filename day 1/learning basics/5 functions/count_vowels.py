def count_vowels(str):
    cnt=0
    for ch in str:
        if ch in "aeiouAEIOU":
            cnt+=1
    return cnt

str=input("enter a valid string ")

cnt=count_vowels(str)
print(f"given string has {cnt} vowels")