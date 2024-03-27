Un macchinario riempie automaticamente delle bottiglie. Da un campione di 20 misurazioni si
ottengono i seguenti valori (in litri)
2.05, 2.04, 1.98, 1.96, 2.03, 2.01, 1.97, 1.99, 2.01, 2.05
1.96, 1.95, 2.04, 2.01, 1.97, 1.96, 2.02, 2.04, 1.98, 1.94
Se la varianza fosse troppo grande, la proporzione di bottiglie sotto o sovrariempite sarebbe non
accettabile.
Calcolare l’intervallo di confidenza al 95% per il limite superiore per la deviazione standard.

(PAG 47 PDF 5)

from scipy.stats import norm, chi2
import numpy as np

arr=np.array([2.05, 2.04, 1.98, 1.96, 2.03, 2.01, 1.97, 1.99, 2.01, 2.05,
              1.96, 1.95, 2.04, 2.01, 1.97, 1.96, 2.02, 2.04, 1.98, 1.94])

dev=np.std(arr, ddof=1)
var=dev**2
leng=np.size(arr)

print("Med: ", med)
print("dev std: ", dev)
print("var: ", var)

intconf= ((dev**2)*(leng-1))/(chi2.ppf(1-0.05,leng-1))
print(intconf)


Med:  1.9979999999999998
dev std:  0.03621572790057408
var:  0.0013115789473684197
0.0008267114803781897