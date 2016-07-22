#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

# Returns the largest prime factor of n
def largestPrime(n):
    factors = []
    
    i = 1
    while n > 1:
        p = nextPrime(i)
        if n % p  == 0:
            factors.append(p)
            n = n / p
        else:
            i = p

    print(max(factors))   # And the largest prime award goes to...

# Tells whether n is prime
def isPrime(n):
    for i in range(2, 100):    # Starts in 2 because divides every number.
        if n%i == 0 and n != i:
            return False
    return True

# Given n return the first prime n < p < 10000
def nextPrime(n):
    for i in range(n+1, 10000):
        if isPrime(i) == True:
            return i
    return 0    # If couldn't find the next prime

# isPrime Testing
##print('Is 7 prime? ' + str(isPrime(7)))
##print('Is 12 prime? ' + str(isPrime(12)))
##print('Is 11 prime? ' + str(isPrime(11)))
##print('Is 29 prime? ' + str(isPrime(29)))
##print('Is 20 prime? ' + str(isPrime(20)))

# nextPrime Testing
##print('Next prime after 7: ' + str(nextPrime(7)))
##print('Next prime after 12: ' + str(nextPrime(12)))
##print('Next prime after 11: ' + str(nextPrime(11)))
##print('Next prime after 29: ' + str(nextPrime(29)))
##print('Next prime after 20: ' + str(nextPrime(20)))

# largestPrimeTesting
largestPrime(12)
largestPrime(17)
largestPrime(147)
largestPrime(13195)
largestPrime(600851475143)
    
