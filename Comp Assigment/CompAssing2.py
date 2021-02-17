import random as ra
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

#Method 1
X1=np.zeros(1000)
Y1=np.zeros(1000)
for i in range(1000): 
    r=ra.uniform(0,1) #Generating Position
    theta=ra.uniform(0,2*np.pi)
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    X1[i]=x #Storing Position 
    Y1[i]=y

mean1=np.mean(X1**2+Y1**2)

plt.title('Method 1')
plt.scatter(X1,Y1)
plt.savefig('Method 1')
plt.show()
plt.figure()

#Method 2
X2=np.zeros(1000)
Y2=np.zeros(1000)
for i in range(1000): 
    x=ra.uniform(-1,1) #Generating Points
    y=ra.uniform(-np.sqrt(1-x**2),np.sqrt(1-x**2))
    X2[i]=x #Storing Position         
    Y2[i]=y

mean2=np.mean(X2**2+Y2**2)

plt.title('Method 2')
plt.scatter(X2,Y2)
plt.savefig('Method 2')
plt.show()
plt.figure()

#Method 3
X3=np.zeros(1000)
Y3=np.zeros(1000)

for i in range(1000): 
    x=ra.uniform(-1,1)
    y=ra.uniform(-1,1)
    X3[i]=x #Storing Position 
    Y3[i]=y
a=np.where(X3**2+Y3**2<1)
X3=X3[a]
Y3=Y3[a]

mean3=np.mean(X3**2+Y3**2)

plt.title('Method 3')
plt.scatter(X3,Y3)
plt.savefig('Method 3')
plt.show()
plt.figure()