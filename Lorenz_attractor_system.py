import numpy as np
from scipy.integrate import solve_ivp

import matplotlib.pyplot as plt

# Lorenz attractor system
def lorenz(t, state, sigma=10., beta=8/3, rho=28.):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

# Initial state and time span
state0 = [1.0, 1.0, 1.0]
t_span = (0, 40)
t_eval = np.linspace(*t_span, 10000)

# Solve ODE
sol = solve_ivp(lorenz, t_span, state0, t_eval=t_eval)

# Plotting the Lorenz attractor
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2], lw=0.5, color='navy')
ax.set_title("Lorenz Attractor")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()