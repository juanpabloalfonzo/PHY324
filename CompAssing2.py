import random as ra
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

#Method 1
X=np.zeros(100000)
Y=np.zeros(100000)
for i in range(100000): 
    r=ra.uniform(0,1) #Generating Position
    theta=ra.uniform(0,2*np.pi)
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    X[i]=x #Storing Position 
    Y[i]=y

plt.title('Method 1')
plt.scatter(X,Y)
plt.show()
plt.figure()

#Method 2
X=np.zeros(100000)
Y=np.zeros(100000)
for i in range(100000): 
    x=ra.uniform(-1,1) #Generating Points
    y=ra.uniform(-np.sqrt(1-x**2),np.sqrt(1-x**2))
    X[i]=x #Storing Position         
    Y[i]=y
plt.title('Method 2')
plt.scatter(X,Y)
plt.show()
plt.figure()

#Method 3
X=np.zeros(100000)
Y=np.zeros(100000)
for i in range(100000): 
    x=ra.uniform(-1,1)
    y=ra.uniform(-1,1)
    X[i]=x #Storing Position 
    Y[i]=y
plt.title('Method 3')
plt.scatter(X,Y)
plt.show()
plt.figure()