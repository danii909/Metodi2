In una catena di produzione si vuole mantenere il numero di pezzi difettosi al di sotto del 5%.
Si analizza un campione di 200 pezzi e si trovano 4 pezzi difettosi.
Si pu`o asserire ad un livello di significativit`a α = 0.05 che la produzione rispetta le
aspettative?
Supponendo che il valore vero sia p∗ = 0.03 e supponendo che il costruttore voglia
accettare un valore dell’errore di secondo tipo β = 0.1, quale ampiezza dovrebbe avere il
campione?

#1
import numpy as np
from scipy.stats import norm
p0=0.05
n=200
d=4
p=0.03 
b=0.1
med=np.mean(n)
p_bar=4/n   #mi ricavo un'altra probabilità, la media di pezzi rotti praticamente
Z= ((p_bar - a)/np.sqrt(p0*(1-p0)))*np.sqrt(n)
print(Z)

if (Z < norm.ppf(a)):
    print("rigettiamo l'ipotesi")
else:
    print("la approviamo")

#2

Dim_camp = ((norm.ppf(b)*np.sqrt(p*(1.-p)) + norm.ppf(a)*np.sqrt(p0*(1.-p0)))/(p0-p))**2.
display(Dim_camp)