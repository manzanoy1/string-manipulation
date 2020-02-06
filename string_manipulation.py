#Yanira Manzano
#2/6/2020
#Adv. Programming
#String Manipulation

print("Please type a string of more than one with commas:")
string = input("")
character = (len(string))

first_character = string[:1]
last_character = string[-1]

upper = string.upper()
title = string.title()
alphabetic = string.isalpha()
individual = string.split()
every_capital= string.isupper()


print(f"Your string has {character} characters")
print(f"The first character is {first_character}")
print(f"The last character is {last_character}")

print(f"String uppercase is {upper}")
print(f"String title case is {title}")
print(f"String being alphabetic: {alphabetic}")
print(f"String split: {individual}")
print(f"Everything Uppercase: {every_capital}")

