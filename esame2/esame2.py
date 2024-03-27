E noto che il numero di pezzi guasti fabbricati in una giornata di lavoro di una catena di produzione
 A segue una distribuzione di Poisson di media 2.
 1. Qual è la probabilità che in un giorno siano stati prodotti esattamente 3 pezzi guasti?
 2. Qual è la probabilità che in un giorno siano stati prodotti tra 2 e 5 pezzi guasti (estremi inclusi)?
 
 Si mette in opera una nuova catena di produzione B. E' noto che il numero di pezzi guasti fabbricati
 in una giornata di lavoro mediante B segue una distribuzione di Poisson di media 1.5.
 
 3. Si trovi la legge della variabile aleatoria che conta complessivemente il numero di pezzi guasti
 prodotti (ciè provenienti indifferentemente da A o da B) e si calcoli la sua media e la sua
 varianza.
 4. Qual è la probabilità che in un giorno siano stati prodotti complessivamente un numero di pezzi
 guasti compreso tra 3 e 6 (estremi inclusi)?

from scipy.stats import poisson
# 1
lambdaA = 2
p1 = poisson.pmf(3, lambdaA)
print(p1)

# 2
p2 = sum([poisson.pmf(i, lambdaA) for i in range(2, 6)])
print(p2)

A ~ Poisson(2)

B ~ Poisson(1.5)

A + B ~ Poisson(3.5)

# 3
lambdaB = 1.5
lambdaAB = lambdaA + lambdaB
print("Media complessiva: ", lambdaAB)
print("Varianza complessiva: ", lambdaAB)

# 4
p3 = sum([poisson.pmf(i, lambdaAB) for i in range(3, 7)])
print(p3)

Il contenuto di sodio (in milligrammi) di 30 scatole di cereali è riportato di seguito
 131.15, 130.69, 130.91, 129.54, 129.64, 128.77, 130.72,
 128.33, 128.24, 129.65, 130.14, 129.29, 128.71, 129.00, 129.39,
 130.42, 129.53, 130.12, 129.78, 130.92, 131.15, 130.69, 130.91,
 129.54, 129.64, 128.77, 130.72, 128.33, 128.24, 129.65.

 1. Si calcoli la media campionaria, la deviazione standard e l’intervallo di confidenza per la media
 con livello di fiducia 0.01.
 2. Rappresentare graficamente i dati mediante un istogramma e mediante un box-plot.



3. Si testi l’ipotesi che il contenuto medio di sodio sia di 130 mg utilizzando α = 0.05. Si calcoli il
 p-value del test precedente.
 4. E' possibile affermare che il contenuto di sodio è distribuito normalmente nelle scatole? Giustificare la risposta.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t, probplot

# 1
dati = np.array([131.15, 130.69, 130.91, 129.54, 129.64, 128.77, 130.72,
                 128.33, 128.24, 129.65, 130.14, 129.29, 128.71, 129.00, 129.39,
                 130.42, 129.53, 130.12, 129.78, 130.92, 131.15, 130.69, 130.91,
                 129.54, 129.64, 128.77, 130.72, 128.33, 128.24, 129.65])

media = np.mean(dati)
dev = np.std(dati)

print("Media: ", media)
print("Deviazione standard: ", dev)

# Intervallo di confidenza al 99%
alpha = 0.01

def conf_int(media, dev, n, alpha):
    phi = norm.ppf(1 - alpha / 2)
    lower = media - (dev / np.sqrt(n)) * phi
    upper = media + (dev / np.sqrt(n)) * phi
    return lower, upper

def conf_int_t(media, dev, n, alpha):
    t_alpha = t.ppf(1 - alpha / 2, n - 1)
    lower = media - (dev / np.sqrt(n)) * t_alpha
    upper = media + (dev / np.sqrt(n)) * t_alpha
    return lower, upper

n = len(dati)
lower, upper = conf_int(media, dev, n, alpha)
print(f"Intervallo di confidenza al 99%: ({lower}, {upper})")

lower, upper = conf_int_t(media, dev, n, alpha)
print(f"Intervallo di confidenza al 99%: ({lower}, {upper})")

# 2

# Istogramma
plt.hist(dati, bins=10, edgecolor='black')
plt.title('Istogramma del contenuto di sodio')
plt.xlabel('Contenuto di sodio (mg)')
plt.ylabel('Frequenza')
plt.show()

# Box plot
plt.boxplot(dati)
plt.title('Box plot del contenuto di sodio')
plt.ylabel('Contenuto di sodio (mg)')
plt.show()

# 3
# Test di ipotesi (sulla media)
# H0: mu = 130
# H1: mu <> 130

mu0 = 130
alpha = 0.05
phi = norm.ppf(1 - alpha / 2)

def z_test(media, dev, mu0, n, phi):
    z = phi * (dev / np.sqrt(n))
    z1 = mu0 - z
    z2 = mu0 + z
    if media < z1 or media > z2:
        return True
    
def t_test(media, dev, mu0, n):
    T = (media - mu0) / dev * np.sqrt(n)
    if abs(T) > t.ppf(1 - alpha / 2, n - 1):
        return True

if z_test(media, dev, mu0, n, phi):
    print("Rigetto H0: la media non è 130")
else:
    print("Accetto H0: la media è 130")

if t_test(media, dev, mu0, n):
    print("Rigetto H0: la media non è 130")
else:
    print("Accetto H0: la media è 130")
    
# P-value
Z0 = np.abs(norm.ppf(1 - alpha / 2))
p_value = 2 * (1 - norm.cdf(Z0))
print("P-value: ", p_value)

# 4
probplot(dati, dist=norm, plot=plt)
plt.show()

I dati non seguono una distribuzione normale.