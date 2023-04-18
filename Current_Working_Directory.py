# Python Program to Get the Full Path of the Current Working Directory.

# Method 1: Using os Module
import os

print(os.path.abspath(os.getcwd()))
print(os.path.dirname(os.path.abspath("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice/Access_Index_List.py")))


# Method 2: Using pathlib Module
import pathlib

print(pathlib.Path().absolute())
print(pathlib.Path("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice/Access_Index_List.py"))
print(pathlib.Path("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice/Access_Index_List.py").parent.absolute())
