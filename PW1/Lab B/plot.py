import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3

# Read observed data
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# Set N0 to the first observed value
N0 = observed[0]

# Analytical decay law
analytical = N0 * np.exp(-LAMBDA * t)

# Create 1x2 subplots with shared axes
fig, axes = plt.subplots(1, 2, sharex=True, sharey=True)

# Observed data
axes[0].scatter(t, observed)
axes[0].set_title("Observed data")
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Count")

# Analytical curve
axes[1].plot(t, analytical)
axes[1].set_title("Analytical")
axes[1].set_xlabel("Time")

# Save figure
plt.savefig("figure.png")
