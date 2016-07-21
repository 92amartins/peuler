# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# range: search-space. E.g.: [1..10]
# mult: multiples. E.g.: [3, 5]
# Find the sum of all the multiples of 3 or 5 below 1000.
def findSum():
        s = 0
        rng = list(range(1, 1000))      # defines search-space.
        for i in rng:
            if i%3 == 0 or i%5 == 0:    # check multiples (3 or 5 here).
                s += i
        print(s)
#Test
findSum()
