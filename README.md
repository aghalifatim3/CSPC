# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW/Lab folders.

## Setup

Create the environment for a given lab:

    conda env create -f environment.yml
    conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- Set up the CSPC repo with a conda environment, wrote a radioactive decay simulation, added tests for it, and compared how fast the loop version runs against the NumPy version.

**Speed comparison (loop vs NumPy):**
- loop: 2.7542 s
- numpy: 0.0003 s
- speed-up: about 9676x faster

**Tests:** all passing? yes

**Conclusion:**
- NumPy was way faster than I expected, mostly because it handles all the atoms at once instead of going through them one by one like the loop does. This lab also helped me get more comfortable with git branching and merging, since I hadn't really practiced that hands-on before

---

## PW1 - Lab B: Data, Plotting, and Automation

What the data showed:
The counts start around 5000 and drop off fast at the beginning, then slow down and flatten out toward the end.

Did it match the analytical law?
Yes, pretty closely. When I compared the two plots side by side, the observed points followed the same curve shape as the analytical exponential decay.

Snakemake pipeline:
The Snakefile has one rule that runs plot.py to build figure.png from the csv file, and it only reruns if the csv changes.

---

## PW2 - Lab A: Motion from Tracking Data

Mean acceleration measured: about -8.58 m/s2 (close to -9.81, the small difference comes from noise).

Why the acceleration was noisy: acceleration comes from taking the derivative twice, and each derivative amplifies measurement noise, so by the second derivative the noise dominates even though the position data looked smooth.

What integrating back showed: integrating the noisy acceleration back up recovered the position within about 0.78 meters of the original, showing that integration suppresses noise instead of amplifying it.