# Pyhon Program to Measure the Elapsed Time in Python.

# Method 1: Using Time Modele
import time
starting_time = time.time()

# print("Sagar Goswami")
num1 = int(input("Enter a First Number: "))
num2 = int(input("Enter a Second Number "))
print(num1 + num2)

ending_time = time.time()
print(ending_time - starting_time)


# Method 2: Using Timeit Module
from timeit import default_timer as timer
starting_value = timer()

# print("Sagar Goswami")
print(27**2001)

ending_value = timer()
print(ending_value - starting_value)
