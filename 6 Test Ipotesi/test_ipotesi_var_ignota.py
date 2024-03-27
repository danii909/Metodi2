Si vuole testare ad un livello di significativit`a α = 0.05 se il carico di rottura di un materiale
supera 10 MPa, tenendo presente che 22 prove hanno fornito i seguenti risultati
19.8 18.5 17.6 16.7 15.8
15.4 14.1 13.6 11.9 11.4
11.4 8.8 7.5 15.4 15.4
19.5 14.9 12.7 11.9 11.4
10.1 7.9
Calcolare inoltre il p-value.

import numpy as np
from scipy.stats import t

arr=np.array([19.8, 18.5, 17.6, 16.7, 15.8, 15.4, 14.1, 13.6, 11.9, 11.4,
              11.4, 8.8, 7.5, 15.4, 15.4, 19.5, 14.9, 12.7, 11.9, 11.4, 10.1, 7.9])

leng=np.size(arr)
med=np.mean(arr)
a=0.05
u=10
dev=np.std(arr,ddof=1)
T=((med - u)/dev)*np.sqrt(leng)
t_test= t.ppf(1-a,leng-1)

print("T: ", T)
print("t_test: ", t_test)

if( T>t_test):
    print("rigettiamo l'ipotesi")
else:
    print("approviamo l'ipotesi")