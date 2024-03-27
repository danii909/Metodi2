import numpy as np
from scipy.stats import rankdata, chi2

X_1 = np.array([3129., 3000., 2865., 2890.])
X_2 = np.array([3200., 3000., 2975., 3150.])
X_3 = np.array([2800., 2900., 2985., 3050.])
X_4 = np.array([2600., 2700., 2600., 2765.])

Y=np.concatenate([X_1,X_2,X_3,X_4])
R=rankdata(Y)
print(R)
n=np.array([4,4,4,4])
N=16

R_med=np.mean(R)


S2 = (np.sum(R**2.) - N*(N+1)**2./4.) / (N-1)
print(S2)

Ri=np.zeros(4)
j=0
i=0
for i in range (4):
    Ri[i]=np.sum(R[j:j+4])
    j=j+4
    

print(Ri)

H=(np.sum((Ri**2)/n) - (N*(N + 1)**2)/4)/S2
print(H)

a=0.05

if(H>=chi2.ppf(a,4-1)):
    print("Rigettiamo l'ipotesi")
else:
    print("Non possiamo rigettarla")

