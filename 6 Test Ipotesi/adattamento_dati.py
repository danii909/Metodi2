from scipy.stats import t,poisson,chi2
import numpy as np



a=0.05
X=np.array([0,1,2,3,4])
Ni=np.array([584,398,165,35,15])

leng=np.size(Ni)
S=np.sum(Ni)
p0=1/4  #sbagliato
pk=Ni/S
print(pk)

#T=np.sum((Ni - (leng * p0 )**2)/(leng*p0))
#print(T)

#da capire come calcolare P0


T=S * ((np.sum(pk - p0)**2)/p0)

print(T)
chi=chi2.ppf(1-a, leng-1)

print(chi)

if(T > chi):
    print("Si rigetta l'ipotesi")
else:
      print("non si può rigettare l'ipotesi")