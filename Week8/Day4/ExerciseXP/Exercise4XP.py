from statsmodels.stats.proportion import proportions_ztest

# Weekly data (hypothetical)
data = [
    {"week": 1, "success_A": 50, "n_A": 500, "success_B": 60, "n_B": 500},
    {"week": 2, "success_A": 120, "n_A": 1000, "success_B": 140, "n_B": 1000},
    {"week": 3, "success_A": 200, "n_A": 1500, "success_B": 240, "n_B": 1500},
]

# Adjusted significance level for sequential testing
alpha = 0.05 / len(data)  # Bonferroni correction

# Evaluate each week
for entry in data:
    week = entry["week"]
    count = [entry["success_A"], entry["success_B"]]
    nobs = [entry["n_A"], entry["n_B"]]
    stat, p_value = proportions_ztest(count, nobs)

    print(f"Week {week}: p-value = {p_value:.4f}")
    if p_value < alpha:
        print(f"Significant result detected at week {week}. Stop the test.")
        break
else:
    print("No significant result detected after all weeks.")
