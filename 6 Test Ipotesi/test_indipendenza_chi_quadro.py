import numpy as np
from scipy.stats import chi2


a=0.05
X=np.array([[44,10],[81,35]])
n=170

# Probabilità empiriche di trattamento
ph = np.array([54, 116])/n          #l'array 54,116 corrisponde ad qk (nella slide 48 pdf 6)
print("qk: ", qk)

# Probabilità empiriche di guarigione
qk = np.array([125, 45])/n          #l'array 125,45 corrisponde ad Nh (nella slide 48 pdf 6)
print("ph: ",ph)


pihk=X/n                            #Nhk (nella slide 48 pdf 6) rappresenta gli elementi dell'array non le somme come prima

print("pihk:",pihk)

T=0
for h in range (2):
    for k in range (2):
        T =T +  (((ph[h]*qk[k] - pihk[h][k])**2)/pihk[h][k])
        print(T)
        continue
T = n * T
print (T)

chi = chi2.ppf(1-a, 1)
print(chi)


if(T > chi):
    print("rigettiamo l'ipotesi")
else:
    print("non possiamo rigettare l'ipotesi")