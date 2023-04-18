# Python Program to Check the File Size.

# Method 1: Using os Module
import os

file_size = os.stat("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice/Check_File_Size.py")
print(file_size)
print(file_size.st_size)


# Method 2: Using pathlib Module
from pathlib import Path

file_size = Path("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice/Check_File_Size.py")
print(file_size.stat())
print(file_size.stat().st_size)
