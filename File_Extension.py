# Python Program to Find All File With .txt Extension Present Inside a Directory.

# Method 1: Using glob & os Module
import glob, os
os.chdir("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice")

for files in glob.glob("*.txt"):
    print(files)


# Method 2: Using os Module
import os
for files in os.listdir("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice"):
    if files.endswith(".py"):
        print(files)


# Method 3: Using os.walk()
import os

for root, dir, files in os.walk("C:/Users/SHIVSHANKAR/Documents/Python Programming/Python Programs for Practice"):
    for file in files:
        if file.endswith(".txt"):
            print(file)
