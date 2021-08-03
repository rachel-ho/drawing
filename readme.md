## Drawing Program

This is a simple console drawing program written in Python.   It uses the NumPy library and pytest for unit testing.  NumPy arrays are used as the data structure to represent a canvas for better efficiency.  Install NumPy and pytest if necessary and run the script with Python 3 or above.


### Instructions
1. Save drawing.py and test_drawing.py to the same folder
2. Navigate to the folder from the terminal
3. For drawing: run drawing.py script with the *python drawing.py* command
4. For unit testing: run test_drawing.py script with the *pytest* command


### Description
This is an interactive drawing program based on command input from the user.  It will continue to run until the user quits.   There are five things you can do with this program: 1) create a canvas, 2) draw a vertical or horizontal line, 3) draw a rectangle, 4) fill a region, and 5) quit.   

**The program will inform the user and prompt for another command under the following conditions:**
- If they try to draw before a canvas is created
- If they try to create a new canvas when one already exists
- If they try to draw a slanted line (only vertical or horizontal lines can be drawn)
- If they try to draw a rectangle with vertical or horizontal coordinates
- If they try to fill a region and the coordinate they pick is not blank i.e. coordinate falls on a line or point
- If they input a coordinate that is out of bounds of the canvas
- If they enter an invalid command


### Commands

The first letter of the command can be either lower case or upper case.  All coordinates and dimensions (x, x1, x2, y, y1, y2) must be *positive integers*.  The character 'c' for the filling command must be a *single character*.

| Command       | Description
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| C w h         | Create a new canvas with width w and height h |
| L x1 y1 x2 y2 | Draw a vertical or horizontal line from (x1, y1) to (x2, y2) with the character 'x'<br>
                  Note: x1=x2 or y1=y2 |
| R x1 y1 x2 y2 | Draw a rectangle with opposite corners (x1, y1) and (x2, y2) with the character 'x'<br>
                  Note: x1!=x2 and y1!=y2; any opposite corners will work |
| B x y c       | Fill all contiguous points to (x, y) with the character 'c'<br>
                  Note: If region is already filled with another character it will replace the old character with the new character |
| Q             | Quit the program |
