import numpy as np
from logging_config import setup_logging

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

    def _compute_likelihood_contribution(self, r, s, m_rs):
        """
        Placeholder for likelihood contribution calculation.
        Should be implemented by child classes.
        """
        raise NotImplementedError("This method should be implemented by child classes.")

    def compute_likelihood(self):
        """
        Compute the unnormalized likelihood of empirical group assignments.
        """
        output = 0
        groups = np.unique(self.group_assignments)
        for r in groups:
            for s in groups:
                if r == s:
                    continue
                m_rs = self._calculate_mrs(r, s)
                output += self._compute_likelihood_contribution(r, s, m_rs)
        return output
    
    def _calculate_mrs(self, r, s):
        m_rs = 0
        for i in range(len(self.group_assignments)):
            for j in range(len(self.group_assignments)):
                if self.group_assignments[i] == r and self.group_assignments[j] == s and i != j:
                    m_rs += self.adjacency_matrix[i, j]
        return m_rs

    def _fit(self, max_iter=100):
        iteration_log_likelihood = self.compute_likelihood()
        # for each node in the graph
        for node in range(self.n):
            # for each of the remaining groups
            for alternative in (set(self.group_assignments)):
                if alternative == self.group_assignments[node]:
                    continue
                # move the node to the alternative group
                self.group_assignments[node] = alternative                    

                # recalculate the log-likelihood
                new_log_likelihood = self.compute_likelihood()
                
                # if we see an improvement in likelihood
                if new_log_likelihood > iteration_log_likelihood:
                    iteration_log_likelihood = new_log_likelihood
                else:
                    # revert the move
                    self.group_assignments[node] = alternative
            logger.info(f"Fitting model on iteration: {node}")
            logger.info(f"Model fit complete with likelihood: {iteration_log_likelihood}")
        return (iteration_log_likelihood, self.group_assignments) # return the log-likelihood and group assignments

