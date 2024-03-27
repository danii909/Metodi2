Un motore a reazione `e formato legando insieme un propellente di accensione e un propellente
di sostegno all’interno di un alloggiamento metallico. La resistenza al taglio del legame tra i
due tipi di propellente `e una caratteristica importante.
Vogliamo testare l’ipotesi che la mediana della resistenza al taglio sia 2000 psi con una signi-
ficativit`a α = 0.05.
I dati sono riportati nel file Dataset motore.dat

from scipy.stats import binom
import numpy as np
med = 2000
a = 0.05
n=200
R=binom.pmf(n,1/2,a)
print(R)
