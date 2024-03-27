La memoria di un computer è composta da 30 hard disk ognuno dei quali contiene 100 file. Un programma dovrà accedere a 28 di questi file (tutti diversi)
1) QUal e la probabilità che non ci siano file proveniendi dall hard disk 1?
2) Qual e la probabilità del punto 1) nel caso in cui i file possano ripetersi? 

from scipy.stats import hypergeom, binom
a=30
b=100
f=28
dim=100*30
x=hypergeom.pmf(0,dim,100,28) #devono esserci 0 successi nei 100 file dell'hard disk 1
print(x)
>0.38534529585831134

y=binom.pmf(0,28,1/30) #usiamo binom perchè vi è il reinserimento, 0 è il numero di successi che vogliamo per 28 file letti, dove vi è 1/30 possibilità che l'hard disk 1 venga letto
print(y)
>0.3870337242752073