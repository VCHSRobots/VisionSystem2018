"""Log.py performs logging functions.

Log.py takes logging information and places it into the "Logging" directory as a file.
It can support logging both strings and images (in the format of a numpy.ndarray).
"""

import sys
import time
from uuid import uuid4
import cv2
import numpy as np

def Log(Message = None, LogLevel = 0):
    if Message == None:
        raise ValueError("Message has no value.")
        return
    Time = time.strftime("%Y-%m-%d %H:%M:%S")
    if type(Message) is str:
        LogLevel = str(LogLevel).upper()
        if LogLevel in ("0", "INFO"):
            Message = "INFO: " + Message
        elif LogLevel in ("1", "DEBUG"): # TODO: Only log messages marked as "DEBUG" if DebugMode == True in Settings.Settings!
            Message = "DEBUG: " + Message
        elif LogLevel in ("2", "WARNING"):
            Message = "WARNING: " + Message
        elif LogLevel in ("3", "ERROR"):
            Message = "ERROR: " + Message
        elif LogLevel in ("4", "CRITICAL"):
            Message = "CRITICAL: " + Message
        Message = Time + " " + Message + "\r\n"
        print(str(Message))
    elif type(Message) is np.ndarray: # If the message is an image.
        ImageName = Time + " " + str(uuid4()) + ".png"
        cv2.imWrite(ImageName, Message)

if __name__ == "__main__":
    sys.exit("This file may not be run as a standalone.")
else:
    pass