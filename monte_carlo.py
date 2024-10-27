# import matplotlib.pyplot as plt
# import numpy as np
# import scipy.integrate as spi


# def f(x):
#     return np.sin(x)


# a, b = 0, 2
# n_points = 5000

# x = np.linspace(0, 6, 700)
# y = f(x)
# fig, ax = plt.subplots()
# ax.plot(x, y, 'r', linewidth=2)

# ix = np.linspace(a, b)
# iy = f(ix)
# ax.fill_between(ix, iy, color='gray', alpha=0.3)

# x_random = np.random.uniform(a, b, n_points)
# y_random = np.random.uniform(0, max(y), n_points)

# dots_under = y_random < f(x_random)
# aprox_integral = (dots_under.sum() / n_points) * (b - a) * max(y)
# integral = spi.quad(f, a, b)

# print(f'Визначений Інтеграл: {integral}')
# print(f'Наближене значення інтегралу: {aprox_integral}')

# ax.scatter(x_random, y_random, color='blue', s=1, alpha=0.3)
# ax.scatter(x_random[dots_under], y_random[dots_under],
#            color='green', s=1, alpha=0.3)

# ax.set_xlim([-0.5, 2.5])
# ax.set_ylim([0, max(y) + 0.5])
# ax.set_xlabel('x')
# ax.set_ylabel('f(x)')
# ax.set_title(
#     f'Обчислення площі під графіком f(x) = sin(x) методом Монте-Карло від {str(a)} до {str(b)}')
# plt.grid()
# plt.show()


import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    return np.sin(x)


a, b = 0, 2
n_points = 5000

x = np.linspace(0, 3, 500)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

x_random = np.random.uniform(a, b, n_points)
y_random = np.random.uniform(0, max(y), n_points)

dots_under = y_random < f(x_random)
aprox_integral = (dots_under.sum() / n_points) * (b - a) * max(y)
integral = spi.quad(f, a, b)

print(f'Визначений Інтеграл: {integral}')
print(f'Наближене значення інтегралу: {aprox_integral}')

ax.scatter(x_random, y_random, color='blue', s=1, alpha=0.3)
ax.scatter(x_random[dots_under], y_random[dots_under],
           color='green', s=1, alpha=0.3)

ax.set_xlim([0, 3])
ax.set_ylim([0, 1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(
    f'Обчислення площі під графіком f(x) = sin(x) методом Монте-Карло від {str(a)} до {str(b)}')
plt.grid()
plt.show()
