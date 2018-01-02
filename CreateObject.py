"""CreateObject.py allows the user to easily create an object for VisionSystem.

CreateObject.py allows the user to easily create an object for use with the VisionSystem, by using command-line and GUI elements.
The created file will have an ".obj" extension, and its contents will be formatted in JSON.
"""

import json
import sys
import time

import cv2
import numpy as np

PixelColor = []
Points = []