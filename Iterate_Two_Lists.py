# Python Program to Iterate Through Two Lists in Parallel.

# Using List, For Loop & ZIP() Function.
l1 = ["Sagar","Giri","Goswami"]
l2 = ["Mohit","Ocean","Huge"]

print(tuple(zip(l1,l2)))

for x,y in zip(l1, l2):
    print(x,y)
