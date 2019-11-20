#Initialise the variables

forward = []
backward = []
values = ["a", "b", "c"]

#LOOP

for value in values:
    forward.append(value)
    backward.insert(0, value)

print(forward)
print(backward)

forward.reverse()
print(forward)

#More variables

countries = ["uk", "usa", "uk", "uae"]



