import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit #Import python libraries

def chi2(y_measure,y_predict,errors):
    #Calculate the chi squared value given a measurement with errors and prediction
    return np.sum( (y_measure - y_predict)**2 / errors**2 )

def chi2reduced(y_measure, y_predict, errors, number_of_parameters):
    #Calculate the reduced chi squared value given a measurement with errors and prediction,
    #and knowing the number of parameters in the model.
    return chi2(y_measure, y_predict, errors)/(y_measure.size - number_of_parameters)


def SHE(R,a1,a2,a3,a4): #Define Function 3 in lab handout to do curve fitting 
    return a1+a2*(np.log(R))+a3*(np.log(R))**2+a4*(np.log(R))**3

def SD(V,I_0,k):
    return I_0*(np.e**((1.6*10**(-9)*V)/(k*298.15))-1)

#Importing Colected Data
TD=np.loadtxt('ThermistorData.txt') 
DD=np.loadtxt('DiodeData.txt')

#Thermistor Analysis
Thermistor_Temp=TD[:,0]+273.15 #Convert temps to Kelvin for curve fitting 
Thermistor_Temp_Err=TD[:,1]
Thermistor_Resistance=TD[:,2] #In K ohms
Thermistor_Resistance_Err=TD[:,3] 

#Fitting the theoretical equation to the data 
popt, pcov= curve_fit(SHE,Thermistor_Resistance,1/Thermistor_Temp, absolute_sigma='True', sigma= Thermistor_Temp_Err)

plt.title('Thermistor Temperature as a Function of its Electrical Resistance')
plt.xlabel('Resitance (k' r'$\Omega$' ')')
plt.ylabel('Temperature(K)')
plt.plot(Thermistor_Resistance, SHE(Thermistor_Resistance,popt[0],popt[1],popt[2],popt[3]),label='Curve Fit')
plt.errorbar(Thermistor_Resistance,Thermistor_Temp,yerr=Thermistor_Temp_Err, xerr=Thermistor_Resistance_Err, label='Collected data')
plt.legend(loc='upper right')
plt.show()
plt.figure()


#Diode Analysis
Diode_Voltage=DD[:,0]
Diode_Voltage_Err=DD[:,1]
Diode_Current=DD[:,2]
Diode_Current_Err=DD[:,3]

#Fitting the theoretical equation to the data 
popt1, pcov1= curve_fit(SD,Diode_Voltage,Diode_Current, absolute_sigma='True', sigma= Diode_Current_Err)

plt.title('I-V Curve of a Silicon Diode')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (miliAmps)')
plt.plot(Diode_Voltage, SD(Diode_Voltage,popt1[0], popt1[1]) ,label='Curve Fit')
plt.errorbar(Diode_Voltage,Diode_Current, yerr=Diode_Voltage_Err, xerr=Diode_Current_Err, label='Collected Data')
plt.legend(loc='upper right')
plt.show()
plt.figure()

