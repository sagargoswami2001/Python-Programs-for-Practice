# Python Program to Get the Class Name of an Instance.

# Method 1: Using __class__.__name__
class SmartPhone:
    def name(self,name):
        return name

s1 = SmartPhone()
print(s1.__class__.__name__)


# Method 2: Using type() and __name__ Attributes
class SmartPhone:
    def name(self,name):
        return name

s1 = SmartPhone()
print(type(s1).__name__)
print(type(s1))
