import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 10, 11)
b = a ** 4
x = np.arange(0, 10)
y = 2 * x
fig = plt.figure(figsize=(2, 2), dpi=100)
axes1 = fig.add_axes([0, 0, 1, 1])
axes1.plot(a, b)
fig.savefig('fig.png', bbox_inches='tight')
# axes1.set_xlim(0, 8)
# axes1.set_ylim(0, 8000)
# axes1.set_xlabel('A')
# axes1.set_ylabel('B')
# axes1.set_title('Возведение в степень 4')
# axes2 = fig.add_axes([0.2, 0.2, 0.5, 0.5])
# axes2.plot(a, b)
# axes2.set_xlim(1, 2)
# axes2.set_ylim(0, 50)
# axes2.set_xlabel('A')
# axes2.set_ylabel('B')
# axes2.set_title('Увеличений фрагмент')
plt.show()
