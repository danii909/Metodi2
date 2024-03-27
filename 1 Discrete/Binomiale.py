Una ditta produce lampadine, di cui il 5% risulta difettoso, e le vende in confezioni da quattro.
1) Qual e la probabilita che in una confezione ci sia una sola lampadina difettosa?
2) Qual e la probabilita che in una confezione ci siano al più due pezzi difettosi
3) Se ogni scatola contiene 40 pezzi, quanti pezzi difettosi conterrebbe in media?

#1
from scipy.stats import binom
stat=5/100
x=binom.pmf(1,4,stat)  #pmf = P(X = x)
print(x)
>0.17147500000000013

#2
y=binom.cdf(2,4,stat)  #cdf = P(X <= x)
print(y)
>0.99951875

#3 chiede letteralmente la media
z=40*stat
print(z)
>2.0