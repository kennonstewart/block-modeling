
def calculate_mrs(r, s, adjacency_matrix, group_assignments):
    """
    Calculate the number of edges between groups r and s
    """
    m_rs = 0
    for i in range(len(group_assignments)):
        for j in range(len(group_assignments)):
            if group_assignments[i] == r and group_assignments[j] == s and i != j:
                m_rs += adjacency_matrix[i, j]
    return m_rs
