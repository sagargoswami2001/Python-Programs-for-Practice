# Write a Python Program to Find Square Root.
def mySqrt(x):
    left = 1
    right = x
    mid = 0
    while(left <= right):
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
            sqrt = mid
    return sqrt

print(mySqrt(36))
