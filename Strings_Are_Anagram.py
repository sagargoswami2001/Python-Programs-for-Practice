# Python Program to Check If Two Strings are Anagram.
print("Program to Check Anagram")
s1 = input("Enter a Word Here: ")
s2 = input("Enter a Word Here: ")

if len(s1) == len(s2):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    if s1_sorted == s2_sorted:
        print("The String is an Anagram")
    else:
        print("The String is not an Anagram")
else:
    print("The String is not an Anagram")
# print(s1_sorted,s2_sorted)
