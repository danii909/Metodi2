ESERCIZIO PAGINA 41 PDF 6

from scipy.stats import norm,chi2
import numpy as np
a=0.05
faces=np.array([1,2,3,4,5,6])
Ni=np.array([20,7,12,18,20,23])
p0=1/6                              #probabilità dado pk0 dalle slide


n=np.sum(Ni)                        #mi calcolo la somma di tutti i lanci, Nk dalle slide
pk=Ni/n                             #mi calcolo la probabilità per ogni numero che è uscito, pk medio dalle slide

T=n * np.sum((pk-p0)**2)/p0         #applico la formuila Tn che si trova a pagina 38 (ho tutti i dati sia pk medio che p0)
print("T_test 1)",T)
chi=chi2.ppf(1-a,5)                 #calcolo il chi2 da confrontare con il valore T, dalle slide a pagina 40
print("chi: ", chi)
if(T > chi):                        #test chi2 a pagina 40 pdf 6
    print("rigettiamo l'ipotesi")
else:
    print("non possiamo respingere l'ipotesi")

Ni2=np.array([388,322,314,316,344,316])                 #da qui ri eseguo esattamente tutti i passaggi di prima cambiando solo le variabili in quanto ho un array diverso

a=0.01                          
n=np.sum(Ni2)
pk=Ni2/n
T=n * np.sum((pk-p0)**2)/p0
print("T_test 2:", T)
chi=chi2.ppf(1-a,5)
print("chi: ", chi)
if(T > chi):
    print("rigettiamo l'ipotesi")
else:
    print("non possiamo respingere l'ipotesi")