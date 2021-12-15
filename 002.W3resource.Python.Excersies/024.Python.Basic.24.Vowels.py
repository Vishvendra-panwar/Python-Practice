#Write a Python program to test whether a passed letter is a vowel or not.
print("!!!! Vowels Verifier !!!!\t\n")
letter=input("Enter one Character:")

def vowel_verify(letter):
    all_vowels='aeiouAEIOU'
    return letter in all_vowels

print("Is your Character vowel?", vowel_verify(letter))