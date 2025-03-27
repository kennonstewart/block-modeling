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

def test_base_sbm_mrs_calculation():
    adjacency_matrix = TEST_BASE_SBM_INITIALIZATION["adjacency_matrix"]
    number_of_blocks = TEST_BASE_SBM_INITIALIZATION["number_of_blocks"]

    # Initialize BaseSBM
    sbm = BaseSBM(adjacency_matrix, number_of_blocks)

    # initialize the test groups
    sbm.group_assignments = np.array([0, 1])

    # Calculate m_rs
    m_rs = sbm._calculate_mrs(0, 1) 

    # Assertions
    assert m_rs == 1

def test_base_sbm_fit():
    adjacency_matrix = TEST_BASE_SBM_INITIALIZATION["adjacency_matrix"]
    number_of_blocks = TEST_BASE_SBM_INITIALIZATION["number_of_blocks"]

    # Initialize BaseSBM
    sbm = BaseSBM(adjacency_matrix, number_of_blocks)

    # Fit
    with pytest.raises(NotImplementedError):
        sbm.fit()