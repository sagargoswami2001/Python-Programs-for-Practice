# Python Program to Extract Extension From the File Name.

# Method 1: Using OS Module
import os

file_ext = os.path.splitext("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice/Access_Index_List.py")
print(file_ext)
print(file_ext[1])


# Method 2: Using Pathlib Module
from pathlib import Path

print(Path("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice/Append_To_File.txt").suffix)
# print(Path("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice/Append_To_File.txt").stem)
