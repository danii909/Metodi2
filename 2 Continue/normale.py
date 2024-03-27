ESERCIZIO (a pagina 9 del pdf Variabili_aleatorie_continue.pdf si legge meglio )
Un lago riceve acqua da due immissari e alimenta un emissario. Misurando la portata in base alla variazione di quota dell'acqua, i due immissari immettono con legge X1 ~ N (2,2) mentre l'emissario viene alimentato con legge X3 ~ N(3/2, 3). Si determini la legge seguita dall'altezza dell'acqua. Qual è la probabilità che la quota superi il livello di guardia pari a 2= Qual e la probabilita che la quota sia inferiore a 0.5? 

from scipy.stats import norm
import numpy as np

X=1+2-3/2
#Y=1+2-3 #ma essendo al quadrato la varianza diventa tutto una somma  dunque: 
Y=1+2+3
print("legge seguita dall'acqua N(",X,",",Y,")")

#2
x=norm.sf(2,X,np.sqrt(Y))
print("2) ",x)

#3
y=norm.cdf(0.5,X,np.sqrt(Y))
print("3)",y)