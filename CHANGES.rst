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