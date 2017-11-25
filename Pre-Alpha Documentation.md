#EPIC Robotz Vision System 2018
##Goals and information:

First task: Update the old system so that it "just works" for detection of targets in the 2018 FRC game.
Second task: Create a new and improved vision system from the ground-up.

*The most important questions: What would the new system entail? And what should we do to create it?*

###GENERAL GOALS:
  - Program using flexible modules.
  - Incorporate a lightweight and comprehensive logging system.
    - Detail how the program came to it's conclusions about target location, along with a copy of a (potentially) labeled image.
  - Incorporate a debugging system.
   - For use when setting up the program or demonstrating its features.
  - Create and maintain proper documentation alongside developing the program.
    - (See https://www.python.org/dev/peps/pep-0008/#documentation-strings and https://www.stack.nl/~dimitri/doxygen/index.html)

###OBJECT RECOGNITION GOALS:
  - We want to recognize any number of arbitrarily-shaped planar polygons in any three-dimensional pose... Whew!
  - That means the program should be able to tell the user:
    - How far away are the objects from the camera?
    - How are they rotated in three-dimensional space?
  - How would users create objects?
    - They would take a picture of the object in a neutral pose (at 0° rotation in all 3 planes), and open it up using a GUI program. (Likely programed in Python and OpenCV + Numpy)
    - The user would then click around the object to draw lines around it; marking the polygon's vertices.
    - The user would then input the distance of the object from the camera when the image was taken.
    - The program would then output an ".obj" file, which the user would then move into the Vision System's "Objects" folder.

###PROGRAM OUTLINE:

  - VisionSystem.py will be the main part of the program. It will handle calls to ObjectDetector.py, Log.py, and HUD.py. It will do this based on input it receives from either the user or Server.py.

  - Server.py will be written to be able to communicate with other devices (in our case mostly the RoboRIO) using a custom message syntax. It will listen for commands about what to do, and what information it should send back. It will also control debug / demonstration / configuration features.

  - Log.py will take care of all logging needs: text logs, and image backups alike.

  - HUD.py will do everything with regards to drawing information onto an image matrix.

  - ObjectDetector will find all specified objects in a given image frame.

##Final notes:
Information listed in this document will **almost certainly** be deprecated by future documentation.
Be aware that anything stated here may be inaccurate, or just plain wrong!