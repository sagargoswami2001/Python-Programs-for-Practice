# Python Program to find HCF(Highest Common Factor) or GCD(Greatest Common Divisor).

def findHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if ((x%i == 0) and (y%i == 0)):
            hcf = i
    return hcf

# x = 12
# y = 30
print("The HCF of the Given Two Numbers is:", findHCF(14, 21))
