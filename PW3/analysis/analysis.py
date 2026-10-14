import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Heart disease dataset
heart_file = BASE_DIR / "heart+disease" / "processed.cleveland.data"

columns = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "restecg", "thalach", "exang",
    "oldpeak", "slope", "ca", "thal", "num"
]

heart = pd.read_csv(
    heart_file,
    header=None,
    names=columns,
    na_values="?"
)

heart = heart.dropna()

print("Heart disease dataset")
print("Dataset shape:", heart.shape)
print(heart.head())

heart["disease"] = (heart["num"] > 0).astype(int)

# Descriptive statistics
variables = ["age", "trestbps", "chol", "thalach"]

print("\nDescriptive statistics")
print(heart[variables].describe())

# Distributions and normality tests
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for ax, variable in zip(axes.flatten(), variables):
    ax.hist(heart[variable], bins=20, edgecolor="black")
    ax.set_title(f"Distribution of {variable}")
    ax.set_xlabel(variable)
    ax.set_ylabel("Frequency")

plt.tight_layout()
plt.savefig(BASE_DIR / "distributions.png")
plt.close()

print("\nNormality tests")

for variable in variables:
    statistic, p_value = stats.shapiro(heart[variable])
    print(f"{variable}: p-value = {p_value:.6f}")

    if p_value < 0.05:
        print("The distribution is not normal.")
    else:
        print("No significant evidence against normality.")

# Compare two groups
print("\nHeart rate comparison")

healthy = heart.loc[heart["disease"] == 0, "thalach"]
disease = heart.loc[heart["disease"] == 1, "thalach"]

print("Healthy group size:", len(healthy))
print("Disease group size:", len(disease))
print("Healthy mean:", healthy.mean())
print("Disease mean:", disease.mean())
print("Healthy standard error:", stats.sem(healthy))
print("Disease standard error:", stats.sem(disease))

u_statistic, p_value = stats.mannwhitneyu(
    healthy,
    disease,
    alternative="two-sided"
)

print("Mann-Whitney U statistic:", u_statistic)
print("P-value:", p_value)

if p_value < 0.05:
    print("The two groups differ significantly.")
else:
    print("No statistically significant difference was found.")

plt.figure(figsize=(8, 5))
plt.boxplot([healthy, disease], tick_labels=["Healthy", "Disease"])
plt.ylabel("Maximum heart rate")
plt.title("Maximum Heart Rate by Disease Group")
plt.tight_layout()
plt.savefig(BASE_DIR / "heart_rate_comparison.png")
plt.close()

# Correlation analysis
print("\nAge and maximum heart rate")

correlation, p_value = stats.spearmanr(
    heart["age"],
    heart["thalach"]
)

print("Spearman correlation:", correlation)
print("P-value:", p_value)

if p_value < 0.05:
    print("There is a statistically significant association.")
else:
    print("No statistically significant association was found.")

plt.figure(figsize=(8, 5))
plt.scatter(heart["age"], heart["thalach"], alpha=0.6)
plt.xlabel("Age")
plt.ylabel("Maximum heart rate")
plt.title("Age vs Maximum Heart Rate")
plt.tight_layout()
plt.savefig(BASE_DIR / "age_thalach.png")
plt.close()

# Chemicals and cancer dataset
print("\nChemicals and cancer dataset")

chemicals_file = BASE_DIR / "chemicals_cancer.csv"
chemicals = pd.read_csv(chemicals_file)

print("Dataset shape:", chemicals.shape)
print(chemicals.head())

# Descriptive statistics
chemical_variables = [
    "benzene",
    "cadmium",
    "pollution_index",
    "age",
    "malignancy"
]

print("\nDescriptive statistics")
print(chemicals.describe())

# Distributions and normality tests
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

for ax, variable in zip(axes.flatten(), chemical_variables):
    ax.hist(chemicals[variable], bins=20, edgecolor="black")
    ax.set_title(f"Distribution of {variable}")
    ax.set_xlabel(variable)
    ax.set_ylabel("Frequency")

axes.flatten()[-1].set_visible(False)

plt.tight_layout()
plt.savefig(BASE_DIR / "chemicals_distributions.png")
plt.close()

print("\nNormality tests")

for variable in chemical_variables:
    statistic, p_value = stats.shapiro(chemicals[variable])
    print(f"{variable}: p-value = {p_value:.6f}")

    if p_value < 0.05:
        print("The distribution is not normal.")
    else:
        print("No significant evidence against normality.")

# Correlation analysis
print("\nCorrelation matrix")
print(chemicals[chemical_variables].corr())

print("\nPollution index and malignancy")

correlation, p_value = stats.spearmanr(
    chemicals["pollution_index"],
    chemicals["malignancy"]
)

print("Spearman correlation:", correlation)
print("P-value:", p_value)

if p_value < 0.05:
    print("Pollution index and malignancy are significantly associated.")
else:
    print("No statistically significant association was found.")

plt.figure(figsize=(8, 5))
plt.scatter(
    chemicals["pollution_index"],
    chemicals["malignancy"],
    alpha=0.6
)
plt.xlabel("Pollution Index")
plt.ylabel("Malignancy")
plt.title("Pollution Index vs Malignancy")
plt.tight_layout()
plt.savefig(BASE_DIR / "pollution_malignancy.png")
plt.close()

# Correlation does not mean causation
print("\nCorrelation vs causation")
print("Pollution index and malignancy are strongly associated in this dataset.")
print("However, correlation alone does not prove that pollution causes malignancy.")
print("Other variables or confounding factors may explain part of the association.")

print("\nAnalysis complete. All figures have been saved.")