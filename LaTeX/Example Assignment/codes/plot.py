import numpy as np
import matplotlib.pyplot as plt

n_1=np.arange(0, 33)
n_2=np.array([10, 15, 30])

#reading the values from the dat file
y1=np.loadtxt("series.dat", delimiter=" ", max_rows=1)

#choosing the values to mark
y2=y1[n_2]

#plotting the graph
plt.stem(n_1, y1, markerfmt='.', linefmt='-', basefmt='r', label=r'$x(n)$') 
plt.stem(n_2, y2, markerfmt='o', linefmt='-') 

plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.legend()
plt.savefig('../figs/fig1.png')
