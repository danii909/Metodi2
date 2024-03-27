import numpy as np
from scipy.stats import norm
a=0.5
b=2
N=10**5
def fx(x):
    return norm.pdf(x,0,1)

def maxf(f,a,b):
    x=np.linspace(a,b,1000)
    return max(f(x))

M=maxf(fx,a,b)

def hitormiss(f,a,b,N):
    c=0
    for i in range (N):
        E=np.random.uniform(a,b)
        eta=np.random.uniform(0,M)
        if(eta  >= 0 and eta <= f(E)):
            c+=1
        else:
            continue
    P=c/N
    I=P*M*(b-a)
    print(I)
    return P


print(hitormiss(fx,a,b,N))
