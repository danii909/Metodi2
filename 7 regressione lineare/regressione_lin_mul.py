import numpy as np
from scipy.stats import t
DATA = np.loadtxt("DATA_reg_lin_2.dat")
x=DATA[:,0]
y=DATA[:,1]
n=x.size
k=2
X=np.ones([x.size,2])
X[:,1]=x

print(X)

XX = np.linalg.pinv(X)
print(XX)

b = XX @ y
display("b: ",b,"\n \n ")
y_hat = X @ b
display("yhatt",y_hat)


#test 
r=y-y_hat
print("r ",r, "\n\n")

mii=np.linalg.pinv(X.T @ X)
print(mii)

M=mii[1][1]
s2= np.sum(r**2)/(n-k)     #n è il size  dell'array x/y non dell'array DATA, k è il numero di colonne, infatti dalle slide i=righe k=colonne
print("s2 ",s2)
s=np.sqrt(s2)
a=0.05

t1=b[1]/(s * np.sqrt(M))
print(t1)
----
t2 = t.ppf(1-a/2,n-2)
print(tt)

if t1 >= t2 :
    print("Rigettiamo l'ipotesi")
else:
    print("Non possiamo rigettarla")
---
# Grafico
xx = np.linspace(0.,12.,100)
yy = b[0] + b[1]*xx

import matplotlib.pyplot as plt
plt.plot(xx, yy)
plt.scatter(x,y)
plt.show()