Kaleidos Fabric Plugins (Tools)
===============================

Currently implemented:

Class path                                     | Description
---------------------------------------------- | -----------
``kfabric.context_managers.SSHTunel``          | Create ssh tunel.
``kfabric.api.HgTool``                         | Mercurial Helpers

How to install?
---------------

Simple instalation instructions::

    git clone git://github.com/kaleidos/kfabric-tools.git
    cd kfabric-tools
    python setup.py install


Api Documentation
-----------------

``kfabric.context_managers.SSHTunel``

Posible parameters:

- «host» is a internal remote host
- «port» is a internal remote port (default: 22)
- «remote_host» is a first level remote host 
- «remote_port» is a first level remote port (default: 22)
- «local_host» is a local bind address (default: localhost)
- «local_port» is a local bind port (defaut: 2222)

Example::
     
    from kfabric.context_managers import SSHTunel
    tunel_kwargs = {
       'remote_host': 'remote_host_or_ip',
       'host': 'intern_remote_host_or_ip',
    }   
    with SSHTunel(**tunel_kwargs) as tunel:
       # do any think with open tunel


``kfabric.api.HgTool``

Is a simple helper for mercurial. Currently only has one method:

- ``HgTool.push_local_changes(path, username)``: Push local mercurial changes to remote mercurial. You can use the configuration of the tunnel.

Example::

    from kfabric.context_managers import SSHTunel
    tunel_kwargs = {
        'remote_host': 'remote_host_or_ip',
        'host': 'intern_remote_host_or_ip',
    }   
    with SSHTunel(**tunel_kwargs) as tunel:
        HgTool().with_tunel(tunel).push_local_changes(path="/path", username="foouser")

