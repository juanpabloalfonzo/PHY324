import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import curve_fit  # Import python libraries

plt.ion()

def chi2(y_measure,y_predict,errors):
    #Calculate the chi squared value given a measurement with errors and prediction
    return np.sum( (y_measure - y_predict)**2 / errors**2 )

def chi2reduced(y_measure, y_predict, errors, number_of_parameters):
    #Calculate the reduced chi squared value given a measurement with errors and prediction,
    #and knowing the number of parameters in the model.
    return chi2(y_measure, y_predict, errors)/(y_measure.size - number_of_parameters)

#Defining needed functions for curve fitting 
def hall1(J,R_h):
    return(R_h*J*800)

def hall2(J,R_h):
    return(R_h*J*587)

def hall3(J,R_h):
    return(R_h*J*355)

#Defining the cross sectional area of metal
w=((8.033-7.026)/(10-0.045))*2945

r=2.217 #Measured Resistance in ohms 

l=2*10**8 #Measured length of metal in angstroms

rho=r*w/l #Calculating electric resistivity with measured parameters 


#Importing Data
data=np.loadtxt('Hall_Ag.txt')
Current1=data[0:10,0]
Uncertanty_Current=data[0:10,1]
HVoltage1=data[0:10,2]
Uncertanty_HVoltage=data[0:10,3]


Current2=data[10:20,0]
HVoltage2=data[10:20,2]

Current3=data[20:30,0]
HVoltage3=data[20:30,2]

J1=Current1/w
E1=-HVoltage1/w

J2=Current2/w
E2=-HVoltage2/w

J3=Current3/w
E3=-HVoltage3/w

Uncertanty_E1=Uncertanty_HVoltage/HVoltage1*E1

Uncertanty_E2=Uncertanty_HVoltage/HVoltage2*E2

Uncertanty_E3=Uncertanty_HVoltage/HVoltage3*E3

#Curve fitting the data to function hall (trial 1)
popt, pcov= curve_fit(hall1,J1,E1, absolute_sigma='True', sigma=Uncertanty_E1)

R_h1=popt[0]

plt.title('E vs J Plot for B=800 mT')
plt.errorbar(J1,E1,yerr=Uncertanty_E1,fmt='o',label='Collected Data')
plt.plot(J1,hall1(J1,R_h1),label='Curve Fit')
plt.xlabel('Current Density (mA/Ang)')
plt.ylabel('Electric Field (' '$\mu$' 'V/Ang)')
plt.legend()
plt.show()
plt.savefig('Ag_Trial_1')
plt.figure()

print('The chi squared value for the first trial fit is:',chi2reduced(E1,hall1(E1,popt[0]),Uncertanty_E1,1))
print('')
print('The parameter R_h found by curve fit is:', popt[0], 'microV/ma*mT', '±', np.sqrt(pcov[0,0]), 'microV/ma*mT')
print('')


#Curve fitting the data to function hall (trial 2)
popt1, pcov1= curve_fit(hall2,J2,E2, absolute_sigma='True', sigma=Uncertanty_E2)

R_h2=popt1[0]


plt.title('E vs J Plot for B=587 mT')
plt.errorbar(J2,E2,yerr=Uncertanty_E2,fmt='o',label='Collected Data')
plt.plot(J2,hall2(J2,R_h2),label='Curve Fit')
plt.xlabel('Current Density (mA/Ang)')
plt.ylabel('Electric Field (' '$\mu$' 'V/Ang)')
plt.legend()
plt.show()
plt.savefig('Ag_Trial_2')
plt.figure()

print('The chi squared value for the first trial fit is:',chi2reduced(E2,hall2(E2,popt1[0]),Uncertanty_E2,1))
print('')
print('The parameter R_h found by curve fit is:', popt1[0], 'microV/ma*mT', '±', np.sqrt(pcov1[0,0]), 'microV/ma*mT')
print('')


#Curve fitting the data to function hall (trial 3)
popt2, pcov2= curve_fit(hall3,J3,E3, absolute_sigma='True', sigma=Uncertanty_E3)

R_h3=popt2[0]

plt.title('E vs J Plot for B=355 mT')
plt.errorbar(J3,E3,yerr=Uncertanty_E3,fmt='o',label='Collected Data')
plt.plot(J3,hall3(J3,R_h3),label='Curve Fit')
plt.xlabel('Current Density (mA/Ang)')
plt.ylabel('Electric Field (' '$\mu$' 'V/Ang)')
plt.legend()
plt.show()
plt.savefig('Ag_Trial_3')
plt.figure()

print('The chi squared value for the first trial fit is:',chi2reduced(E3,hall3(E3,popt2[0]),Uncertanty_E3,1))
print('')
print('The parameter R_h found by curve fit is:', popt2[0], 'microV/ma*mT', '±', np.sqrt(pcov2[0,0]), 'microV/ma*mT')
print('')

#Calculating the other needed parameters and their uncertanties 

n1=1/(R_h1*-1.6202e-16) #Note here elementary charge is in units of mA*s since R_h is in units of mA
n2=1/(R_h2*-1.6202e-16)
n3=1/(R_h3*-1.6202e-16)

un1=(np.sqrt(pcov[0,0])/R_h1)*n1
un2=(np.sqrt(pcov1[0,0])/R_h2)*n2
un3=(np.sqrt(pcov2[0,0])/R_h3)*n3

mu1=(1/rho)*R_h1
mu2=(1/rho)*R_h2
mu3=(1/rho)*R_h3

unmu1=((np.sqrt(pcov[0,0])/R_h1)+(0.001/r)+(1e4/l))*mu1
unmu2=((np.sqrt(pcov1[0,0])/R_h2)+(0.001/r)+(1e4/l))*mu1
unmu3=((np.sqrt(pcov2[0,0])/R_h3)+(0.001/r)+(1e4/l))*mu1

vd1=mu1*E1
vd2=mu2*E2
vd3=mu3*E3

unvd1=((unmu1/mu1)+(Uncertanty_E1/E1))*vd1
unvd2=((unmu2/mu2)+(Uncertanty_E2/E2))*vd2
unvd3=((unmu3/mu3)+(Uncertanty_E3/E3))*vd3
