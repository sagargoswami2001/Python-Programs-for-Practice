# Python Program to Represent Enum.
from enum import Enum

class SmartPhones(Enum):
    Realme = 1
    Redmi = 2
    Infinix = 3

print(SmartPhones.Realme)
print(SmartPhones.Realme.name)
print(SmartPhones.Redmi.value)
