class BaseSBM:
    def __init__(self, adjacency_matrix, number_of_blocks):
        self.adjacency_matrix = adjacency_matrix  # Adjacency matrix
        self.number_of_blocks = number_of_blocks  # Number of blocks
        self.n = A.shape[0]
        self.group_assignments = np.random.randint(K, size=self.n)

    def compute_likelihood(self):
        raise NotImplementedError

    def fit(self):
        raise NotImplementedError
