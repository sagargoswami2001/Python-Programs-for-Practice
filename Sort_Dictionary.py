# Python Program to Sort a Dictionary By Value.

marks = {"Sagar": 27, "Teesha": 7, "Prakash": 18, "Sonali": 7}
print(marks)

# Solution 1 : Sort the Dictionary Based on Values
sg = sorted(marks.items(), key= lambda x : x[1])
print(sg)

# Solution 2 : Sort Only the Values
m = sorted(marks.values())
print(m)