import numpy as np
from base_sbm import BaseSBM
from logging_config import setup_logging

logger = setup_logging(__name__)

class DCSBM(BaseSBM):
    """
    Degree-Corrected Stochastic Block Model
    """

    def __init__(self, *args, **kwargs):
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)

    def __compute_likehood_contribution(self, r, s, m_rs):
        """
        Compute the contribution of group r and s to the likelihood
        """
        k_r = self.__calculate_group_degree(r)
        k_s = self.__calculate_group_degree(s)
        output = m_rs * np.log(m_rs / (k_r * k_s))
        return output
    
    def __calculate_group_degree(self, group):
        """
        Calculate the total degree (k_group) for a given group.
        """
        group_nodes = np.where(self.group_assignments == group)[0]
        total_degree = 0
        for node in group_nodes:
            total_degree += np.sum(self.adjacency_matrix[node])
        return total_degree

    def compute_likelihood(self):
        # compute the unnormalized likelihood of empirical group assignments
        output = 0

        # calculate m_{r, s}: the number of edges between groups r and s
        groups = np.unique(self.group_assignments)
        for r in groups:
            for s in groups:
                if r == s:
                    continue
                m_rs = self._calculate_mrs(r, s) # number of edges between r and s
                output += self.__compute_likehood_contribution(r, s, m_rs)
        return output

    def fit(self):
        # Placeholder for optimization routine
        output = self._fit()
        return output