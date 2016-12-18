#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zubair.zahiruddin
#
# Created:     07/09/2016
# Copyright:   (c) zubair.zahiruddin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


import random

# A generator is very similar to a function that returns an array, in that a generator has parameters, can be called, and generates a sequence of values.
#However, instead of building an array containing all the values and returning them all at once, a generator yields the values one at a time, which requires
#less memory and allows the caller to get started processing the first few values immediately. In short, a generator looks like a function but behaves
#like an iterator.

# function version
def fibon(n):
    a = b = 1
    result = []
    for i in xrange(n):
        result.append(a)
        a, b = b, a + b
    return result

# generator version
def fibonn(n):
    a = b = 1
    for i in xrange(n):
        yield a
        a, b = b, a + b

#The function is clearer. And if you use the function like this:

for x in fibonn(5):
   print x,

# USE GENERATORS to run a select query but in batches.
# select top 1000 , with min and max ids , till we get the whole table.

# Another EXAMPLE

# for each i iteration, takes the first number, executes it, pauses the execution state, return it to the function that called it.
# function/statement calling the generator - runs its execution- then asks the generator to resume its state to get the other values.

def lottery():
    # returns 6 numbers between 1 and 40
    for i in xrange(6):
        #yield i;
        yield random.randint(30, 40);

    # returns a 7th number between 1 and 15
    yield random.randint(10,15);

for random_number in lottery():
    print "And the next number is... %d!" % random_number
