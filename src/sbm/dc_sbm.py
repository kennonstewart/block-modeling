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
        # Placeholder for optimization routine
        pass