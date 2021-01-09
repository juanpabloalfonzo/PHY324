import random as ra
import numpy as np

#Exercise 1
X=np.zeros(10**4)
Y=np.zeros(10**4)
for i in range(10**4): 
    x=ra.uniform(-1,1) #Generating Position
    y=ra.uniform(-1,1)
    X[i]=x #Storing Position 
    Y[i]=y

inside=np.where(X**2+Y**2<1)
