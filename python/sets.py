#1 

a = set([0, 1, 2, 3, 4, 5])
b = set([2, 4, 6, 8])

print(a.union(b))
print(a.intersection(b))

#2

band = ["mel", "geri", "victoria", "mel"]
counts = {}

for name in band:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1 

for name in counts:
    print(name, counts[name])    

#3

d = {"maggie" : "uk", "ronnie" : "usa"}

print(dir(d))
print(d.items())
print(d.keys())
print(d.values())



