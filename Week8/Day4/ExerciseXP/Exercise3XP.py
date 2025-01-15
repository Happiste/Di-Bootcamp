from statsmodels.stats.power import TTestIndPower


alpha = 0.05       
effect_size = 0.2  
power_levels = [0.7, 0.8, 0.9] 

analysis = TTestIndPower()

sample_sizes_by_power = {
    power_level: analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power_level, alternative='two-sided')
    for power_level in power_levels
}


for power_level, sample_size in sample_sizes_by_power.items():
    print(f"Power level {power_level}: Required sample size per group = {sample_size:.2f}")
