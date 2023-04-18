# Python Program to Differentiate Between Type() and IsInstance().

# Type Vs Instance
# l = [1,2,3,4,5,6,7,8,9]
# print(type(l)==list)
# print(isinstance(l, list))

class SmartPhone:
    def name(self):
        pass
class Realme(SmartPhone):
    def phone_name(self):
        pass

obj_SP = SmartPhone()
obj_RM = Realme()

print(type(obj_SP)==SmartPhone)
print(type(obj_RM)==Realme)
print()
print(isinstance(obj_SP, SmartPhone))
print(isinstance(obj_RM, Realme))
print()
print(type(obj_SP)==Realme)
print(isinstance(obj_RM, SmartPhone))
