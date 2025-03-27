# src/sbm/run_pipeline.py

import numpy as np
from sbm import DCSBM, SBM

# Generate a toy adjacency matrix (undirected, binary)
A = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
])

# Number of communities to fit
K = 2

# Choose model type
USE_DEGREE_CORRECTION = True

# Initialize and run model
if USE_DEGREE_CORRECTION:
    model = DCSBM(A, K)
    print("Running Degree-Corrected SBM...")
else:
    model = SBM(A, K)
    print("Running Standard SBM...")

model.fit()

# Show results
print("Group assignments:", model.assignments)
print("Log-likelihood:", model.compute_likelihood())