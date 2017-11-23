# EPIC Robotz Vision System 2018
Goals and information:

First task: Update the old system so that it "just works" for detection of targets in the 2018 FRC game.
Second task: Create a new and improved vision system from the ground-up.

What would the new system entail? And what should we do to create it?

GENERAL GOALS:
 - Program using flexible modules.
 - Incorporate a lightweight and comprehensive logging system.
    - Detail how the program came to it's conclusions about target location, along with a copy of a (potentially) labeled image.
 - Incorporate a debugging system.
    - For use when setting up the program or demonstrating its features.
 - Create and maintain proper documentation alongside developing the program.
    - (See https://www.python.org/dev/peps/pep-0008/#documentation-strings and https://www.stack.nl/~dimitri/doxygen/index.html)

OBJECT RECOGNITION GOALS:
 - We want to recognize any number of arbitrarily-shaped planar polygons in any three-dimensional pose... Whew!
 - That means the program should be able to tell the user:
    - How far away are the objects from the camera?
    - How are they rotated in three-dimensional space?
 - How would users create objects?
    - They would take a picture of the object in a neutral pose (at 0° rotation in all 3 planes), and open it up using a GUI program. (Likely programed in Python and OpenCV + Numpy)
    - The user would then click around the object to draw lines around it; marking the polygon's vertices.
    - The user would then input the distance of the object from the camera when the image was taken.
    - The program would then output an ".obj" file, which the user would then move into the Vision System's "Objects" folder.

PROGRAM FLOW:

TODO