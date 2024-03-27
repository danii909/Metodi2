import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
n=26
DATA = np.loadtxt("DATA_reg_lin.dat")
x = DATA[:,1]    # Peso corporeo
y = DATA[:,2]    # Pressione sistolica
print(x,y)
#calcolo i coefficenti della retta di regressione
x_mean=np.mean(x)
y_mean=np.mean(y)
n=np.size(x)
devx=np.std(x)
devxy=(np.sum(x*y - x_mean*y_mean))/n

varx=(np.sum(x**2-x_mean**2))/n
print(devxy)
print(varx)

b0= y_mean - (devxy/(varx))* x_mean
b1=(devxy/varx)

print(b0)
print(b1)

xx=np.linspace(min(x),max(x),1000)
yy=b0+b1*xx

plt.plot(xx,yy)
plt.scatter(x,y)
plt.show()

--

# Calcolo dei residui
y_hat = b0 + b1*x
r = y - y_hat
print(r)

s2 = np.sum(r**2.)/(n-2)
display(s2)
s=np.sqrt(s2)
print(s)

intsx=b1-(s/(devx*np.sqrt(n)) * t.ppf(1-a/2,n-2))
intdx=b1+(s/(devx*np.sqrt(n)) * t.ppf(1-a/2,n-2))

print(intsx,intdx)

---
#significatività bilatero

Test=np.abs(np.sqrt(n)*(b1/s)*devx)
t=t.ppf(1-a/2,n-2)

print(Test)
print(t)

if(Test>=t):
    print("rigetto l'ipotesi")
else:
    print("non possiamo rigettarla")

---
#calcolo coefficente di determinazione
vary=np.var(y)
R= devxy**2/(varx*vary)



print(R)
--
o= np.sum(x**2 - x_mean**2)/n  #slide 13 pdf 7, calcolare quella roba e calcolare la varianza è la stessa cosa
print(o)
print(devx**2)