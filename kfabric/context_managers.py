# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import time
import signal
from subprocess import Popen


class SSHTunnel(object):
    """Context manager for creating an ssh tunnel.

    Posible parameters:
     * «host» is a internal remote host
     * «port» is a internal remote port (default: 22)
     * «remote_host» is a first level remote host (first destination)
     * «remote_port» is a first level remote port (first destination, default: 22)
     * «local_host» is a local bind address (default: localhost)
     * «local_port» is a local bind port (defaut: 2222)

     The final command is:
        ssh -L local_host:local_port:host:port -N remote_host -p remote_port

     The remote host can contain credentials. Example: user@kaleidos.net

     """

    def __init__(self, host, remote_host, local_port="2222", remote_port="22",
                 local_host="localhost", port="22"):
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.local_host = local_host
        self.local_port = local_port
        self.host = host
        self.port = port

    def __enter__(self):
        print("Starting tunnel...")

        tunnel_command = "ssh -L {0}:{1}:{2}:{3} -N {4} -p {5}".format(
            self.local_host,
            self.local_port,
            self.host,
            self.port,
            self.remote_host,
            self.remote_port,
        )

        self.p = Popen(tunnel_command.split())
        self.pid = self.p.pid
        time.sleep(2)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Stoping tunnel...")
        os.kill(self.pid, signal.SIGQUIT)
