#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

P = []    # List of candidates for the Largest Prime Award!
# Returns the largest prime factor of n
def largestPrime(n):
    global P        # Initialize empty list of candidates!
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]   # First few primes.
    while n > 1:            # Until reach one, we need further investigation!
        for p in primes:
            r = 1           # r > 0 so we enter the first iteration
            while r > 0:    # Until find a prime which successfully divides n
                r = n%p
                if r > 0:
                    break   # If p is not a factor, try next p
                else:
                    P.append(p)    # Hooray! We found a candidate!
                    largestPrime(n/p)

    # Phew! That was a quite exhausting hunting. I'm knackered...
    # ... but the winner is...:
    print(max(P))

# Test
largestPrime(600851475143)
    
