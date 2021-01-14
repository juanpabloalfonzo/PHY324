import random as ra
import numpy as np
import matplotlib.pyplot as plt

def in_circle(N):
    num_inside=np.zeros(100)
    for z in range(100): #Runs the trial 100 times
        X=np.zeros(N)
        Y=np.zeros(N)
        for i in range(N): 
            x=ra.uniform(-1,1) #Generating Position
            y=ra.uniform(-1,1)
            X[i]=x #Storing Position 
            Y[i]=y
        inside=np.where(X**2+Y**2<1) #Finding points inside circle
        num_inside[z]=np.size(inside) #Storing number of points inside circle 
    return(num_inside)

def under_curve(N):
    num_inside=np.zeros(100)
    for z in range(100): #Runs the trial 100 times
        X=np.zeros(N)
        Y=np.zeros(N)
        for i in range(N): 
            x=ra.uniform(0,1) #Generating Position
            y=ra.uniform(0,1)
            X[i]=x #Storing Position 
            Y[i]=y

        inside=np.where(Y<np.sin(1/X)) #Finding points under the Curve 
        num_inside[z]=np.size(inside) #Storing number of points under the Curve 
    return(num_inside)

def under_curve3(N):
    num_inside=np.zeros(100)
    for z in range(100): #Runs the trial 100 times
        X=np.zeros(N)
        Y=np.zeros(N)
        for i in range(N): 
            x=ra.uniform(0,1) #Generating Position
            y=ra.uniform(0,1)
            X[i]=x #Storing Position 
            Y[i]=y

        inside=np.where(Y<np.sqrt(1-X**2)) #Finding points under the Curve 
        num_inside[z]=np.size(inside) #Storing number of points under the Curve 
    return(num_inside)

plt.ion()

#Exercise 1

#N=2**8
a=in_circle(2**8)
mean_a=np.mean(a)
un_a=np.std(a)/10

#N=2**9
b=in_circle(2**9)
mean_b=np.mean(b)
un_b=np.std(b)/10

#N=2**10
c=in_circle(2**10)
mean_c=np.mean(c)
un_c=np.std(c)/10

#N=2**11
d=in_circle(2**11)
mean_d=np.mean(d)
un_d=np.std(d)/10

#N=2**12
e=in_circle(2**12)
mean_e=np.mean(e)
un_e=np.std(e)/10

#N=2**13
f=in_circle(2**13)
mean_f=np.mean(f)
un_f=np.std(f)/10

N=np.array([2**8,2**9,2**10,2**11,2**12,2**13])
means=np.array([mean_a,mean_b, mean_c,mean_d, mean_e,mean_f])
un=np.array([un_a,un_b, un_c,un_d, un_e,un_f])

plt.semilogx(N,means/N, basex=2)
plt.errorbar(N,means/N,yerr=un/N, label='Monte Carlo Simulation Results')
plt.hlines(np.pi/4,2**7,2**14, label=r'$\frac{\pi}{4}$')
plt.xlabel("Number of Generated Points")
plt.ylabel('Ratio of Points Inside Circle')
plt.title('Randomly Generated Points in a 2x2 Square That Lie in a Concetric Circle of Radius 1')
plt.legend()
plt.show()
plt.figure()



#Excersise 2
#N=2**8
a2=under_curve(2**8)
mean_a2=np.mean(a2)
un_a2=np.std(a2)/10

#N=2**9
b2=under_curve(2**9)
mean_b2=np.mean(b2)
un_b2=np.std(b2)/10

#N=2**10
c2=under_curve(2**10)
mean_c2=np.mean(c2)
un_c2=np.std(c2)/10

#N=2**11
d2=under_curve(2**11)
mean_d2=np.mean(d2)
un_d2=np.std(d2)/10

#N=2**12
e2=under_curve(2**12)
mean_e2=np.mean(e2)
un_e2=np.std(e2)/10

#N=2**13
f2=under_curve(2**13)
mean_f2=np.mean(f2)
un_f2=np.std(f2)/10

means2=np.array([mean_a2,mean_b2, mean_c2,mean_d2, mean_e2,mean_f2])
un2=np.array([un_a2,un_b2, un_c2,un_d2, un_e2,un_f2])

plt.semilogx(N,means2/N, basex=2)
plt.errorbar(N,means2/N,yerr=un2/N)
plt.xlabel("Number of Generated Points")
plt.ylabel('Ratio of Points Under Curve')
plt.title('Randomly Generated Points That Lie Under' r'$Sin^2(1/x)$' 'for 0<x<1 and 0<y<1')
plt.show()
plt.figure()

#Excerise 3
#N=2**8
a3=under_curve3(2**8)
mean_a3=np.mean(a3)
un_a3=np.std(a3)/10

#N=2**9
b3=under_curve3(2**9)
mean_b3=np.mean(b3)
un_b3=np.std(b3)/10

#N=2**10
c3=under_curve3(2**10)
mean_c3=np.mean(c3)
un_c3=np.std(c3)/10

#N=2**11
d3=under_curve3(2**11)
mean_d3=np.mean(d3)
un_d3=np.std(d3)/10

#N=2**12
e3=under_curve3(2**12)
mean_e3=np.mean(e3)
un_e3=np.std(e3)/10

#N=2**13
f3=under_curve3(2**13)
mean_f3=np.mean(f3)
un_f3=np.std(f3)/10

means3=np.array([mean_a3,mean_b3, mean_c3,mean_d3, mean_e3,mean_f3])
un3=np.array([un_a3,un_b3, un_c3,un_d3, un_e3,un_f3])

plt.semilogx(N,means3/N, basex=2)
plt.errorbar(N,means3/N,yerr=un3/N, label='Monte Carlo Simulation Results')
plt.hlines(np.pi/4,2**7,2**14, label=r'$\frac{\pi}{4}$')
plt.legend()
plt.xlabel("Number of Generated Points")
plt.ylabel('Ratio of Points Under Curve')
plt.title('Randomly Generated Points That Lie Under' r'$\sqrt{1-x^2}$' 'for 0<x<1 and 0<y<1')
plt.show()
plt.figure()

#Excersise 4 
