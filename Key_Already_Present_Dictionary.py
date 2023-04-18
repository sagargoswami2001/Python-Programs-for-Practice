# Python Program to Check if a Key is Already Present in a Dictionary.

Friends = {"Goswami":"Sagar","Sahu":"Prakash","Rawat":"Sonali","Singhal":"Teesha"}

name = input("Enter a Key Here: ")
# name = "Goswami"
if name in Friends.keys():
    print("It is Present")
