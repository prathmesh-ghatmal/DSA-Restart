def check_vowels_consonants(ch):
    if  len(ch)!=1 or not ch.isalpha() :
        print("invalid input")
    elif ch in "aeiouAEIOU":
        print("vowel")
    else:
        print("consonant")

check_vowels_consonants("ae")