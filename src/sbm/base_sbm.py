import numpy as np

class BaseSBM:
    """
    Base class for Stochastic Block Model
    """

    def __init__(self, adjacency_matrix: np.ndarray, number_of_blocks):
        self.adjacency_matrix = adjacency_matrix  # Adjacency matrix
        self.number_of_blocks = number_of_blocks  # Number of blocks
        self.n = adjacency_matrix.shape[0]
        self.group_assignments = np.random.randint(number_of_blocks, size=self.n)

    def compute_likelihood(self):
        raise NotImplementedError

    def fit(self):
        raise NotImplementedError
