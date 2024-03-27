import numpy as np
from scipy.stats import binom,poisson

arr=np.array([   2.1587000e+03,
   1.6781500e+03,
   2.3160000e+03,
   2.0613000e+03,
   2.2075000e+03,
   1.7083000e+03,
   1.7847000e+03,
   2.5751000e+03,
   2.3579000e+03,
   2.2567000e+03,
   2.1652000e+03,
   2.3995500e+03,
   1.7798000e+03,
   2.3367500e+03,
   1.7653000e+03,
   2.0535000e+03,
   2.4144000e+03,
   2.2005000e+03,
   2.6542000e+03,
   1.7537000e+03,
])
n=np.size(arr)
print(n)
a=0.05
H0=2000 #==
arr=arr-H0
print(arr)

c=0


for i in range (np.size(arr)):
    if(arr[i]>=0):
        c=c+1

print (c)

#R=binom.pmf(c,n,1/2)              Non ho capito come calcoliamo il p-value (pagina 56 pdf 6)
#print("R: ",R)

#controlliamo se l'insieme r+ è maggiore o minore di n/2 (dalla slide 56)
arr2=np.array([14,15,16,17,18,19,20])
if(c<n/2):
   Y=binom.pmf(arr2,n,1/2)
else:
    Y=binom.pmf(arr2,n,1/2)


p_value=2*np.sum(Y)
print(p_value)

