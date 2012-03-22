# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

class HgTool(object):
    def __init__(self, local_host="localhost", local_port="2222"):
        self.local_host = local_host
        self.local_port = local_port

    def with_tunel(self, tunel):
        self.tunel = tunel
        self.local_host = tunel.local_host
        self.local_port = tunel.local_port
        return self

    def push_local_changes(self, path, username="kaleidos"):
        push_command = "hg push --new-branch ssh://{0}@{1}:{2}{3}"\
            .format(username, self.local_host, self.local_port, path)

        p = Popen(push_command.split(), stdout=PIPE)
        result = p.communicate()
        if result and result[0]:
            print result[0]
