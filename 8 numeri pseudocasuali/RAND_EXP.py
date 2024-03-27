import numpy as np
import matplotlib.pyplot as plt

lam = 2.
N = 200000
X = np.random.rand(N)

print(X)

Y = -np.log(X)/lam  #DA PAG 16 PDF 8 

#creazione di numeri distribuiti esponenzialmente
xx = np.linspace(0.,5.,1000)
from scipy.stats import expon
yy = expon.pdf(xx, 0., 1./lam)

#chek di corrispondenza con un grafico esponenziale 
from scipy.stats import probplot
fig, ax = plt.subplots(1, 1)
probplot(Y, dist=expon, plot=ax)
plt.show()