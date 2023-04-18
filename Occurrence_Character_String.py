# Python Program to Count the Number of Occurrence of a Character in String.

# Method 1: Using For Loop
string = "Sagar_Goswami"
char = "a"
count = 0
for i in string:
    if i == char:
        count = count + 1

print(count)


# Method 2: Using Count Function
string = "Sagar_Goswami"
char = "a"
print(string.count(char))
