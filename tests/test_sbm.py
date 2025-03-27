from sbm.sbm import SBM
from test_data import *
import pytest


def test_sbm_initialization():
    adjacency_matrix = TEST_SBM_INITIALIZATION["adjacency_matrix"]
    number_of_blocks = TEST_SBM_INITIALIZATION["number_of_blocks"]

    # Initialize BaseSBM
    sbm = SBM(adjacency_matrix, number_of_blocks)

    # Assertions
    assert sbm.adjacency_matrix.shape == (2, 2)
    assert sbm.number_of_blocks == 2
    assert sbm.n == 2
    assert len(sbm.group_assignments) == 2

def test_sbm_likelihood():
    adjacency_matrix = TEST_SBM_INITIALIZATION["adjacency_matrix"]
    number_of_blocks = TEST_SBM_INITIALIZATION["number_of_blocks"]

    # Initialize SBM
    sbm = SBM(adjacency_matrix, number_of_blocks)

    # Compute likelihood
    likelihood = sbm.compute_likelihood()
    
    # Assertions
    assert likelihood == 2

def test_sbm_fit():
    adjacency_matrix = TEST_SBM_INITIALIZATION["adjacency_matrix"]
    number_of_blocks = TEST_SBM_INITIALIZATION["number_of_blocks"]

    # Initialize SBM
    sbm = SBM(
        adjacency_matrix,
        number_of_blocks
    )

    # assert that the fit method is not implemented
    with pytest.raises(NotImplementedError):
        sbm.fit()