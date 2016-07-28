# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# d is the number of digits
def largestPalindrome(d):   # TODO: Treat case d = 0
    n = 10**(d) - 1;        # Initialize n and m with the highest possible values
    m = n                   # For d = 2, n = m = 99; for d = 3, n = m = 999, ...
    lbound = 10**(d-1) - 1  # lower bound = 99 for d = 3
    
    while n > lbound and m > lbound:    # while n and m are 3-digit numbers
        pal = n*m
        if(isPalindrome(pal)):
            return pal
        elif n > m:
            n -= 1
        else:
            m -= 1

# Tells whether n is palindrome or not
def isPalindrome(n):
    s = str(n)  # Casts n to string
    return s == s[::-1] # Tests whether s is read the same backwards and forwards

# print(largestPalindrome(1)) # Outputs ?
# print(largestPalindrome(2)) # Outputs 9009
print(largestPalindrome(3)) # Outputs ????
# print(largestPalindrome(4)) # Outputs ????
