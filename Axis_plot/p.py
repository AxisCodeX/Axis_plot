import numpy as np


x = np.array([ 600,  900, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900,
 4200, 4500, 4800, 5100, 5400, 5700, 6000, 6300,])
y = np.array([600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600,
 600, 600, 600, 600, 640,])

p1 = np.column_stack((x[: -1 ],np.zeros(x.shape[0] - 1)))
p2 = np.column_stack(( x[1:],np.zeros(x.shape[0] - 1)))

h1 = np.column_stack((x[:-1], y))
h2 = np.column_stack((x[1: ] , y))
print(h1)
print(h2)

triangle_1 = np.column_stack((p1,p2,h1))
triangle_2 = np.column_stack((p2,h2,h1))
triangle = np.column_stack((triangle_1 , triangle_2))
print(triangle)



