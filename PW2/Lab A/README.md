# PW2 Lab A — Motion from Tracking Data

## Results

The noisy free-fall position data were differentiated to obtain velocity and acceleration.

The mean acceleration was:

- Mean acceleration: -8.58 m/s²
- Standard deviation: 28.72 m/s²

The expected gravitational acceleration is -9.81 m/s². The calculated mean acceleration is reasonably close to this value, but the acceleration data are quite noisy.

The noise becomes more noticeable after differentiation. This is because numerical differentiation can amplify small variations and measurement noise in the position data. The second differentiation, used to obtain acceleration, makes this effect even stronger.

The acceleration was then integrated back to recover velocity and position.

## Files

- `analysis.py` — analysis and plotting code
- `freefall.csv` — free-fall tracking data
- `trajectory.csv` — 2D tracking data for the bonus task
- `motion.png` — position, velocity, and acceleration plots
