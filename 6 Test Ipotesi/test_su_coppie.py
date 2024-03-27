Si vogliono confrontare due tipi di preparati per pittura. Ci si aspetta un diverso tempo di essic-
camento. Si pu`o supporre che la deviazione standard del tempo di essiccamento per ciascun tipo
di essiccamento sia 8 minuti. 10 pareti vengono tinteggiate con il trattamento 1 e altrettamente
pareti con il trattamento 2. Si rilevano le medie campionare ¯X = 121 minuti e ¯Y = 112 minuti.
Si pu`o trarre la conclusione che il tempo di essiccamento del campione 1 sia maggiore di quello
del campione 2 assumendo α = 0.05?
Calcolare l’intervallo di confidenza per la differenza dei tempi medi di essiccamento.

import numpy as np 
from scipy.stats import norm,t


dev=8
var=dev**2
n=10
u1=121
u2=112
#t1 > t2?
a=0.05

#Z=((u1-u2 - (dev-dev))/np.sqrt((var/n)+(var/n))) Uguale 
#print("Z: ",Z)

Z_test= ((u1 - u2)/np.sqrt(var/n+var/n))
print(Z_test)
if(Z_test>norm.ppf(1-a)):       #UNILATERO A DESTRA
    print("rigettiamo l'ipotesi")
else:
    print("approviamo l'ipotesi")


u3=u1-u2
intrv=u1-u2 - ( norm.ppf(1-a))*(np.sqrt(var/n + var/n)) #UNILATERO A DESTRA
#dx=u1-u2 + ( norm.ppf(1-a/2))*(np.sqrt(var/n + var/n))
print("intervallo: ", intrv)