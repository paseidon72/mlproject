import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10)
y = 2 * x
df = plt.plot(x, y)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Название')
plt.xlim(0, 6)
plt.ylim(0, 15)
plt.savefig('myfig.png')
plt.show()
print(df)