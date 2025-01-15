
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt

alpha_prior, beta_prior = 1, 1


successes, failures = 65, 35

alpha_posterior = alpha_prior + successes
beta_posterior = beta_prior + failures


x = np.linspace(0, 1, 100)
prior = beta.pdf(x, alpha_prior, beta_prior)
posterior = beta.pdf(x, alpha_posterior, beta_posterior)

plt.plot(x, prior, label='Prior', linestyle='--')
plt.plot(x, posterior, label='Posterior', color='blue')
plt.title('Prior vs. Posterior Distribution')
plt.xlabel('Engagement Rate')
plt.ylabel('Density')
plt.legend()
plt.show()


posterior_mean = alpha_posterior / (alpha_posterior + beta_posterior)
print(f"Posterior mean: {posterior_mean:.2f}")
