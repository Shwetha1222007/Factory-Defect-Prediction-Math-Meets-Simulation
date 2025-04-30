import random

# Inputs
N = 10000
p = 0.004

# Simulation
defective_simulated = sum(1 for _ in range(N) if random.random() < p)

# Expected value
expected_defective = N * p

# Percentage error
error_percentage = abs(defective_simulated - expected_defective) / expected_defective * 100

# Output
print(f"Simulated defective count: {defective_simulated}")
print(f"Expected defective count: {expected_defective}")
print(f"Percentage error: {error_percentage:.2f}%")