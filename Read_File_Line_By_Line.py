# Python Program Read a File Line By Line Into a List.

# Method 1: Using ReadLines()
f = open("Read_File_Line_By_Line.txt", "r")
lines = f.readlines()

print(lines)

# for remove \n
new_lines = [x.strip() for x in lines]
print(new_lines)


# Method 2: Using For Loop & List Comprehension
f = open("Read_File_Line_By_Line.txt", "r")
line = [line for line in f]

print(line)

new_line = [x.strip() for x in line]
print(new_line)
