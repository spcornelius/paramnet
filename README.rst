paramnet
========

``paramgraph`` provides a convenience mixin, `Parametrized`, for creating subclasses of
NetworkX's `Graph` (`DiGraph`) that have expected parameters associated with each
node and/or edge (e.g., in a network dynamical system). It enforces the existence
of specified named attributes for the (Di)Graph's nodes/edges, and also maintains
a well-defined order for the nodes. This allows the user to extract a given node (edge)
parameters as a well-defined vector (matrix).

Examples
--------
A parametrized network class can be created by subclassing from `Graph` or `DiGraph`
using the `Parametrized` mixin and specifying the names of the node/edge parameters
in the class definition:

.. code:: python

    class MyGraph(Parametrized, Graph):
        _node_params = ['x']
        _edge_params = ['weight']

    G = MyGraph()
..

As with all mixins, `Parametrized` should be inherited from *first* as above.
Any instance of this class will require all corresponding attributes to be defined for each new
node or edge, meaning the following will raise exceptions:

.. code:: python

    G.add_node(0)

    G.add_edge(0, 1)

..

Because `Parametrize` maintains the order of nodes, one can get a numpy `ndarray` corresponding
to the value of a given parameter for all nodes (edges)

.. code:: python

    G.add_node("a", x=1)
    G.add_node("b", x=2)

    G.add_edge("a", "b", weight=10)

    # returns [1, 2]
    G.node_param_vector('x')

    # returns [[0, 10],
    #          [10, 0]]
    G.edge_param_matrix('weight')

..

For convenience, the weighted adjacency matrix can also be accessed through the property `.A`

.. code:: python

    # equivalent to G.edge_param_matrix('weight')
    G.A

..

Dependencies
------------
* NetworkX (>= 2.0)
* indexed.py
* scipy

License
-------

``paramnet`` is released under the MIT license. See LICENSE for details.