import random as ra
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

#Random Walk Code

def random_walk(N):
    avg_location=np.zeros(100)
    for z in range(100): #Runs the trial 100 times
        X=np.zeros(N)
        for i in range(N): 
            x=np.random.choice([-1,1],1) #Generating Step
            X[i]=x #Storing Position
        avg_location[z]=np.mean(X) #Storing average location after N steps 
    return(avg_location) #Array containing the average location after 100 trials of N steps

def RMS(N):
    distance=np.zeros(100)
    for z in range(100): #Runs the trial 100 times
        X=np.zeros(N)
        for i in range(N): 
            x=np.random.choice([-1,1],1) #Generating Step
            X[i]=x #Storing Position
        distance[z]=np.sum(X) #Storing distance after N steps 
    return(distance) #Array containing the distance of 100 trials of N steps each


#Excercise 5
X=np.zeros(1000)
for i in range(1000): 
    x=np.random.choice([-1,1],1) #Generating Step
    X[i]=x+X[i-1] #Storing Position

Y=np.zeros(1000)
for i in range(1000): #Define an array to serve as x axis of scatter plot below
    Y[i]=i

plt.title('Random Location of Particle')
plt.plot(Y,X)
plt.xlabel('Step Number')
plt.ylabel('Location (from origin)')
plt.savefig('RandomLocation.png')
plt.show()
plt.figure()





#1D Random Walk Code
#N=2**8
a=random_walk(2**8)
mean_a=np.mean(a)
un_a=np.std(a)/10

#N=2**9
b=random_walk(2**9)
mean_b=np.mean(b)
un_b=np.std(b)/10

#N=2**10
c=random_walk(2**10)
mean_c=np.mean(c)
un_c=np.std(c)/10

#N=2**11
d=random_walk(2**11)
mean_d=np.mean(d)
un_d=np.std(d)/10

#N=2**12
e=random_walk(2**12)
mean_e=np.mean(e)
un_e=np.std(e)/10

#N=2**13
f=random_walk(2**13)
mean_f=np.mean(f)
un_f=np.std(f)/10

N=np.array([2**8,2**9,2**10,2**11,2**12,2**13])
means=np.array([mean_a,mean_b, mean_c,mean_d, mean_e,mean_f])
un=np.array([un_a,un_b, un_c,un_d, un_e,un_f])

plt.semilogx(N,means, basex=2)
plt.errorbar(N,means,yerr=un, label='Monte Carlo Simulation Results')
plt.hlines(0,2**7,2**14,label='Theoretical Value')
plt.xlabel("Number of Generated Points")
plt.ylabel('Mean Location From Origin after 100 Trials')
plt.title('1-D Random Walk')
plt.legend()
plt.savefig('1D-RandomWalk.png')
plt.show()
plt.figure()

#RMS Code

#N=2**8
a=RMS(2**8)
mean_a=np.sqrt(np.mean((a**2)))
un_a=np.std(a)/10

#N=2**9
b=RMS(2**9)
mean_b=np.sqrt(np.mean((b**2)))
un_b=np.std(b)/10

#N=2**10
c=RMS(2**10)
mean_c=np.sqrt(np.mean((c**2)))
un_c=np.std(c)/10

#N=2**11
d=RMS(2**11)
mean_d=np.sqrt(np.mean((d**2)))
un_d=np.std(d)/10

#N=2**12
e=RMS(2**12)
mean_e=np.sqrt(np.mean((e**2)))
un_e=np.std(e)/10

#N=2**13
f=RMS(2**13)
mean_f=np.sqrt(np.mean((f**2)))
un_f=np.std(f)/10

N=np.array([2**8,2**9,2**10,2**11,2**12,2**13])
means=np.array([mean_a,mean_b, mean_c,mean_d, mean_e,mean_f])
un=np.array([un_a,un_b, un_c,un_d, un_e,un_f])

plt.semilogx(N,means, basex=2)
plt.errorbar(N,means,yerr=un/N, label='Monte Carlo Simulation Results')
plt.hlines(np.sqrt(N),2**8,2**13,label='Theoretical Values' r'$\sqrt{N}$')
plt.xlabel("Number of Generated Points (N)")
plt.ylabel('RMS after 100 Trials')
plt.title('1-D Random Walk (RMS)')
plt.legend()
plt.savefig('1D-RandomWalk(RMS).png')
plt.show()
plt.figure()




