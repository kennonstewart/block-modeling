# src/sbm/run_pipeline.py

import numpy as np
from sbm import SBM
from logging_config import setup_logging
from dc_sbm import DCSBM

logger = setup_logging(__name__)

# Generate a toy adjacency matrix (undirected, binary)
A_undirected_binary = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
])

logger.info("Running SBM on a toy dataset...")

# Generate a directed binary matrix
A_directed_binary = np.array([
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
])

# Generate a random adjacency matrix with 10 dimensions
# for a graph with up to 10 multiedges between nodes
np.random.seed(9271999)
A_random = np.random.randint(0, 11, (10, 10))

# Number of communities to fit
K = 4

# Choose model type
USE_DEGREE_CORRECTION = True

# Initialize and run model
if USE_DEGREE_CORRECTION:
    model = DCSBM(A_random, K)
    logger.info("Running Degree-Corrected SBM...")
else:
    model = SBM(A, K)
    logger.info("Running Standard SBM...")

model.fit()

# Show results
print("Group assignments:", model.group_assignments)
print("Log-likelihood:", model.compute_likelihood())
print("Results from fitting: ", model.fit())