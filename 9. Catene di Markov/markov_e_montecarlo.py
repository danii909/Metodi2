import numpy as np
from scipy.stats import norm, binom
P = np.array([[0,1/4,3/4],
             [0,1/2,1/2],
             [3/4, 0, 1/4]])
n=3
print(P)


# Calcoliamo P^2
print(P@P)  #pagina 11 pdf 9, per vedere se una matrice di trnasizione è regolare: se esiste un intero m che noi poniamo a potenza di P tale che crei un altra matrice 
                    #dove ogni elemento è maggiore di zero allora essa è regolare, in questo caso stampiamo e vediamo che tutti gli elementi sono positivi

                    # per il teorema di Markov (pag 11) possiamo dire che una matrice di transizione regolare ha un unica distribuzione stazionaria pi, dunque abbiamo risposto al punto 1


#metodo analitico
w,v=np.linalg.eig(P.T)  #calcolo gli autovettori sinistri (pag 13): dice che gli autovettori destri di A.T sono uguali ai sinistri della stessa matrice
                        #dunque con linalg.eig calcolo gli auto vettori destri MA della matrice trasposta, dunque calcolo infine i sinistri
print(w,"\n\n",v)       # w sono gli autovalori !!! 

# a pagina 14 c'è scrittop che per determinare se una distribuzione è stazionaria dobbiamo soddisfare la relazione v=vP, dove v sono gli autovettori sinistri e P è la nostra matrice
# c'è scritto però che: Questa relazione è soddisfatta dagli autovettori sinistri di P corrispondenti all'autovalore 1,
# gli autovalori sono calcolati nel vettore w, l'1 lo troviamo solo nella seconda colonna, ovvero [:,1]

t=v[:,1]/np.sum(v[:,1])         #questa formula non è scritta esplicitamente nel pdf, ( sarebbe a pag 14 ma non è manco quella ), ergo, pizzino 
print(t)

# Metodo Monte Carlo

F = np.zeros(n)
j = np.random.randint(n)
F[j] = 1
N = 1000000
for i in range(N):
    j_multi = np.random.multinomial(1, P[j,:])
    j = np.nonzero(j_multi)[0][0]
    F[j] = F[j]+1
vv = F/N
display(vv)