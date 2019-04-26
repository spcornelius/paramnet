v2.3.0
======
- Inheritance of node/graph/edge parameters
- Minor bugfix

v2.2.0
======
- Allow access to all numpy attrs of parameter arrays

v2.1.0
======
- Support for graph-wide params

v2.0.0
======
- Simplified interface
- Missing params return NaN instead of raising errors
- Improved documentation

v1.3.0
======
- Reinstate use of ParametrizedMeta metaclass
- Support for fancy indexing and array-wise assignment of param values

v1.2.0
======
- Minor interface change for subclassing Parametrized

v1.1.1
======
- Allow subclassing of Parametrized without Graph

v1.1.0
======
- Simplify interface by removing MetaClass
- Allow defining node/edge params in class arguments

v1.0.2
======
- Fix example code error in README
- Add scipy to testing requirements

v1.0.1
======
- Minor code cleanup

v1.0.0
======
- View interface to node/edge params
- Named param fields support O(1) random access for specific values (keyed by node/edge)
- Named param fields also support array (numpy) operations (non-indexed access)
- Improved documentation

v0.4.0
======
- Overhaul enforcement of require attrs through custom dicts/descriptors
- Make said dicts/descriptors exported and available to inherit

v0.3.2
======
- ParametrizedMeta inheritance tweak

v0.3.1
======
- ParametrizedMeta shift from __new__ to __init__

v0.3.0
======
- Use more efficient/standard OrderedDict to maintain node order

v0.2.0
======
- Support for getting node/edge param arrays via named fields (properties)

v0.1.1
======
- Package housekeeping/documentation

v0.1.0
======
- Initial release