#1 
import numpy as np	

a = np.array([range(4), range(10,14)])
b = np.array([2, -1, 1, 0])

print(a)
print(b)

ab = a * b 
print(ab) 

b1 = b * 100 
b2 = b * 100.0

print(b1)
print(b2)

print(b1 == b2)

print(b1.dtype)
print(b2.dtype)

#2

arr = np.arange(10)
print(arr < 3)
print(np.less(arr, 3))
condition = np.logical_or(arr < 3 , arr > 8)
new_arr = np.where(condition, arr * 5, arr * -5)

print(new_arr)

#3 

def calculate(u, v):
    magtotal = ((u**2) + (v**2))**0.5
    magtotal_out = np.where(magtotal > 0.1, magtotal, 0.1)
    return magtotal_out 

u_1 = np.array([[4, 5, 6], [2, 3, 4]])
v_1 = np.array([[2, 2, 2], [1, 1, 1]])

print(calculate(u_1,v_1))

u_2 = np.array([[4, 5, 0.01], [2, 3, 4]])
v_2 = np.array([[2, 2, 0.03], [1, 1, 1]])

print(calculate(u_2,v_2))








