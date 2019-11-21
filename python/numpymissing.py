import numpy as np
import numpy.ma as MA

#1

maskedarr = MA.masked_array(range(10), fill_value = -999)

print(maskedarr)
print(maskedarr.fill_value)

maskedarr[2] = MA.masked

print(maskedarr)

print(maskedarr.mask)

narr = MA.masked_where(maskedarr > 6, maskedarr)
print(narr)
print(narr.fill_value)

print(narr.filled())

print(type(narr.filled()))

#2

m1 = MA.masked_array(range(1,9))
print(m1)
m2 = MA.reshape(m1, (2,4))
print(m2)

m3 = MA.masked_where(m2 > 6, m2)
print(m3)

m3 = m3 * 100
print(m3)

m4 = np.ones((2,4))

print(m3 - m4)
