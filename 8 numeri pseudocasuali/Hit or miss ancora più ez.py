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


#questa funzione è la funzione di rigetto solo che al posto di caricare l'array X aumentiamo un contatore ad ogni if accettato
def hitormiss(f,a,b,N):
    Ns=0
    for i in range (N):
        E=np.random.uniform(a,b)
        eta=np.random.uniform(0,M)
        if(eta  >= 0 and eta <= f(E)):
            Ns+=1
        else:
            continue
    p=Ns/N
    I=p*M*(b-a)
    print(I)
    return p


print(hitormiss(fx,a,b,N))