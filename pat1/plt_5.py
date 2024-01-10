import matplotlib.pyplot as plt
import numpy as np

#m = np.linspace(0, 10, 11)
# c = 3 * 10**8
# E = m * c**2
# plt.plot(m, E, color='red', lw=5)
# plt.title('E = mc^2')
# plt.xlabel('маса в грамах')
# plt.ylabel('єнергия в джоулях')
# plt.xlim(0, 10)
# plt.yscale('log')
# plt.grid(which='both', axis='y')
""""""

# fig = plt.figure()
# axes = fig.add_axes([0, 0, 1, 1])
labels = ['1 Mo', '3 Mo', '6 Mo', '1 Yr', '2 Yr', '3 Yr', '5 Yr', '7 Yr', '10 Yr', '20 Yr', '30 Yr']
july16_2007 = [4.75, 4.98, 5.08, 5.01, 4.89, 4.89, 4.95, 5.05, 5.21, 5.14]
july16_2020 = [0.12, 0.11, 0.13, 0.14, 0.16, 0.17, 0.28, 0.46, 0.62, 1.09, 1.31]
# axes.plot(labels, july16_2007, label='july16_2007')
# axes.plot(labels, july16_2020, label='july16_2020')
# axes.legend();
# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 8))
# axes[0].plot(labels, july16_2007)
# axes[0].set_title('july16_2007')
# axes[1].plot(labels, july16_2020)
# axes[1].set_title('july16_2020')
fix, ax1 = plt.subplots(figsize=(12, 8))
ax1.plot(labels, july16_2007, lw=2, color='blue')
ax1.set_ylabel('july16_2007', fontsize=18, color='blue')
for label in ax1.yticklabels():
    label.set_color("blue")
ax2 = ax1.twinx()
ax2.plot(labels, july16_2007, lw=2, color='red')
ax2.set_ylabel('july16_2007', fontsize=18, color='red')
for label in ax2.yticklabels():
    label.set_color("red")
plt.show()