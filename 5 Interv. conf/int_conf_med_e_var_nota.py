Si vuole testare un dispositivo con uno strumento che fornice delle misure di voltaggio. Si
eseguono 9 misurazioni registrando i valori in volt
11, 13.2, 12.3, 10.9, 13, 10.5, 12.3, 13, 13.15.
`E nota la precisione dello strumento e si ha σ = 1 V.
1 Si determinino gli intervalli di confidenza al 95% e al 99%.
2 Determinare gli stessi intervalli di confidenza nel caso in cui si avesse σ = 1.4 V.
3 Sempre con precisione σ = 1 V, determinare gli stessi intervalli con la stessa media delle
misure ma supponendo che essa provenga da un campione di 20 misurazioni.

PAG 41 pdf 5

import numpy as np
from scipy.stats import norm

arr=np.array([11,13.2,12.3,10.9,13,10.5,12.3,13,13.15])
med=np.mean(arr)
leng=np.size(arr)
var=1

intsx95=med-(var/np.sqrt(leng))*(norm.ppf(1-0.05/2))
intdx95=med+(var/np.sqrt(leng))*(norm.ppf(1-0.05/2))
print("sx 95% :", intsx95, " dx 95% :", intdx95)
intsx99=med-(var/np.sqrt(leng))*(norm.ppf(1-0.01/2))
intdx99=med+(var/np.sqrt(leng))*(norm.ppf(1-0.01/2))
print("sx 99% :", intsx99, " dx 99% :", intdx99)

sx 95% : 11.496678671819982  dx 95% : 12.803321328180019
sx 99% : 11.291390232150366  dx 99% : 13.008609767849634

var1=1.4
intsx952=med-(var1/np.sqrt(leng))*(norm.ppf(1-0.05/2))
intdx952=med+(var1/np.sqrt(leng))*(norm.ppf(1-0.05/2))
print("sx 95% :", intsx952, " dx 95% :", intdx952)
intsx992=med-(var1/np.sqrt(leng))*(norm.ppf(1-0.01/2))
intdx992=med+(var1/np.sqrt(leng))*(norm.ppf(1-0.01/2))
print("sx 99% :", intsx992, " dx 99% :", intdx992)

sx 95% : 11.235350140547975  dx 95% : 13.064649859452025
sx 99% : 10.947946325010513  dx 99% : 13.352053674989488

intsx95=med-(var/np.sqrt(20))*(norm.ppf(1-0.05/2))
intdx95=med+(var/np.sqrt(20))*(norm.ppf(1-0.05/2))
print("sx 95% :", intsx95, " dx 95% :", intdx95)
intsx99=med-(var/np.sqrt(20))*(norm.ppf(1-0.01/2))
intdx99=med+(var/np.sqrt(20))*(norm.ppf(1-0.01/2))
print("sx 99% :", intsx99, " dx 99% :", intdx99)