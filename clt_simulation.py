import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a population (not normally distributed for fun!)
np.random.seed(42)
population = np.random.exponential(scale=50, size=10000)  # Skewed population

# Step 2: Sampling function
def generate_sample_means(sample_size, num_samples):
    means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size, replace=True)
        means.append(np.mean(sample))
    return means

# Step 3: Try different sample sizes
sample_sizes = [5, 20, 30, 50]
num_samples = 1000

# Step 4: Plot histograms of sample means
plt.figure(figsize=(15, 10))
for i, size in enumerate(sample_sizes, 1):
    sample_means = generate_sample_means(size, num_samples)
    plt.subplot(2, 2, i)
    plt.hist(sample_means, bins=30, color='skyblue', edgecolor='black')
    plt.title(f'Sample Size = {size}')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.suptitle("Central Limit Theorem Simulation", fontsize=16, y=1.02)
plt.show()
