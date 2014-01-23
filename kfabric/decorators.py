# -*- coding: utf-8 -*-

import functools

from .context_managers import SSHTunnel


def ssh_tunnel(**options):
    def _decorator(function):
        @functools.wraps(function)
        def _wrapper(*args, **kwargs):
            with SSHTunnel(**options) as tunel:
                kwargs['tunel'] = tunel
                return function(*args, **kwargs)
        return _wrapper
    return _decorator
