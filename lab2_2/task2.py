#!/usr/bin/env python
import os
import sys

import angr

def analysis(goose):
    """Args:
    goose: filepath to goose binary
    """

    # TODO: Place your code here!

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <goose_publisher_example>" % os.path.basename(sys.argv[0]))
        sys.exit(1)

    analysis(sys.argv[1])

if __name__ == '__main__':
    main()
