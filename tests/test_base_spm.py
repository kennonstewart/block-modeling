import numpy as np
import pytest
from sbm.base_sbm import BaseSBM

def test_base_sbm_initialization():
    adjacency_matrix = np.array([[0, 1], [1, 0]])
    number_of_blocks = 2

    # Initialize BaseSBM
    sbm = BaseSBM(adjacency_matrix, number_of_blocks)

    # Assertions
    assert sbm.adjacency_matrix.shape == (2, 2)
    assert sbm.number_of_blocks == 2
    assert sbm.n == 2
    assert len(sbm.group_assignments) == 2