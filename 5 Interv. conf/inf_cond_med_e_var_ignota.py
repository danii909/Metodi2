Viene effettuato un test di rottura di un certo materiale ottenendo i seguenti valori in megapascal
(MPa).
19.8 10.1 14.9 7.5 15.4 15.4
15.4 18.5 7.9 12.7 11.9 11.4
11.4 14.1 17.6 16.7 15.8
19.5 8.8 13.6 11.9 11.4
Dopo aver verificato graficamente che il campione proviene da una popolazione distribuita ap-
prossimativamente in modo normale, determinare l’intervallo di confidenza al 95% per la media.

import numpy as np
from scipy.stats import probplot,norm,t
import matplotlib.pyplot as plt
arr = np.array([19.8, 10.1, 14.9, 7.5, 15.4, 15.4, 15.4, 18.5, 7.9, 12.7, 11.9, 11.4, 11.4, 14.1, 17.6, 16.7, 15.8, 19.5, 8.8, 13.6, 11.9, 11.4])
leng=len(arr)

fig,ax=plt.subplots()
probplot(arr, dist=norm, plot=ax)

plt.show()

#2
med=np.mean(arr)
dev=np.std(arr, ddof=1)
Intsx= med - (dev/np.sqrt(leng))*norm.ppf(1-0.05/2)
Intdx= med + (dev/np.sqrt(leng))*norm.ppf(1-0.05/2)
print(Intsx, "sx")
print(Intdx, "dx")

12.22871886508923 sx
15.198553862183497 dx

intsx1=med-(dev/np.sqrt(leng) * t.ppf(1-0.05/2,leng-1))
intdx1=med+(dev/np.sqrt(leng) * t.ppf(1-0.05/2,leng-1))
print(intsx1, "sx")
print(intdx1, "dx")

12.138069152904343 sx
15.289203574368383 dx