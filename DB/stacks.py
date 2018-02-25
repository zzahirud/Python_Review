#Stack
#LIFO
#using a built in data structure - list and list functions.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s = Stack()
s.push('hello')
s.push('true')
print(s.pop())

print(s.items)

#Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

def revstring(mystr):
    s = Stack()
    s.items = list(mystr);
    rev = ""
    while not s.isEmpty():
        rev =  rev + (s.peek())
        s.pop()
    return  rev
print(revstring("zubair"))
