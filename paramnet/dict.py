from paramnet.exceptions import ParametrizedNetworkError, NodeParameterError, \
    EdgeParameterError

__all__ = []
__all__.extend([
    'node_attr_dict_factory',
    'edge_attr_dict_factory'
])


class AttrDict(dict):
    """ dict that prevents specified keys from being removed once added """

    _exception = ParametrizedNetworkError
    _node_edge = ""
    _required_attrs = set()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not set(self.required_attrs) <= set(self):
            raise self._exception(
                f"Can't create {self._node_edge} without all required "
                f"attributes: {self.required_attrs}.")

    @property
    def required_attrs(self):
        return self._required_attrs

    def __delitem__(self, k):
        if k in self._equired_attrs:
            raise self._exception(
                f"Can't delete required {self._node_edge} attribute '{k}'.")
        super().__delitem__(k)

    def clear(self):
        if self.required_attrs:
            raise self._exception(
                f"Can't clear the following required {self._node_edge} "
                f"attributes: {self.required_attrs}")
        super().clear()

    def pop(self, k, default=None):
        if k in self.required_attrs:
            if default is None:
                raise self._exception(
                    f"Can't pop required {self._node_edge} attribute '{k}'.")
            return default
        return super().pop(k, default)

    def popitem(self):
        k, v = super().popitem()
        if k in self.required_attrs:
            self[k] = v
            raise self._exception(
                f"Cannot pop required {self._node_edge} attribute '{k}' for "
                f"{self._el}")


def node_attr_dict_factory(node_params):
    class NodeAttrDict(AttrDict):
        _required_attrs = set(node_params)
        _exception = NodeParameterError
        _node_edge = "node"

    return NodeAttrDict


def edge_attr_dict_factory(edge_params):
    class EdgeAttrDict(AttrDict):
        _required_attrs = set(edge_params)
        _exception = EdgeParameterError
        _node_edge = "edge"

    return EdgeAttrDict
