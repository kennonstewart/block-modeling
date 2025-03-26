import numpy as np

class BaseSBM:
    """
    Base class for Stochastic Block Model
    """

    def __init__(self, adjacency_matrix: np.ndarray, number_of_blocks, degree_correction = False):
        self.adjacency_matrix = adjacency_matrix  # adjacency matrix
        self.number_of_blocks = number_of_blocks  # number of classes
        self.n = adjacency_matrix.shape[0]
        self.group_assignments = np.random.randint(number_of_blocks, size=self.n)
        self.degree_correction = degree_correction

    def fit(self):
        raise NotImplementedError
