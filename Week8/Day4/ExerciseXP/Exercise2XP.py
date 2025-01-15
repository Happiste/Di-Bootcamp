from statsmodels.stats.power import TTestIndPower

alpha = 0.05   
power = 0.8     
effect_sizes = [0.2, 0.4, 0.5]  


analysis = TTestIndPower()

sample_sizes = {
    effect_size: analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='two-sided')
    for effect_size in effect_sizes
}

# Print results
for effect_size, sample_size in sample_sizes.items():
    print(f"Effect size {effect_size}: Required sample size per group = {sample_size:.2f}")
