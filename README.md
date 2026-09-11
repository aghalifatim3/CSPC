# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
    conda env create -f PW<n>/Lab <X>/environment.yml
    conda activate cspc


## PW1 - Lab A: Reproducible Foundations

What I built:
I set up the CSPC repo with a conda environment, wrote a radioactive decay simulation, added tests for it, and compared how fast the loop version runs against the NumPy version.

Speed comparison (loop vs NumPy):
- loop  : 2.7542 s
- numpy : 0.0003 s
- speed-up: about 9676x faster

Tests: all passing, yes

Conclusion:
NumPy was way faster than I expected,mostly because it handles all the atoms at once instead of going through them one by one like the loop does.This lab also helped me get more comfortable with git branching and merging,since I hadn't really practiced that hands-on before.