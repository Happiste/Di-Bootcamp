from statsmodels.stats.power import TTestIndPower

# Define parameters for the test
effect_size = 0.3  # Expected effect size
alpha = 0.05       # Significance level
power = 0.8        # Power of the test

# Initialize the power analysis object
analysis = TTestIndPower()

# Calculate the required sample size per group
sample_size_per_group = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='two-sided')

print(f"Required sample size per group: {sample_size_per_group:.2f}")
