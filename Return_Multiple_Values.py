# Python Program to Return Multiple Values From a Function.

# Method 1: Using Tuples Unpacking
def name():
    return "Sagar", "Goswami", "Ocean"

print(name())
n1, n2, n3 = name()
print(n1, ",", n2, "-", n3)
print(n1, n2)


# Method 2: Using a Dictionary
def names():
    n4 = "Mohit"
    n5 = "Goswami"
    n6 = "Huge"

    return {1:n4,2:n5,3:n6}
naam = names()
print(naam)
print(naam[1], ",", naam[2])
