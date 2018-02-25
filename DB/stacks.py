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



#  Closing symbols match opening symbols in the reverse order of their appearance;
# they match from the inside out. This is a clue that stacks can be used to solve the problem.

#Use a queue when you want to get things out in the order that you put them in.
#Use a stack when you want to get things out in the reverse order than you put them in.
#Use a list when you want to get anything out, regardless of when you put them in (and when you don't want them to automatically be removed).

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))

