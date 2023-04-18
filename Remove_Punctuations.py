# Python Program to Remove Punctuations from a String.

punc = '''!@#$%^&*()_-+=~`/[]{};:'"\|<>,.?'''

string = input("Enter Anything Here: ")

empty_str = ""

for i in string:
    if i not in punc:
        empty_str += i

print(empty_str)
