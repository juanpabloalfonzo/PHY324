import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit #Import python libraries

plt.ion()

def voltage(deltat,S): #Defining Seebeck Effect Eqn
    return S*deltaT

def chi2(y_measure,y_predict,errors):
    #Calculate the chi squared value given a measurement with errors and prediction
    return np.sum( (y_measure - y_predict)**2 / errors**2 )

def chi2reduced(y_measure, y_predict, errors, number_of_parameters):
    #Calculate the reduced chi squared value given a measurement with errors and prediction,
    #and knowing the number of parameters in the model.
    return chi2(y_measure, y_predict, errors)/(y_measure.size - number_of_parameters)

#Importing Data 
data=np.loadtxt('ThermocoupleData.txt')

#Categorizing the Data
T1=data[:,0]
T1U=data[:,1]
T2=data[:,2]
T2U=data[:,3]
deltaT=T2-T1
deltaTU=T1U+T2U
V=data[:,4]
VU=data[:,5]

#Resistance of 1.425 ohms

#Fitting the theoretical equation to the data 
popt, pcov= curve_fit(voltage,deltaT,V, absolute_sigma='True', sigma=VU)


plt.errorbar(deltaT,V,yerr=VU,xerr=deltaTU,label='Experimental Data')
plt.plot(deltaT,voltage(deltaT,popt[0]),label='Curve Fit')
plt.title('Voltage and Delta Temperature Relation of the Thermocouple')
plt.xlabel(r'$\Delta$''T (' r'$^{\circ}C$' ')')
plt.legend()
plt.savefig('Thermocouple')
plt.show()
plt.figure()


print('The chi squared value for the Thermocouple fit is:',chi2(deltaT,voltage(deltaT,popt[0]),deltaTU))
print('')
print('The parameter S found by curve fit is:', popt[0], 'mV/C', '±', np.sqrt(pcov[0,0]), 'mV/C')

def temp(voltage): #Function takes user inputed voltage in (mV) and output corresponding delta T (in C)
    return voltage/popt[0]

