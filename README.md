# CSPC - Computer Science for Physics and Chemistry
## What I built
- Set up a Conda environment for the lab
- Created a radioactive decay simulation with Python and NumPy
- Added tests to check the simulation
## Speed comparison (loop vs NumPy)
- loop: 1.9989 s
- NumPy: 0.0002 s
- speed-up: 11818.45x
## Tests
All tests passing? Yes
## Conclusion
- All three tests passed successfully
- The NumPy implementation was much faster than the Python loop
- This lab helped me practice Git, GitHub, Conda, NumPy, and pytest

## PW1 — Lab B

The observed decay data showed a decreasing trend in the number of counts over time. The observed data generally followed the analytical exponential decay curve, with some small differences between the measured values and the model.
The Snakemake pipeline takes `decay_observed.csv` as input, runs `plot.py`, and produces `figure.png` as the output.