import numpy as np
import math
import matplotlib.pyplot as plt

x00 = 1
t0 = [1.9, 2.0, 2.2, 2.3]
t = [0, 0, 0, 0]
y = [0, 0, 0, 0]

for i in range(len(t0)):
    t[i] = np.arange(t0[i], t0[i] + 2.2, 0.002)
    i = i + 1

for i in range(len(t0)):
    y[i]=x00*np.exp(4*t0[i]*np.cos(t0[i]) - 4*np.sin(t0[i]) + t0[i]**2)*np.exp(4*np.sin(t[i]) - 4*t[i]*np.cos(t[i]) - t[i]**2)
    i = i + 1

for i in range(len(t0)):
    plt.plot(t[i], y[i], label="t_0=" + str(t0[i]), linestyle="solid")
    i = i + 1

plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("x(t)")
plt.legend()  # 打上标签
plt.show()


