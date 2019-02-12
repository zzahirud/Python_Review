
print (1)

# a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.


# o(n^2)
def anangram(s1, s2):
    stillOK = True
    for letter in s1:
        for letter1 in s2:
            print ("comparing " + letter + " and " + letter1)
            if letter == letter1:
                stillOK = True
                break
            else:
                stillOK = False

        print(stillOK)
        # if a charachter from s1 is not found in s2 then we don't need to compare other ones
        if(stillOK == False):
            return  stillOK
    return stillOK

print(anangram("zubair", "raibpz"))


# O (n)
def anangram1(s1, s2):
    mapping = {}
    mapping1 = {}
    for character in s1:
        if character not in mapping:
            mapping[character] = 1
        else:
            mapping[character] += 1

    for character in s2:
        if character not in mapping1:
            mapping1[character] = 1
        else:
            mapping1[character] += 1

    return (mapping == mapping1)


print(anangram1('zubbbbair', 'zubbbbair'))


def bubbleSort(alist):

   #Setting the range for comparison (first round: n, second round: n-1  and so on)
   for i in range(len(alist)-1,0,-1):
       print('first iteration')
       print(i)

      #Comparing within set range
       for j in range(i):
           print('second loop')
           print(j)

           #Comparing element with its right side neighbor
           if alist[j] > alist[j+1]:
               print(alist[j])
               print(alist[j+1])

               #swapping
               temp = alist[j]
               alist[j] = alist[j+1]
               alist[j+1] = temp

   return alist

print(bubbleSort([5,1,2,3,9,8,0]))
# How do you find the missing number in a given integer array of 1 to 100


# palindrome
# 2 egg problem
# reverse linked list
# stacks
# queues
# recursion - 3 principles
# bracket matching problem
# principles = for highest number vs something like anangram- requires nested - evaluate after nested loop
# swift - coding challenges



for i in range(5,0,-1):
    #does not include 0, goes 5,4,3,2,1
    print i

for i in range(5):
    # does not include 5
    #goes 0, 1 ,2, ,3 ,4
    print i