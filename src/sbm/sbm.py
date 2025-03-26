import numpy as np
from sbm_base import SBMBase

class SBM(SBMBase):
    """
    Stochastic Block Model
    """

    def __init__(self, *args, **kwargs):
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)

    def compute_likelihood(self):
        # compute the unnormalized likelihood of empirical group assignments
        output = self.n
        return output

    def fit(self):
        # Placeholder for optimization routine
        pass