"""Settings.py manages settings.

Settings.py can provide the values of requested keys. It can also edit the values of keys.
Settings information is stored in VS.cfg in JSON.
"""

import json
import sys

Config = []

# Load initial settings from configuration file. The default file is "VS.cfg", but this can be changed.
def Read(FileName = "VS.cfg"):
    try:
        with open(Filename, "r") as File:
            global Config
            Config = json.load(File)
    except FileNotFoundError:
        Log("Unable to load configuration file \"" + FileName + "\": File does not exist.", 4)
    except PermissionError:
        Log("Unable to read configuration file \"" + FileName + "\": Insufficient permissions.", 4)
    except ValueError:
        Log("Unable to parse configuration file \"" + FileName + "\": Bad JSON.", 4)

# Write settings into settings object.
def Write(Foo):
    pass

# Write settings to configuration file.
def WriteToFile(Foo):
    try:
        with open("VS.cfg", "w") as File:
            pass
    except:
        pass

# Write default settings value to file.
def WriteDefaultsToFile():
    try:
        with open("VS.cfg", "w") as File:
            File.write()
    except PermissionError:
        Log("Unable to write default settings to configuration file \"VS.cfg\": Insufficient permissions.", 3)

Read()