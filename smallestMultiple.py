# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder. What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?


# Returns the smallest positive number divisible by all the numbers in the
# specified interval.
def smallestMultiple(end):
    found = False
    m = 1    # Candidate for smallestMultiple
    i = 1
    while found == False:
        while i <= end:    # From 1 to end
            if m % i == 0:  # m is evenly divisible by i?
                i += 1    # Yes, next i
            else:
                m += 1    # No, next candidate
                i = 1
        found = True      # Found our candidate!
    print(m)
                
        

# Test
smallestMultiple(5)
smallestMultiple(10)
smallestMultiple(20)
