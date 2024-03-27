from scipy.stats import norm,chi2
import numpy as np

arr = np.array([2.05, 2.04, 1.98, 1.96, 2.03, 2.01, 1.97, 1.99, 2.01, 2.05,
              1.96, 1.95, 2.04, 2.01, 1.97, 1.96, 2.02, 2.04, 1.98, 1.94])

leng=np.size(arr)
a=0.05
med=np.mean(arr)
S=np.std(arr,ddof=1)
var=dev**2
sig0=0.05

print("var: ", var)

W=((S**2)/sig0**2)*(leng-1)

print(W)

chi=chi2.ppf(a/2,leng-1)

print(chi)


if(W < chi or W > chi):
    print("si rigetta")
else:
    print("si approva")