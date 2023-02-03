def add(a, b):
    return a + b

sum = lambda a, b: a + b

myList=[lambda a, b: a + b, lambda a, b: a * b]
print(myList[0](1, 2))