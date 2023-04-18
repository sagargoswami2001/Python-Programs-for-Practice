# Python Program to Iterate Over Dictionaries Using For Loop.
friends = {"Sagar":"Goswami","Teesha":"Singhal","Prakash":"Sahu","Sonali":"Rawat"}
print(friends)

# Solution 1 : With .items
for key, value in friends.items():
    print(key, value)

# Solution 2 : With Keys
for key in friends:
    print(key,":", friends[key])

# Solution 3 : With Keys and Values
for key in friends.keys():
    print(key)

for i in friends.values():
    print(i)
    