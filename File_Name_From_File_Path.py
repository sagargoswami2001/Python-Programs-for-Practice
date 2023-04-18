# Python Program to Get the File Name From the File Path.

# Method 1: Using OS Module
import os

file_name = os.path.basename("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice/Access_Index_List.py")
print(os.path.splitext(file_name)[0])


# Method 2: Using Pathlib Module
from pathlib import Path

print(Path('C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice/Access_Index_List.py').stem)
