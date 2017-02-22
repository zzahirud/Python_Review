

#max in a list
list =[5,6,7,8,34534,542]
def maximum(l):
    max_value = l[0];
    for item in l:
        if item > max_value:
            max_value = item
    return max_value
print maximum(list)

#find key with the most occurance in a sentence

sentence = "Tomorrow is my Facebookkkkkk interview"
def max_key(sentence):
    results = {}
    for item in sentence:
        if item not in results:
            results[item] = 1
        else:
            results[item] = results[item] + 1

    for k,v in results.items():
        if v == max(results.values()):
            return k
print (max_key(sentence))

#First recurring item

def first_recurr(sentence):
    results = {}
    for item in sentence:
        if item not in results:
            results[item] = 1
        else:
            results[item] = results[item] + 1

    for item in sentence:
        if results[item] > 1 :
            return item

print first_recurr(sentence)

#Print all even #s in the list
list_even = [1,2,3,4,5,6,7676,88,65]
def even_only(l):
    results = []
    for num in l:
        if num%2 == 0:
            results.append(num)
    return results
print even_only(list_even)

#print all odd #s in the list
#same with != operator

#print all even indices
def even_indices(l):
    for index, item in enumerate(l,start=1):
        #print index,item
        if index%2 == 0:
            print index,item

even_indices(list_even)
#print all odd indices
def odd_indices(l):
    for index, item in enumerate(l,start=1):
        #print index,item
        if index%2 != 0:
            print index,item

odd_indices(list_even)
#median
def find_median(l):
    if len(l)%2!=0:
        return l[len(l)/2]
    else:
        x = len(l)/2
        y= x-1
        return (l[x] + l[y])/2.0

print find_median(list)

#palindrome

#anagram

#bracket match

#wave sort


#duplicates
dup = [1,2,3,3,4,5,5,6,100,100]
def remove_duplicates(l):
    orig = {}
    dups = []

    for num in l:
        if num not in orig:
            orig[num]=1
        else:
            dups.append(num)
    return orig.keys()
print(remove_duplicates(dup))




#converting sentence to list of workds

#counting the # of words
sentence = 'I  have an interview tomorrow'
def count_words(s):
    results = {}
    list_words = s.split();
    for word in list_words:
        if word not in results:
            results[word]=1
        else:
            results[word]=results[word]+ 1
    return results
print count_words(sentence)

#################################################################################3

#counting numbers in list
def counting_numbers(l):
    res ={}
    for item in l:
        for s in str(item):
            if s not in res:
                res[s]=1
            else:
                res[s] = res[s]+ 1
    return res;
numbers = [123, 1256, 3456, 98]
print (counting_numbers(numbers))

#cleaning strings
input = [
  'ab cde',
  'x yz qwerty',
  'abc x cde abc d er'
]
def clean_strings(l):
    y = []
    for x in input:
        y.extend( x.split())
    return (set(y))
print(clean_strings(input))


