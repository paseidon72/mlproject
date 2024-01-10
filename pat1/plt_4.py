import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 11)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
# ax.plot(x, x, color='red', lw=3, linestyle='--')
# ax.plot(x, x, color='blue', lw=3, linestyle='--')
# lines = ax.plot(x, x+1, color='blue', lw=3)
# lines[0].set_dashes([1, 2, 1, 2, 10, 2])
ax.plot(x, x, color='blue', lw=2, marker='o', linestyle='--', ms=10,
        markerfacecolor='red', markeredgewidth=4, markeredgecolor='orange')
#ax.plot(x, x+1, color='blue', lw=2, marker='+', linestyle='-.', ms=20)
# ax.plot(x, x, label='X vc X')
# ax.plot(x, x**2, label='X vc X^2')
# ax.legend()
plt.show()