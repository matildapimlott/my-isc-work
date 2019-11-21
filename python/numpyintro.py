# 1

import numpy as np

x = list(range(1,11))
print(x)
a1 = np.array(x)
print(a1)
a2 = np.array(x, dtype=np.float64)
print(a2)

print(a1.dtype)
print(a2.dtype)

#2

azeros = np.zeros((2, 3, 4))
print(azeros)

aones = np.ones((2, 3, 4))
print(aones)

y = np.arange(1000)


#3

a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])

print(a[1])
print(a[1:4])

b = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],[1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]])

print(b)
print(b[:,3])
print(b[1:4,0:4])






