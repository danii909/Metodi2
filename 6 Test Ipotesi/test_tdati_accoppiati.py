PAG 36 PDF 6

from scipy.stats import t
import numpy as np

arr = np.array([265., 240., 258., 295., 251., 245., 287., 314., 260., 279., 283., 240., 238., 225., 247.])
arr2 = np.array([229., 231., 227., 240., 238., 241., 234., 256., 247., 239., 246., 218., 219., 226., 233.])
a=0.05

D=arr-arr2          #attenzizone a mettere prima il primo insieme e sottrarre poi il secondo
med=np.mean(arr)-np.mean(arr2) # or med=np.mean(D)
var=med**2
S=np.std(D,ddof=1)
leng=np.size(D)
med1=np.mean(D)
print(D)



T_test=(med/S)*np.sqrt(leng)
t=t.ppf(1-a,leng-1)

print("T TEST", T_test)
print("t", t)

if(T_test<t):
    print("rigettiamo l'ipotesi ")
else:
    print("Non possiamo rigettare l'ipotesi")


[36.  9. 31. 55. 13.  4. 53. 58. 13. 40. 37. 22. 19. -1. 14.]
T TEST 5.465873994105008
t 1.7613101357748562
Non possiamo rigettare l'ipotesi