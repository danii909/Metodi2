import numpy as np

P=np.array([[0,1/3,0,1/3,1/3],[1/3,0,1/3,0,1/3],[0,1/3,0,1/3,1/3],[1/3,0,1/3,0,1/3],[1/4,1/4,1/4,1/4,0]])


P2=P@P 

print(P2)
print("è regolare perchè esiste un esponente che rende ogni elemento della matrice maggiore di zero")

# metodo analtico per determinare la distr.

x,y=np.linalg.eig(P.T)  #trovo gli autovettori sinistri (pag 13)

print(np.real(x),"\n\n",np.real(y))
v=np.real(y[:,np.argmax(x)])/np.sum(np.real(y[:,np.argmax(x)]))

print("\n\n",v)

n=5
F=np.zeros(n)
j=np.random.randint(n)
F[j]=1
N = 100000
for i in range (N):
        j_multi= np.random.multinomial(1,P[j,:])
        j=np.nonzero(j_multi)[0][0]
        F[j]=F[j]+1
vv=F/N
print (vv)