"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)

t = data[:, 0]
y = data[:, 1]
# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)

print("Mean acceleration:", np.mean(a))
print("Standard deviation:", np.std(a))
# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]

y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]
# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Position
axes[0].plot(t, y, label="Measured position")
axes[0].plot(t, y_recovered, label="Recovered position")
axes[0].set_ylabel("Position (m)")
axes[0].legend()
axes[0].grid()

# Velocity
axes[1].plot(t, v, label="Measured velocity")
axes[1].plot(t, v_recovered, label="Recovered velocity")
axes[1].set_ylabel("Velocity (m/s)")
axes[1].legend()
axes[1].grid()

# Acceleration
axes[2].plot(t, a, label="Measured acceleration")
axes[2].axhline(-9.81, linestyle="--", label="True -9.81 m/s²")
axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Acceleration (m/s²)")
axes[2].legend()
axes[2].grid()

plt.tight_layout()
plt.savefig("motion.png")
plt.show()
# Bonus: 2D tracked trajectory

trajectory = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)

t2 = trajectory[:, 0]
x = trajectory[:, 1]
y2 = trajectory[:, 2]

vx = np.gradient(x, t2)
vy = np.gradient(y2, t2)

speed = np.sqrt(vx**2 + vy**2)

fig2, axes2 = plt.subplots(2, 1, figsize=(8, 8))

# 2D trajectory
axes2[0].plot(x, y2)
axes2[0].set_xlabel("x")
axes2[0].set_ylabel("y")
axes2[0].set_title("2D Tracked Trajectory")
axes2[0].grid()

# Speed vs time
axes2[1].plot(t2, speed)
axes2[1].set_xlabel("Time (s)")
axes2[1].set_ylabel("Speed")
axes2[1].set_title("Speed vs Time")
axes2[1].grid()

plt.tight_layout()
plt.savefig("trajectory.png")
plt.show()
