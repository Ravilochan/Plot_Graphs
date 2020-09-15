# Plot the density of state graph with value of "a" as 1A.
# Here we are taking the elements in the equation and appending to a list to plot the graph.
# We use grid() to display on a Grid layout.
# We show the Graph.

import numpy as np 
import math
import matplotlib.pyplot as plt

x=np.linspace(-10,10,num=100)

fx=[]
for i in range(len(x)):
    fx.append((math.pi/4)*(1.153547277*10**27)*x[i]**(1/2))
plt.plot(x,fx)
plt.grid()
plt.axvline()
plt.axhline()
plt.show()