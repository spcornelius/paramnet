__all__ = []

__all__.extend([
    'ParametrizedNetworkError',
    'NodeParameterError',
    'EdgeParameterError'
])


class ParametrizedNetworkError(Exception):
    pass


class NodeParameterError(ParametrizedNetworkError):
    pass


class EdgeParameterError(ParametrizedNetworkError):
    pass
