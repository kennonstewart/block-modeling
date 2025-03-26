import numpy as np
from sbm.base_sbm import BaseSBM
from sbm.logging_config import setup_logging

logger = setup_logging(__name__)

class SBM(BaseSBM):
    """
    Stochastic Block Model
    """

    def __init__(self, *args, **kwargs):
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)

    def compute_likelihood(self):
        # compute the unnormalized likelihood of empirical group assignments
        print(self.group_assignments)
        output = 2
        return output

    def fit(self):
        # raise not implemented error
        raise NotImplementedError