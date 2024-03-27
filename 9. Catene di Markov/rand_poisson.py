# Generazione di numeri pseudo-casuali con ditribuzione Pois(lambda)

import numpy as np

def rand_exp(lam):
    eta = np.random.rand()
    X = -np.log(eta)/lam
    return X

def rand_pois(lam):
    t = 0
    X = 0
    while t <= 1:
        r = rand_exp(lam)
        t = t+r
        X = X+1
    X = X-1
    return X

lam = 2.
N = 10000
X = np.zeros(N)
for i in range(N):
    X[i] = rand_pois(lam)

M = np.max(X)
display(M)

F = np.zeros(int(M+1))
for i in range(N):
    k = int(X[i])
    F[k] = F[k]+1
F = F/N

import matplotlib.pyplot as plt

xx = np.arange(int(M+1))
from scipy.stats import poisson
yy = poisson.pmf(xx, lam)

fig, ax = plt.subplots(1, 1)
plt.bar(xx,F)
plt.plot(xx,yy,'r*')
ax.set_title("Distribuzione Pois(lam)")
plt.show()

display(xx)
display(yy)
display(F)