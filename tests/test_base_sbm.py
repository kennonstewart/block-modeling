import numpy as np
import pytest
from sbm.base_sbm import BaseSBM
from test_data import *

def test_base_sbm_initialization():
    adjacency_matrix = TEST_BASE_SBM_INITIALIZATION["adjacency_matrix"]
    number_of_blocks = TEST_BASE_SBM_INITIALIZATION["number_of_blocks"]

    # Initialize BaseSBM
    sbm = BaseSBM(adjacency_matrix, number_of_blocks)

    # Assertions
    assert sbm.adjacency_matrix.shape == (2, 2)
    assert sbm.number_of_blocks == 2
    assert sbm.n == 2
    assert len(sbm.group_assignments) == 2

def test_base_sbm_fit():
    adjacency_matrix = TEST_BASE_SBM_INITIALIZATION["adjacency_matrix"]
    number_of_blocks = TEST_BASE_SBM_INITIALIZATION["number_of_blocks"]

    # Initialize BaseSBM
    sbm = BaseSBM(adjacency_matrix, number_of_blocks)

    # Fit
    with pytest.raises(NotImplementedError):
        sbm.fit()