# Section 1 

t = (1,)
print(t[-1])
tup = tuple(range(100,201))
print(tup)
print(tup[0], tup[-1])

print('next section')

# Section 2

mylist = [23, "hi", 2.4e-10]

for (count, index) in enumerate(mylist):
    print (count, index)

print('next section')

# Section 3

first, middle, last = mylist 

print(first)
print(middle)
print(last)

first, middle, last = middle, last, first

print(first)
print(middle)
print(last)

print('the end')
