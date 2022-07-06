import numpy as np

low_n, hi_n = 500, 1001
low_m, hi_m = 10, 51

while True:
    n = input("Введите число n 500<N≤1000: ")
    try:
        n = int(n)
    except:
        print('Введите целое число')
        continue
    if n not in range(low_n, hi_n):
        print('Введите число в диапозоне 500 < n <= 1000')
        continue
    break

while True:
    m = input("Введите число m 10 < m ≤= 50: ")
    try:
        m = int(m)
    except:
        print('Введите целое число')
        continue
    if m not in range(low_m, hi_m):
        print('Введите число в диапозоне 10 < m <= 50')
        continue
    break

print((1 - (-1)) *np.random.sample((n, m)) - 1)
a = (1 - (-1)) *np.random.sample((n, m)) - 1
np.savetxt("vectors.csv", a, fmt = '%1.8f', delimiter=",")
