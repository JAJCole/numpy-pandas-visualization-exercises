# Use matplotlib to plot the following equation:
# y = x**2 -x + 2
# You'll need to write the code that generates the x and y points.
# Add an anotation for the point 0, 0, the origin.

import matplotlib.pyplot as plt


x = range(-100,100)
y = [(num**2-num +2)for num in x]

plt.plot(x,y)
plt.xlabel = 'x'
plt.ylabel = 'y'
plt.title('y = x**2 -x + 2 [-100,100]')
plt.annotate('Origin', xy = (0,0))

# Create and label 4 separate charts for the following equations 
# (choose a range for x that makes sense):
import math

# y=√x
x = range(0,30)
y = [(math.sqrt(n))for n in x]
plt.plot(x,y)
plt.title('y=√x [0,30]')


# y=x**3
x = range(-30,30)
y = [(math.pow(n,3))for n in x]
plt.plot(x,y)
plt.title('y=x**3 [-30,30]')

# y=2**x
x = range(0,30)
y = [(math.pow(2,n)) for n in x]
plt.plot(x,y)
plt.title('y=2**x [0,30]')


# y=1/(x+1)
x = range(0,30)
y = [1/(n + 1)for n in x]
plt.plot(x,y)
plt.title('1/(x+1) [0,30]')


# Combine the figures you created in the last step into one large figure with 4 subplots.
n_row = 1
n_column = 5

# what about plt.subplot(1,4,1) ?
plt.suptitle('Sample Functions')
plt.subplot(n_row, n_column, 2)
x_2 = range(0,30)
y_2 = [(math.sqrt(n))for n in x_2]
plt.plot(x_2,y_2)
#plt.title('y=√x [0,30]')


plt.subplot(n_row,n_column,3)
x_3 = range(-30,30)
y_3 = [(math.pow(n,3))for n in x_3]
plt.plot(x_3,y_3)
#plt.title('y=x**3 [-30,30]')


plt.subplot(n_row,n_column,4)
x_4 = range(0,30)
y_4 = [(math.pow(2,n)) for n in x_4]
plt.plot(x_4,y_4)
#plt.title('y=2**x [0,30]')


plt.subplot(n_row,n_column,1)
x = range(0,30)
y = [1/(n + 1)for n in x]
plt.plot(x,y)
#plt.title('1/(x+1) [0,30]')


# Combine the figures you created in the last step into one figure 
# where each of the 4 equations has a different color for the points. 
# Be sure to include a legend and an appropriate title for the figure.

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0, 5, 100)
x3 = np.linspace(-3, 5, 100)
x4 = np.linspace(0, 5, 100)

y = [1 / (n + 1) for n in x]
y_2 = [math.sqrt(n) for n in x if n >= 0]
y_3 = [math.pow(n, 3) for n in x3]
y_4 = [math.pow(2, n) for n in x4]

fig, ax = plt.subplots()

ax.plot(x, y, label='y = 1/(x+1)', color='g')
ax.plot(x, y_2, label='y = √x', color='b')
ax.plot(x3, y_3, label='y = x**3', color='m')
ax.plot(x4, y_4, label='y = 2**x', color='r')

ax.set_title('Overlayed Sample Functions')
ax.legend()
plt.tight_layout()
plt.ylim(-3,9)
plt.show()



