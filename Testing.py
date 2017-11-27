import sys
import time
import cv2
import numpy as np

Points = []

def GetPoints(Event, X, Y, Flags, Parameter):
    global MouseX, MouseY
    global Points
    if Event == cv2.EVENT_LBUTTONDOWN:
        Points.append((X, Y))

File = "Test_Moon_1.png" # Change this as needed for now. Filename will be called in command input in the future.

print("> Welcome to the VisionSystem object creator.")
print("> First things first: What would you like this object to be named?")
ObjectName = input()
#Log("Object name saved.")
print("> Now you will need to draw an outline around the object, by clicking on each vertice, in order. (Clockwise or counterclockwise.)")
print("> Press enter to save the outline, press delete to remove the last point, and press escape to exit the outliner window.")
print("> IMPORTANT: Your image of the object must be taken in a \"neutral\" pose: with proper lighting, and at 0° rotation in all three planes; facing the camera.")
input("> Press enter to continue...")
print("Loading file \"" + File + "\"...")
cv2.namedWindow("Select the vertices of the target in order. Backspace = Delete last point, Enter = Save outline")
cv2.setMouseCallback("Select the vertices of the target in order. Backspace = Delete last point, Enter = Save outline", GetPoints)
Frame = cv2.imread("TestImages/" + File)

while True:
    NewFrame = Frame.copy()
    N = 0
    for Pair in Points:
        X, Y = Pair
        cv2.circle(NewFrame, (X, Y), 7, (0, 0, 0), -1)
        cv2.circle(NewFrame, (X, Y), 5, (0, 255, 0), -1)
        N += 1
    cv2.imshow("Select the vertices of the target in order. Backspace = Delete last point, Enter = Save outline", NewFrame)
    k = cv2.waitKey(20) & 0xFF
    if k == 13: # Enter key.
        cv2.destroyAllWindows()
        print("> Are you sure this is the outline you want to use to create the object? Type \"Y\" to continue; type \"N\" to return to the outliner.")
        Input = input()
        if Input.upper() == "Y":
#            Log("Saved object outline.") # TODO: Actually save the outline. Extract key features (Color Min/Max, etc)
            break
        else:
            print("> Returning to outliner window.")
            cv2.namedWindow("Select the vertices of the target in order. Backspace = Delete last point, Enter = Save outline")
            cv2.setMouseCallback("Select the vertices of the target in order. Backspace = Delete last point, Enter = Save outline", GetPoints)
    if k == 27: # Escape Key.
        print("> Bye!")
        sys.exit()
    if k == 8: # Delete Key.
        Points = Points[:-1]
cv2.destroyAllWindows()

print("> One more thing... How far away, in inches, was the object in the image from the camera?")
Distance = input()
print("> OK. Now that we've finished describing the object, would you like to view a fancy 3D graphic of it? (Y/N)")
Input = input()
if Input.upper() == "Y":
    print("> Not implemented yet.") # TODO: Implement this!
else:
    print("> Ok.")
print("> Finally, we need to save the object file. What would you like the filename to be? Keep it short and simple.")
FileName = input() + ".obj"
print("> Saving file \"" + FileName + "\"...")
print("> File saved. Bye!")
# TODO: Save it! Parts: ObjectName, Points, ColorMin, ColorMax, ..., Distance, FileName