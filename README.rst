Kaleidos Fabric Plugins (Tools)
===============================

Currently implemented:

Class path                                     | Description
---------------------------------------------- | -----------
``kfabric.api.HgTool``                         | Mercurial Helpers
``kfabric.decorators.ssh_tunel``               | Operate in a ssh tunel.
``kfabric.context_managers.SSHTunel``          | Low level decorator for ssh tuneling.


How to install?
---------------

Simple instalation instructions::

    git clone git://github.com/kaleidos/kfabric-tools.git
    cd kfabric-tools
    python setup.py install


Api Documentation
-----------------


SSH Tuneling
^^^^^^^^^^^^

- ``kfabric.decorators.ssh_tunel``
- ``kfabric.context_managers.SSHTunel``

Posible parameters:

- «host» is a internal remote host
- «port» is a internal remote port (default: 22)
- «remote_host» is a first level remote host 
- «remote_port» is a first level remote port (default: 22)
- «local_host» is a local bind address (default: localhost)
- «local_port» is a local bind port (defaut: 2222)

Usage example of a decorator::

    from kfabric.decorartors import ssh_tunel
    tunel_kwargs = {
       'remote_host': 'remote_host_or_ip',
       'host': 'intern_remote_host_or_ip',
    }

    @ssh_tunel(**tunel_kwargs)
    def deploy(**kwargs):
        run('uname -a')


This decorator, internaly uses ``SSHTunel`` context manager, and this is a simple example::
     
    from kfabric.context_managers import SSHTunel
    tunel_kwargs = {
       'remote_host': 'remote_host_or_ip',
       'host': 'intern_remote_host_or_ip',
    }   
    with SSHTunel(**tunel_kwargs) as tunel:
       # do any think with open tunel


Mercurial
^^^^^^^^^

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

