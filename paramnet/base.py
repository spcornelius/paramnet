import networkx as nx
from indexed import IndexedOrderedDict

from paramnet.dict import node_attr_dict_factory, edge_attr_dict_factory
from paramnet.exceptions import ParametrizedNetworkError
from paramnet.util import node_param_vector, edge_param_matrix

__all__ = []
__all__.extend([
    'Parametrized'
])

_add_methods = ['add_node', 'add_nodes_from', 'add_edge', 'add_edges_from',
                'add_weighted_edges_from']


def verify_add(method):
    """ wrapper to check all node/edge additions have required parameters and
    rollback if not

    Checking is done by casting the attr dicts for any new nodes/edges as
    the appropriate AttrDict subclass in this module, which enforces required
    keys. Cleanest general solution, since (i) nx.add_node/edge* methods accept
    different input types and (ii) they don't consistently use
    node(edge)_attr_dict_factory to create new attr dicts. """

    def wrapped(self, *args, **kwargs):
        old_nodes = set(self.nodes())
        old_edges = set(self.edges())

        method(self, *args, **kwargs)

        new_nodes = self.nodes() - old_nodes
        new_edges = self.edges() - old_edges
        try:
            for new_node in new_nodes:
                if not isinstance(self._node[new_node], self._nadf):
                    self._node[new_node] = self._nadf(self._node[new_node])
            for new_edge in new_edges:
                u, v = new_edge
                if not isinstance(self._adj[u][v], self._eadf):
                    self._adj[u][v] = self._eadf(self._adj[u][v])
        except ParametrizedNetworkError as err:
            # rollback
            self.remove_nodes_from(new_nodes)
            self.remove_edges_from(new_edges)
            raise err

    return wrapped


class ParametrizedMeta(type):
    """ Metaclass for Parametrized graphs. """

    def __new__(mcs, name, bases, attrs):
        cls = type.__new__(mcs, name, bases, attrs)

        # maintain order of nodes and allow indexing
        cls.node_dict_factory = IndexedOrderedDict

        # enforce presence of attributes after creation
        cls._nadf = node_attr_dict_factory(getattr(cls, "_node_params", []))
        cls._eadf = edge_attr_dict_factory(getattr(cls, "_edge_params", []))

        for method in _add_methods:
            if hasattr(cls, method):
                # wrap all add_ methods with attribute checks
                setattr(cls, method, verify_add(getattr(cls, method)))
        return cls

    def __call__(mcs, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        if not isinstance(obj, nx.Graph):
            raise TypeError(
                "Parametrize mixin must be used with a subclass of nx.Graph.")
        return obj


class Parametrized(object, metaclass=ParametrizedMeta):
    _node_params = []
    _edge_params = []

    def index(self, node):
        try:
            return self._node.keys().index(node)
        except ValueError:
            raise nx.NetworkXError(f"The node {node} is not in the graph.")

    @property
    def A(self):
        return nx.adjacency_matrix(self).todense()

    @property
    def node_params(self):
        return self._node_params

    @property
    def edge_params(self):
        return self._edge_params

    def node_param_vector(self, name):
        return node_param_vector(self, name)

    def edge_param_matrix(self, name, transpose=False):
        return edge_param_matrix(self, name, transpose=transpose)
