
# define a function

#hcf or gcd

# to get to a smaller fraction
def computerHCF(x, y):
   if x > y:
       smaller = y
   else:
       smaller = x
   for i in range(smaller, 0, -1):
       if((x % i == 0) and (y % i == 0)):
           return i
print(computerHCF(18,204))

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

#lcm

# define a function

def lcm_3(l):
    l.sort()
    worst = l[0] *l[1] *l[2]
    for x in range (l[2],worst+1,l[2]):
        if x % l[0]==0 and x%l[1]==0:
            return x
print lcm_3([3,6,18])

def lcm_zuby(n1,n2):
    if n1> n2:
        greater = n1
        smaller = n2
    else:
        greater = n2
        smaller = n1
    for x in range(greater, (n1*n2)+1, greater):
        if x % smaller == 0:
            return x

print lcm_zuby(2,11)



#percentile
#square root
#power of

#prime or not


def isPrime(num):
    flag=True
    for x in range(2, num):
        if num%x ==0:
            print x
            flag=False
            break
    return flag
print (isPrime(90))


def maxPrime(maxnum):
    results = []
    for x in range(2,maxnum):
        flag = True

        for y in range(2, x):
            if x % y == 0:
                #print y
                flag = False
                break
        if flag:
            results.append(x)
    return results

print maxPrime(100)
