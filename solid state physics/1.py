import numpy as np
from matplotlib import pyplot as plt

n = np.arange(1, 20, 1)
alpha = []
for x in n:
    a = 0
    for i in range(-x, x):
        for j in range(-x, x):
            for k in range(-x, x):
                if i == 0 and j == 0 and k == 0:
                    a = a
                else:
                    a = a+((-1)**(i+j+k+1))/((i**2+j**2+k**2)**(1/2))
    alpha.append(a)



plt.subplots()
plt.plot(n,alpha)
plt.show()
