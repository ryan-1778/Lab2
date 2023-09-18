#!/usr/bin/env python
import os
import sys

import angr

def solve(fauxware):
    """Args:
    fauxware: filepath to fauxware binary
    """

    # TODO: Place your code here!

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <fauxware>" % os.path.basename(sys.argv[0]))
        sys.exit(1)

    solve(sys.argv[1])

if __name__ == '__main__':
    main()
