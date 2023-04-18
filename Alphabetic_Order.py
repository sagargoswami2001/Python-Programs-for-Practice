# Python Program to Sort Words in Alphabetic Order.

# a = "Harry Potter and the Goblet of Fire"
a = input("Enter Something Here: ")
b = a.split()

print(b)

for i in range (len(b)):
    b[i] = b[i].lower()

print(b)
b.sort()
print(b)

# for Alphabetic Order
for i in b:
    print(i)
