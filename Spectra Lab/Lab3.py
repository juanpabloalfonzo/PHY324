import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import curve_fit  # Import python libraries


def chi2(y_measure,y_predict,errors):
    #Calculate the chi squared value given a measurement with errors and prediction
    return np.sum( (y_measure - y_predict)**2 / errors**2 )

def chi2reduced(y_measure, y_predict, errors, number_of_parameters):
    #Calculate the reduced chi squared value given a measurement with errors and prediction,
    #and knowing the number of parameters in the model.
    return chi2(y_measure, y_predict, errors)/(y_measure.size - number_of_parameters)

def HR(Wavelenght,m,b): #Hartmann Relation Function 
    return((m/(Wavelenght-286))+b)

def RC(n,RH): #Defining Rydberg Constant Eqn
    return(RH*(0.25-(1/n**2)))

plt.ion()

#Importing the Data
data=np.loadtxt('Hellium.txt')
data2=np.loadtxt('Hydrogen.txt')
Measure=data[:,0]
Wavelenght=data[:,1]
UM=data[:,2]
Hydrogen=data2[:,0]
UH=data2[:,1]
Unknown=data2[:,2]
UU=data2[:,3]
lamba_0=286.0 #+\- 2.0

#Curve fitting the data to function HR
popt, pcov= curve_fit(HR,Wavelenght,Measure, absolute_sigma='True', sigma=UM)

plt.title('Hartmann Relation for Hellium')
plt.errorbar(1/Wavelenght-lamba_0,Measure,yerr=UM, label='Experimental Data')
plt.xlabel('1/Wavelenght (with factor ' r'$\lambda_0$' ' subtracted)')
plt.ylabel('Measured Value on Spectrometer')
plt.plot(1/Wavelenght-lamba_0,HR(Wavelenght,popt[0],popt[1]),label='Curve Fit')
plt.legend()
plt.show()
plt.savefig('CalibrationCurve')
plt.figure()

m=popt[0]
b=popt[1]

print('The chi squared value reduced for the Calibration fit is:',chi2reduced(Measure,HR(Wavelenght,m,b),UM,2))
print('')
print('The parameter m found by curve fit is:', popt[0], 'dial units/nm', '±', np.sqrt(pcov[0,0]), 'dial units/nm')
print('')
print('The parameter b found by curve fit is:', popt[1], 'dial units', '±', np.sqrt(pcov[1,1]), 'dial units')
print('')


#Balmer Series

def WL(measurement): #Define a function which takes in a Spectrometer measurement and outputs a wavelenght
    return((m/(measurement-b))+lamba_0)

i=float(input('Enter Spectrometer Measurement')) #Taking function and propting a user input of dial measurement
W=WL(i)                                          #which returns the corresponding wavelenght
print('The corresponding wavelenght is:', W)    

n=np.array([3,4,5,6]) #array of n values for RC function

HydrogenWavelenghts=WL(Hydrogen)

UH=UH/HydrogenWavelenghts*(1/HydrogenWavelenghts) #Coverting Wavelenght uncertanties by taking their ratio to the wavelenghts of hydrogen
                                                  #And multiplying by the plotted magnitued which is 1/Hydrogen  Wavelenghts

popt1, pcov1= curve_fit(RC,n,1/HydrogenWavelenghts, absolute_sigma='True', sigma=UH)

plt.title('Balmer Series')
plt.errorbar(n,1/HydrogenWavelenghts,yerr=UH, label='Experimental Data')
plt.xlabel('Energy Level (n)')
plt.ylabel('1/Wavelenght of Hydrogen Lines')
plt.plot(n,RC(n,popt1[0]),label='Curve Fit')
plt.legend()
plt.show()
plt.savefig('BalmerSeries')
plt.figure()

Rh=popt1[0] #units of 1/nm

print('The chi squared reduced value for the Balmer Series fit is:',chi2reduced(n,RC(n,Rh),UH,1))
print('')
print('The parameter R_h found by curve fit is:', popt1[0], '1/nm', '±', np.sqrt(pcov1[0,0]), '1/nm')
print('')

#Gas Identification 

#Plug in measured values for wavelengths to verify our guess of Xenon based on colour 

XenonWavelenghts=WL(Unknown)

#Computating hcR_h
RhSI=Rh*1e9 #Converting R_h to SI units

b=sp.constants.h*sp.constants.c*RhSI #Getting calculationg of interest in SI units

c=b*6.242e18 #Converting from J to eV
