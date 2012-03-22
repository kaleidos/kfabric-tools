# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import time

class SSHTunel(object):
    """
    Context manager for create ssh tunel.
    Posible parameters:
     * «host» is a internal remote host
     * «port» is a internal remote port (default: 22)
     * «remote_host» is a first level remote host 
     * «remote_port» is a first level remote port (default: 22)
     * «local_host» is a local bind address (default: localhost)
     * «local_port» is a local bind port (defaut: 2222)
     """

    def __init__(self, host, remote_host, local_port="2222", 
                remote_port="22", local_host="localhost", port="22"):
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.local_host = local_host
        self.local_port = local_port
        self.host = host
        self.port = port

    def __enter__(self):
        print "Starting tunnel..."
        from subprocess import Popen
        tunel_command = "ssh -L {0}:{1}:{2}:{3} -N {4} -p {5}".format(
            self.local_host,
            self.local_port,
            self.host,
            self.port,
            self.remote_host,
            self.remote_port,
        )

        self.p = Popen(tunel_command.split())
        self.pid = self.p.pid
        time.sleep(2)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print "Stoping tunel..."
        import os, signal
        os.kill(self.pid, signal.SIGQUIT)
