#1

s = 'I love to write python'
print(s)

for letter in s:
    print(letter)

print(s[4]) # 5th element
print(s[-1]) # Last element

print(len(s)) # Length

print(s[0])
print(s[0][0])
print(s[0][0][0])

#2

s = 'I love to write python'
split_s = s.split(' ')
print(split_s)

for word in split_s:
    if word.lower().find('i') > -1:
        print(f"I found 'i' in: '{word}'")

#3

something = 'Completely Different'
print(dir(something))
print(something.count('t'))
print(something.find('plete'))
print(something.split('e'))

thing2 = something.replace('Different','Silly')
print(thing2)

something[0] = 'B'

