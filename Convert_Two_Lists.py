# Python Program to Convert Two Lists Into a Dictionary.

# Method 1: Using ZIP() And Dictionary Methods
name = ["Sagar", "Mohit", "Goswami", "Ocean"]
marks = [98,97,96,95]

dictionary = zip(name, marks)
print(dict(dictionary))


# Method 2: Using ZIP() And List Comprehension
name = ["Sagar", "Mohit", "Goswami", "Ocean"]
marks = [98,97,96,95]

dictionary = {key:value for key, value in zip(name,marks)}
print(dictionary)
