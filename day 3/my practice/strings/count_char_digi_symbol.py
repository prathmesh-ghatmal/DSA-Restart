text=input("enter a string")
vowels,consonants,digits,symbols=0,0,0,0
for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1

    elif ch.isnumeric():
        digits+=1
    else:
        symbols+=1

print(f"vowels={vowels} consonants={consonants} digits={digits} sympbols={symbols}")


