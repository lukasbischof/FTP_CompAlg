import numpy as np
import matplotlib.pyplot as plt

A = 1


def F(z):
    return 1 + z + 0.5 * z**2


granularity = 300
X, Y = np.meshgrid(np.linspace(-2, 2, granularity), np.linspace(-2j, 2j, granularity))
Z = F(A * (X + Y))

stable_region = np.abs(Z) < 1

plt.imshow(stable_region, extent=[-2, 2, -2, 2])
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.title("Stable region for the function $F(z) = 1 + z + 0.5z^2$")
plt.grid()
plt.show()
