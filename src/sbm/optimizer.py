from logging_config import setup_logging


logger = setup_logging(__name__)

def optimize_model(adjacency_matrix, group_assignments):
    """
    Given an adjacency matrix, fit a Stochastic Block Model such that
    the likelihood of the observed group assignments is maximized.
    """
    likelihood = 0
    groups = np.unique(group_assignments)
    for r in groups:
        for s in groups:
            if r == s:
                continue
            m_rs = calculate_mrs(adjacency_matrix, group_assignments, r, s)
            likelihood += compute_likelihood_contribution(adjacency_matrix, group_assignments, r, s, m_rs)
    return likelihood
