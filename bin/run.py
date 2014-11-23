# -*- coding: utf-8 -*-
import os, sys

possible_topdir = os.path.normpath(os.path.join(os.path.abspath(
        sys.argv[0]), os.pardir, os.pardir))
if os.path.exists(os.path.join(possible_topdir, "lightning", "__init__.py")):
    sys.path.insert(0, possible_topdir)

if __name__ == '__main__':
    pass