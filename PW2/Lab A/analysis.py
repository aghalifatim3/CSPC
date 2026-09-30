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

t, y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?

v = np.gradient(y, t)
a = np.gradient(v, t)

print("Mean acceleration:", np.mean(a))
print("Std of acceleration:", np.std(a))

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0] 
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]
diff = np.abs(y_recovered - y) 
print("Max difference:", np.max(diff))

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 9), sharex=True)

ax1.plot(t, y)
ax1.set_ylabel("position (m)")
ax1.set_title("Position")

ax2.plot(t, v)
ax2.set_ylabel("velocity (m/s)")
ax2.set_title("Velocity")

ax3.plot(t, a)
ax3.axhline(-9.81, color="red", linestyle="--", label="-9.81 m/s2")
ax3.set_ylabel("acceleration (m/s2)")
ax3.set_xlabel("time (s)")
ax3.set_title("Acceleration")
ax3.legend()

plt.tight_layout()
plt.savefig("motion.png")

t2, x, y2 = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1, unpack=True)

plt.figure()
plt.plot(x, y2)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Trajectory path")
plt.savefig("trajectory_path.png")

vx = np.gradient(x, t2)
vy = np.gradient(y2, t2)
speed = np.sqrt(vx**2 + vy**2)

plt.figure()
plt.plot(t2, speed)
plt.xlabel("time (s)")
plt.ylabel("speed (m/s)")
plt.title("Speed over time")
plt.savefig("speed_over_time.png")