#linear search

def sequentialSearch(alist, item):
	    pos = 0
	    found = False
	
	    while pos < len(alist) and not found:
	        if alist[pos] == item:
	            found = True
	        else:
	            pos = pos+1
	
	    return found
	
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))


#binary search

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
#print(binarySearch(testlist, 3))
#print(binarySearch(testlist, 13))

def my_search (l, item):
    l.sort()
    first_index = 0
    last_index = len(l)-1
    found = False

    while first_index <= last_index and not found :

        if l[last_index//first_index] == item:
            found = True
        else:
            if item > l[(last_index//first_index)]:
                first_index = (last_index//first_index)
            elif item < l[(last_index//first_index)]:
                last_index = (last_index//first_index)

    return found

print my_search(testlist,3)
# 0(n) = log
O(logn)
