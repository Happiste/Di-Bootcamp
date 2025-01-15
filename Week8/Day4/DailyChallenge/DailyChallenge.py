from statsmodels.stats.power import TTestIndPower

# Parameters for the test
current_conversion = 0.05  # Current conversion rate
new_conversion = 0.07      # Expected conversion rate with the new process
effect_size = 0.2          # Cohen's d
alpha = 0.05               # Significance level
power = 0.8                # Desired power

# Initialize the power analysis object
analysis = TTestIndPower()

# Calculate required sample size for the specified effect size
sample_size_for_effect_size_02 = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='two-sided')

# Analyze the impact of different effect sizes
effect_sizes = [0.1, 0.2, 0.3, 0.4]
sample_sizes_by_effect_size = {
    es: analysis.solve_power(effect_size=es, alpha=alpha, power=power, alternative='two-sided')
    for es in effect_sizes
}

# Print results
print(f"Sample size required for effect size 0.2: {sample_size_for_effect_size_02:.2f}")
print("Sample sizes for varying effect sizes:")
for es, sample_size in sample_sizes_by_effect_size.items():
    print(f"Effect size {es}: Required sample size = {sample_size:.2f}")


# As the effect size increases, the required sample size decreases.
# A larger effect size means the difference between groups is more pronounced and easier to detect, requiring fewer observations.

