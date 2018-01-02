#!/usr/bin/env python

import sys

CommandLineArguments = [X.lower() for X in sys.argv[1:]]
if CommandLineArguments[0] in ("-h", "-?", "--help"):
    print("VisionSystem Help: ")
elif CommandLineArguments[0] in ("-s", "--source"):
    pass