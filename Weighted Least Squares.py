import numpy as np
import matplotlib.pyplot as plt

# Read in data
file_path = "coursework_dataset.txt"
data = []
with open(file_path, 'r') as file:
    for line in file:
        value = float(line.strip())
        data.append(value)

b = data
n = len(b)  # Size of the dataset
A = np.eye(n)

# Create the bidiagonal matrix L
L = np.diag(-np.ones(n)) + np.diag(np.ones(n - 1), 1)
L = L[:n-1, :n]

# Set the regularisation parameters (lambda)
λ_values = [1, 10, 100, 1000]

# Set the weight update tolerance
δ = 1e-5

# Set number of iterations
iterations = 100

# Plot original data
plt.figure(figsize=(10, 6))
plt.plot(b, label='Original Data', color='b')


# Solution for weighted least squares
def solve_RLS(A, W, b):
    return np.linalg.inv(A.T @ W @ A) @ A.T @ W @ b


# Implement the algorithm
for λ in λ_values:

    # Initialise the weights
    w = np.ones(2*n-1)
    W = np.diag(w)

    # Augment A, b to get A^ and b^
    A_hat_λ = np.vstack([np.eye(n), np.sqrt(λ)*L])
    b_hat = np.hstack([b, np.zeros(n-1)])
    for iteration in range(iterations):

        x = solve_RLS(A_hat_λ, W, b_hat)

        # Update the weights vector 'w'
        w = 1 / np.maximum(δ, np.abs(np.dot(A_hat_λ, x) - b_hat))
        W = np.diag(w)

    # Plot the denoised data for the current λ
    plt.plot(x, label=f'Denoised Data (λ = {λ})')

plt.xlabel('Data Point Index')
plt.ylabel('Value')
plt.title('Original Data vs. Denoised Data for Different λ Values')
plt.legend()
plt.show()
