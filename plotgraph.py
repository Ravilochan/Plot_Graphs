# Plot the density of state graph with varying value of "a" such as 2 A , 5 A , 10 A all in one Graph.
# Here we are taking three lists and appending the equations respectively to plot the graph.
# We show the three graphs in one Graph.

import numpy as np 
import math
import matplotlib.pyplot as plt

x=np.linspace(-10,10,num=100)

fx=[]
fx2=[]
fx3=[]
for i in range(len(x)):
    fx.append((math.pi/4)*(((4*8*9.11*10**17)/6.626)**(3/2))*x[i]**(1/2))
    fx2.append((math.pi/4)*(((25*8*9.11*10**17)/6.626)**(3/2))*x[i]**(1/2))
    fx3.append((math.pi/4)*(((100*8*9.11*10**17)/6.626)**(3/2))*x[i]**(1/2))
plt.plot(x,fx)
plt.plot(x,fx2)
plt.plot(x,fx3)
plt.grid()
plt.axvline()
plt.axhline()
plt.show()