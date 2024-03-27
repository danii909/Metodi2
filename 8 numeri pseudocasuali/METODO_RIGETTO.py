Eseguire un confronto statistico tra i numeri generati e la distribuzione teorica (x >= -pi and x < pi)

def f(x):
    if 0 <= x and x <= 2:
        return (-3/4) * x**2 + (3/2) * x
    else:
        return 0
    
def max_f(f, a, b):
    x = np.linspace(a, b, 1000)
    y = [f(i) for i in x]
    return max(y)

a = 0
b = 2
M = max_f(f, a, b)

def rigetto(f, a, b, M, N):
    arr = []
    while len(arr) < N:
        x = np.random.uniform(a, b)
        y = np.random.uniform(0, M)
        if 0 <= y and y <= f(x):
            arr.append(x)
    return arr

N = 10**5
arr = rigetto(f, a, b, M, N)

xx = np.linspace(a, b, 1000)
yy = [f(i) for i in xx]

plt.plot(xx, yy, 'r')
plt.hist(arr, bins=100, density=True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()