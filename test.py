"""test.py describes the use of the custom logging module used with VisionSystem 2018."""

from Log import Log

Log("Log.py can log both textual information as well as images created with OpenCV and NumPy.", 1)
Log("The following is a demonstration of all 5 textual log levels (referred to in code as \"LogLevel\"s):", 1)
Log("This is debug information. Not much to see here, unless you are /really/ interested in the program internals, or are demonstrating some of the program\'s features.", 0)
Log("This is the standard information level. You can expect to see messages such as \"File Saved\" or \"Settings Loaded!\" here.", 1)
Log("This is the warning log level. \"Fulfilling server request would exceed stated bandwidth in configuration! Limiting data transfer rate to maximum of N KBps...\" is a message which might appear here.", 2)
Log("This is the log level where you know something has gone wrong. \"Unable to process request from server: Bad header?!\" is an example of a message appropriate for this type of LogLevel.", 3)
Log("This is the critical log level. Use this for only the most dire of errors - ones which will crash the program entirely, or brick the system. Examples include \"This location will be bombarded with a \'relativistic kill vehicle\' in ten seconds...\", and \"Configuration file missing!\".", 4)
Log("This is not a real log level. It's included for demonstration purposes.", 5)