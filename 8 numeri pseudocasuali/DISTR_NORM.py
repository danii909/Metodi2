import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats import probplot

N = 100000
E1=  np.random.rand(N)
E2 = np.random.rand(N)

eta1= np.sqrt(-2 * np.log(E1))*np.cos(2*np.pi*E2)
eta2= np.sqrt(-2 * np.log(E1))*np.sin(2*np.pi*E2)

Y = np.concatenate((eta1,eta2))


xx=np.linspace(-5,5,1000)
yy= norm.pdf(xx,0,1)
plt.hist(Y, bins=100, density=True)
plt.plot(xx, yy, 'r')
plt.show()