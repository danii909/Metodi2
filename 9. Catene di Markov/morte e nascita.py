# Simulazione di una catena di nascita e di morte a tempo continuo

import numpy as np

n0 = 2    # Numero iniziale di individui
lam = 2   # Tasso di nascita
mu = 1    # Tasso di morte
T = 5    # Tempo finale

t = np.array([0.])
X = np.array([n0])
time = 0.
i = 0
while time <= T:
    if X[i] == 0:
        break
    r = np.random.rand()
    time = time - np.log(r)/(lam*X[i]+mu*X[i])
    s = np.random.rand()
    if s < lam/(lam+mu):
        X = np.append(X, X[i]+1)
    else:
        X = np.append(X, X[i]-1)
    t = np.append(t, time)
    i = i+1

import matplotlib.pyplot as plt
plt.plot(t,X)
plt.xlabel('tempo')
plt.ylabel('numero di individui')
plt.show()