# Python Program to Append to a File.
f = open("Append_To_File.txt", "a")
f.write("\nThis is My Demo File")
s = "\nHope You Like It"

for i in range(0, 5):
    f.write(s)
f.close()
