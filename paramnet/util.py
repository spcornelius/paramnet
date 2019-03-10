import networkx as nx
import numpy as np

__all__ = []

__all__.extend([
    'node_param_vector',
    'edge_param_matrix'
])


def node_param_vector(G, param_name, nodes=None):
    if nodes is None:
        nodes = G.nodes()

    def get_param(node):
        return G.nodes[node][param_name]

    return np.array([get_param(node) for node in nodes])


def edge_param_matrix(G, param_name, nodes=None, transpose=False):
    if nodes is None:
        nodes = G.nodes()

    P = nx.attr_matrix(G, edge_attr=param_name, rc_order=nodes).A
    return P.T if transpose else P
