import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 10, 11)
b = a ** 4
x = np.arange(0, 10)
y = 2 * x
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0][0].plot(x, y)
axes[0][1].plot(x, y)
axes[0][1].set_xlabel('A')
axes[1][0].plot(x, y)
axes[1][1].plot(a, b)
axes[1][1].set_title('Title')
fig.suptitle('Title')
plt.tight_layout()
#fig.subplots_adjust(wspace=0.5, hspace=0.5)
fig.savefig('figure.png', bbox_inches='tight')

plt.show()