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
import random


# A generator is very similar to a function that returns an array, in that a generator has parameters, can be called, and generates a sequence of values.
#However, instead of building an array containing all the values and returning them all at once, a generator yields the values one at a time, which requires
#less memory and allows the caller to get started processing the first few values immediately. In short, a generator looks like a function but behaves
#like an iterator.

#Generators are defined similar to function but there is only one difference,
#we use yield  keyword to return value used for each iteration of the for loop.

# function version
def fibon(n):
    a = 1 ;
    b = 1 ;
    result = []
    for i in xrange(n):
        result.append(a)
        a  = b ;
        b = a + b ;
    return result

# generator version
def fibonn(n):
    a = 1 ;
    b = 1 ;
    for i in xrange(n):
        yield a
        a  = b ;
        b = a + b ;

#The function is clearer. And if you use the function like this:

for x in fibonn(10):
   print x

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


# Reading DB Rows using a generator.


#In applications that use the Python DB API, you often see code that goes somewhat like (where
#cursor is a DB API cursor object):

cursor.execute('select * from HUGE_TABLE')
for result in cursor.fetchall( ):
    doSomethingWith(result)

#This simple approach is "just" fine, as long as fetchall returns a small result set, but it does not
#work very well if the query result is very large.
#A large result set can take a long time to return.
#Also, cursor.fetchall( ) needs to allocate enough memory to store the entire result set in
#memory at once. Further, with this simple approach, the doSomethingWith function isn't going to
#get called until the entire query's result finishes coming over from the database to our program.
#An alternative approach is to rely on the cursor.fetchone method:

for result in iter(cursor.fetchone, None):
    doSomethingWith(result)

#However, this alternative approach does not allow the database to optimize the fetching process:
#most databases can exhibit better efficiency when returning multiple records for a single query,
#rather than returning records one at a time as fetchone requires.

def fetchsome(cursor, arraysize=1000):
    ''' A generator that simplifies the use of fetchmany '''
    while True:
        results = cursor.fetchmany(arraysize)
        if not results: break
        for result in results:
            yield result

for result in fetchsome(cursor):
    doSomethingWith(result)

# I believe this will be only useful once you cursor.execute("sql") is completed, then we can bring the results in python in batches.

# Another Example
#--------------------------------------

def my_range(start, stop, step = 1):
    if stop <= start:
        raise RuntimeError("start must be smaller than stop")
    i = start
    while i < stop:
        yield i
        i += step

try:
    for k in my_range(10, 50, 3):
        print(k)
     #pass
except RuntimeError as ex:
    print(ex)
except:
    print("Unknown error occurred")

#In for loop my_range()  function get called, it initializes values of the three arguments( start , stop  and step ) and also checks
# whether stop  is smaller than or equal to start , if it is not then i  is assigned value of start . At this point i  is 10 so while
#condition evaluates to True  and while loop starts executing. In next statement yield transfer control to the for loop and assigns
#current value of i to variable k , inside the for loop print statement get executed, then the control again passes to line 7 inside
#the function my_range()  where i  gets incremented. This process keeps on repeating until i < stop