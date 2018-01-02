"""Log.py performs logging functions.

Log.py takes logging information and places it into the "Logging" directory as a file.
It can support logging both strings and images (in the format of a numpy.ndarray).
"""

import sys
import time
from uuid import uuid4

import cv2
import numpy as np

def Log(Message = None, LogLevel = 1):
    if Message == None:
        raise ValueError("Message has no value.")
        return
    Time = time.strftime("%Y-%m-%d %H:%M:%S")
    if type(Message) == str:
        LogLevel = str(LogLevel).lower()
        if LogLevel in ("0", "debug"):
            Message = "DEBUG:    " + Message
        elif LogLevel in ("1", "info"):
            Message = "INFO:     " + Message
        elif LogLevel in ("2", "warning"):
            Message = "WARNING:  " + Message
        elif LogLevel in ("3", "error"):
            Message = "ERROR:    " + Message
        elif LogLevel in ("4", "critical"):
            Message = "CRITICAL: " + Message
        else:
            raise ValueError("Improper value passed for log level.")
        Message = "{0} > {1}".format(Time, Message)
        print(str(Message))
    elif type(Message) is np.ndarray: # If the message is an image.
        ImageName = "{0} {1}.png".format(Time, uuid4())
        cv2.imWrite(ImageName, Message)

if __name__ == "__main__":
    sys.exit("This file may not be run as a standalone.")