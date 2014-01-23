Kaleidos Fabric Plugins (Tools)
===============================

Currently implemented:

+------------------------------------------------+-------------------------------------------+
| Class path                                     | Description                               |
+================================================+===========================================+
| ``kfabric.api.HgTool``                         | Mercurial Helpers                         |
+------------------------------------------------+-------------------------------------------+
| ``kfabric.decorators.ssh_tunnel``              | SSH Tunneling implemented as decorator.   |
+------------------------------------------------+-------------------------------------------+
| ``kfabric.context_managers.SSHTunnel``         | SSH Tunneling implemented as ctx manager. |
+------------------------------------------------+-------------------------------------------+

How to install?
---------------

Simple instalation instructions::

    git clone git://github.com/kaleidos/kfabric-tools.git
    cd kfabric-tools
    python setup.py install


Api Documentation
-----------------


SSH Tunneling
^^^^^^^^^^^^^

- ``kfabric.decorators.ssh_tunnel``
- ``kfabric.context_managers.SSHTunnel``

Posible parameters:

- «host» is a internal remote host
- «port» is a internal remote port (default: 22)
- «remote_host» is a first level remote host 
- «remote_port» is a first level remote port (default: 22)
- «local_host» is a local bind address (default: localhost)
- «local_port» is a local bind port (defaut: 2222)

Usage example of a decorator::

    from kfabric.decorartors import ssh_tunnel
    tunnel_kwargs = {
       'remote_host': 'remote_host_or_ip',
       'host': 'intern_remote_host_or_ip',
    }

    @ssh_tunnel(**tunnel_kwargs)
    def deploy(**kwargs):
        run('uname -a')


This decorator, internaly uses ``SSHTunnel`` context manager, and this is a simple example::
     
    from kfabric.context_managers import SSHTunnel
    tunnel_kwargs = {
       'remote_host': 'remote_host_or_ip',
       'host': 'intern_remote_host_or_ip',
    }   
    with SSHTunnel(**tunnel_kwargs) as tunnel:
       # do any think with open tunnel


Mercurial
^^^^^^^^^

``kfabric.api.HgTool``

Is a simple helper for mercurial. Currently only has one method:

- ``HgTool.push_local_changes(path, username)``: Push local mercurial changes to remote mercurial. You can use the configuration of the tunnel.

Example::

    from kfabric.context_managers import SSHTunnel
    tunnel_kwargs = {
        'remote_host': 'remote_host_or_ip',
        'host': 'intern_remote_host_or_ip',
    }   
    with SSHTunnel(**tunnel_kwargs) as tunnel:
        HgTool().with_tunnel(tunnel).push_local_changes(path="/path", username="foouser")

