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


Bonus: I also plotted the 2D trajectory (x vs y) and computed the speed over time from vx and vy using the same gradient approach.

## PW2 - Lab B: Optimization

### Part 2 — Three routes to a minimum

### 2A

All three methods reached x ≈ 3 from x0 = 0, so they agree on the minimum.

### 2B

From x0 = 0:

* Gradient descent: x ≈ -1.30084
* Newton: x ≈ 0.16994, maximum
* SLSQP: x ≈ -1.30086

From x0 = 2:

* Gradient descent: x ≈ 1.13090
* Newton: x ≈ 1.13090, minimum
* SLSQP: x ≈ -1.30064

The methods do not always agree. The starting point affects the result, especially for Newton's method. Newton can find a stationary point that is a maximum rather than a minimum.

### Part 3 — Reaction Rate Fitting

The fitted rate constant was **k ≈ 0.26176**, which is close to the expected value of 0.25. The fitted exponential curve follows the measured concentration data.

### Part 4 — Chemical Equilibrium

For the reaction H2 + I2 ⇌ 2HI, both Newton's method and SLSQP gave approximately the same equilibrium extent:

* Newton: x ≈ 0.66385
* SLSQP: x ≈ 0.66385
* They agree: True

Equilibrium amounts:

* H2 ≈ 0.33615 mol
* I2 ≈ 0.33615 mol
* HI ≈ 1.32770 mol

The result agrees with the expected x ≈ 0.66 and HI ≈ 1.33 mol.

### Part 5 — Titration Equivalence Point

The equivalence point was found by calculating the slope of the pH curve using `np.gradient` and finding its maximum with `np.argmax`.

* Equivalence point: **50.0 mL**
* The result agrees with the expected value of about 50 mL.
* The pH curve and its slope were plotted and saved as `titration.png`.

# Practical Work 3: Data, Distributions, Testing, and Causation

## Objective

The objective of this practical work is to perform statistical analysis on two datasets using Python. The analysis includes descriptive statistics, distributions, normality tests, group comparisons, correlation, and the difference between correlation and causation.

## Tools and Libraries

- Python
- Pandas
- Matplotlib
- SciPy

## Datasets

### 1. Heart Disease Dataset

The Cleveland heart disease dataset is used to analyze patient characteristics and investigate differences between healthy individuals and individuals with heart disease.

### 2. Chemicals and Cancer Dataset

This dataset contains the following variables:

- Benzene
- Cadmium
- Pollution index
- Age
- Malignancy

It is used to investigate relationships between chemical exposure indicators and malignancy.

## Analysis

### Task 1: Load the Heart Disease Dataset

The dataset is loaded using Pandas. Missing values are removed before analysis.

### Task 2: Descriptive Statistics

The mean, standard deviation, minimum, maximum, and quartiles are calculated for selected variables.

### Task 3: Distributions and Normality Tests

Histograms are created to visualize distributions. The Shapiro-Wilk test is used to assess normality.

### Task 4: Comparison of Two Groups

Maximum heart rate is compared between healthy individuals and individuals with heart disease using the Mann-Whitney U test.

### Task 5: Correlation Analysis

Spearman correlation is calculated to investigate the relationship between age and maximum heart rate.

### Task 6: Load the Chemicals and Cancer Dataset

The chemicals and cancer dataset is loaded using Pandas.

### Task 7: Descriptive Statistics

Descriptive statistics are calculated for the dataset variables.

### Task 8: Distributions and Normality Tests

Histograms and Shapiro-Wilk tests are used to examine the distributions.

### Task 9: Correlation Analysis

A correlation matrix is calculated. Spearman correlation is used to examine the relationship between pollution index and malignancy.

### Task 10: Correlation vs Causation

The results are interpreted carefully. A strong correlation does not necessarily mean that one variable causes changes in another.

## Results

- The selected heart disease variables do not follow normal distributions according to the Shapiro-Wilk tests.
- Maximum heart rate differs significantly between the healthy and disease groups (Mann-Whitney U test, p < 0.001).
- Age and maximum heart rate show a negative association (Spearman correlation approximately -0.393).
- Pollution index and malignancy show a strong positive association (Spearman correlation approximately 0.900).
- These associations do not, by themselves, establish causation.

## Generated Figures

The analysis generates the following figures:

- `distributions.png`
- `heart_rate_comparison.png`
- `age_thalach.png`
- `chemicals_distributions.png`
- `pollution_malignancy.png`

## How to Run

Activate the Conda environment:

```bash
conda activate cspc
