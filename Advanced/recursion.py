# reversing a string using recursion

name = "zubair_zahiruddin"
def reverse(name):
    if len(name) == 1 :
        return name[0]
    else:
        return name[len(name)-1] + reverse(name[:-1])
print reverse(name)
