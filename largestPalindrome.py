# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# d is the number of digits
def largestPalindrome(d):   # TODO: Treat case d = 0
    n = 10**(d) - 1         # n is the largest d-digit number
    lbound = 10**(d-1) - 1  # lower bound = 99 for d = 3
    pals = []
    while n > lbound:
        m = n
        while m > lbound:   
            pal = n*m
            if(isPalindrome(pal)):
                pals.append(pal)
                break
            m -= 1;
        n -= 1;
    return max(pals)
        

# Tells whether n is palindrome or not
def isPalindrome(n):
    s = str(n)  # Casts n to string
    return s == s[::-1] # Tests whether s is read the same backwards and forwards

print(largestPalindrome(1)) # Outputs 9
print(largestPalindrome(2)) # Outputs 9009
print(largestPalindrome(3)) # Outputs 906609
print(largestPalindrome(4)) # Outputs 99000099
