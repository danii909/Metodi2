import numpy as np
from scipy.stats import norm,t
import matplotlib.pyplot as plt
x = np.array([0,1,2,3,4,5,6,7,8,9,10])
y=  np.array([19.5,22.1,24.3,25.7,26.1,28.5,30,32.1,32.7,32.7,35])

print(x,y)
n=x.size
x_mean=np.mean(x)
y_mean=np.mean(y)
dev_xy=np.sum(x*y - x_mean*y_mean)/n
#dev_xy=np.sum((x-x_mean)*(y-y_mean))/n

x_dev=np.std(x)
x_var=np.sum((x**2)-(x_mean**2))/n

print(x_var, " ", x_dev**2)
print(x_mean,y_mean)

print(dev_xy, x_dev, x_var)






xx=np.linspace(y.min(),y.max(),1000)
yy=b0 + b1*xx
plt.plot(xx,yy)
plt.scatter(x,y)
plt.show()
----

b0=y_mean - (dev_xy/x_var)*x_mean
b1=dev_xy/x_var
print(b0,b1)
----
#2 calcolo significatività

a=0.05
#residui:
y_hat=b0+b1*x
r=y-y_hat
print(r)
s2=np.sum(r**2)/(n-2)
s=np.sqrt(s2)

T=np.abs(np.sqrt(n)*(b1/s)*x_mean)

t=t.ppf(1-a/2,n-2)

print(T,"t piccolo;",t)

if(T>=t):
    print("Rigettiamo l'ipotesi")
else:
    print("Non possiamo rigettare l'ipotesi")