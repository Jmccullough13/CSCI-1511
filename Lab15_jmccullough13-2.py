#The Cubes
#Jeffrey McCullough
# #Plots the first 5000 cubes onto a graph

import matplotlib.pyplot as plt

x_values = range(0, 5001)
y_values = [x**3 for x in x_values]
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=20)
ax.set_title("Cubed Numbers",fontsize=30)
ax.set_xlabel("Value",fontsize=15)
ax.set_ylabel("Cube of Value",fontsize=15)
ax.tick_params(axis='both',which='major',labelsize=15)
ax.axis([0,5100,0,130000000000])
plt.show()
