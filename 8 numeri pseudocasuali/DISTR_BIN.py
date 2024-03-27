from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

arr=np.random.uniform(0,1,1000)
p=0.05

def X (y):

    if(y >= 0 and y < p):
        return 1
    else:
        return 0

arr2=[]

for i in range (1000):
    arr2.append(X(arr[i]))

print (arr2)

# Frequenze osservate
N_succ=np.sum(arr2)
N_insucc=1000-N_succ
print(N_succ,N_insucc)
# probabilità empiriche
P_succ= N_succ/1000
P_insucc=N_insucc/1000

print(P_succ,P_insucc)