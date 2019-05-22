#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path, sys


def import_full_path(name, path):
    if sys.version_info >= (3, 5):
        from importlib import util
        spec = util.spec_from_file_location(name, path)
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    else:
        import importlib.machinery
        return importlib.machinery.SourceFileLoader(name, path).load_module()


if __name__ != '__main__':
    raise SystemError('do not import this script')

path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                    'rbpd-python', 'rbpd.py')
import_full_path('rbpd-python.rbpd', path).main()

