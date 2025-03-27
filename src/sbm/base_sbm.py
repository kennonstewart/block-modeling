import numpy as np

logger = setup_logging(__name__)

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

    def _calculate_mrs(self, r, s):
        """
        Calculate the number of edges between groups r and s
        """
        m_rs = 0
        for i in range(len(self.group_assignments)):
            for j in range(len(self.group_assignments)):
                if self.group_assignments[i] == r and self.group_assignments[j] == s and i != j:
                    m_rs += self.adjacency_matrix[i, j]
        return m_rs

    def fit(self):
        raise NotImplementedError
