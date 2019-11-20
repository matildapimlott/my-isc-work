#1

a = [0, 1, 2]
b = a 

print(a)
print(b)

b[0] = 'hello'

print(a)
print(b)

a.append(3)

print(a)
print(b)

#2

a = 'can I change?'
b = a 

print(a)
print(b)

b = 'different'

print(a)
print(b)

print(('Strings are immutable!!!!!!!!!!!!!!!!!!!!')*10)

#3

a = [0, 1, 2]
import copy
b = copy.deepcopy(a)

print(a)
print(b)

b[0] = 'hello'

print(a)
print(b)







