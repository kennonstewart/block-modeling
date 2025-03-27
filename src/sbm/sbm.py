import numpy as np
from base_sbm import BaseSBM
from optimizer import calculate_mrs
from logging_config import setup_logging

logger = setup_logging(__name__)

class SBM(BaseSBM):
    """
    Stochastic Block Model
    """

    def __init__(self, *args, **kwargs):
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)

    def __calculate_mrs(self, r, s):
        """
        Calculate the number of edges between groups r and s
        """
        m_rs = 0
        for i in range(len(self.group_assignments)):
            for j in range(len(self.group_assignments)):
                if self.group_assignments[i] == r and self.group_assignments[j] == s and i != j:
                    m_rs += self.adjacency_matrix[i, j]
        return m_rs
    
    def __compute_likehood_contribution(self, r, s, m_rs):
        """
        Compute the contribution of group r and s to the likelihood
        """
        output = m_rs * np.log(m_rs / (sum(self.group_assignments==r) * sum(self.group_assignments==s)))
        return output


    def compute_likelihood(self):
        # compute the unnormalized likelihood of empirical group assignments
        output = 0

        # calculate m_{r, s}: the number of edges between groups r and s
        groups = np.unique(self.group_assignments)
        for r in groups:
            for s in groups:
                if r == s:
                    continue
                m_rs = self.__calculate_mrs(r, s)
                output += self.__compute_likehood_contribution(r, s, m_rs)
        return output

    def fit(self):
        # raise not implemented error
        return 10