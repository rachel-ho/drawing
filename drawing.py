import numpy as np

class Drawing():
    def __init__(self):
        self.canvas = None
        self.canvas_width = 0
        self.canvas_height = 0

    def draw(self):
        active = True #loop until user quits
        while active:
            command = input('\nenter command: ').split()
            action = command[0].upper()

            #check command input - only proceed if valid; otherwise loop until valid input is provided
            if self.check_input(command):

                #quit drawing - command Q
                if action == 'Q':
                    active = False

                #create new canvas (required before drawing) - command C w h
                elif action == 'C' and self.canvas is None:
                    self.canvas_width = int(command[1])
                    self.canvas_height = int(command[2])
                    self.canvas = self.create_canvas(self.canvas_width, self.canvas_height)
                    self.print_canvas(self.canvas)

                #inform user that canvas already exists if they try to create one when it already exists
                elif action == 'C':
                    print('\nCanvas already exists - quit first before creating a new one')

                #request user to create canvas if they try to draw before canvas is created
                elif action in ('L', 'R', 'B') and self.canvas is None:
                    print('\nA new canvas needs to be created before drawing')

                #draw horizontal or vertical lines with x - command L x1 y1 x2 y2
                elif action == 'L':
                    x1 = int(command[1])
                    y1 = int(command[2])
                    x2 = int(command[3])
                    y2 = int(command[4])
                    if self.check_bounds(x1, y1) and self.check_bounds(x2, y2) and self.check_line(x1, y1, x2, y2):
                        self.draw_line(x1, y1, x2, y2)
                        self.print_canvas(self.canvas)

                #draw rectangle with x - command R x1 y1 x2 y2
                elif action == 'R':
                    x1 = int(command[1])
                    y1 = int(command[2])
                    x2 = int(command[3])
                    y2 = int(command[4])
                    if self.check_bounds(x1, y1) and self.check_bounds(x2, y2) and self.check_rectangle(x1, y1, x2, y2):
                        self.draw_rectangle(x1, y1, x2, y2)
                        self.print_canvas(self.canvas)

                #fill all contiguous points to (x, y) with specified input character c - command B x y c
                elif action == 'B':
                    x = int(command[1])
                    y = int(command[2])
                    c = command[3]
                    i, j = self.convert_coordinates(x, y)
                    if self.check_bounds(x, y) and self.check_bucket(i, j):
                        self.fill_bucket(i, j, c)
                        self.print_canvas(self.canvas)

                else:
                    pass

            #request for valid input if command input validation fails
            else:
                print('\nInvalid command')
                print('Valid commands include: ')
                print('C w h')
                print('L x1 y1 x2 y2')
                print('R x1 y1 x2 y2')
                print('B x y c')
                print('Q')
                print('Refer to readme file for further details')


    #check if action (first letter of command) is valid: C, L, R, B, Q
    #check if number of arguments provided is correct
    #check if data types of arguements are correct
    def check_input(self, command):
        action = command[0].upper()
        if action == 'C':
            if len(command) != 3:
                return False
            elif command[1].isnumeric() and command[2].isnumeric():
                return True
            else:
                return False
        elif action in ('L', 'R'):
            if len(command) != 5:
                return False
            elif command[1].isnumeric() and command[2].isnumeric() and command[3].isnumeric() and command[4].isnumeric():
                return True
            else:
                return False
        elif action == 'B':
            if len(command) != 4:
                return False
            elif command[1].isnumeric() and command[2].isnumeric() and len(command[3]) == 1:
                return True
            else:
                return False
        elif action == 'Q':
            if len(command) != 1:
                return False
            else:
                return True
        else:
            return False

    #check if coordinates are out of bounds
    def check_bounds(self, x, y):
        if x < 1 or x > self.canvas_width:
            print('\nx coordinate is out of bounds - valid x coordinates are between 1 and ' + str(self.canvas_width) + ', inclusive')
            return False
        elif y < 1 or y > self.canvas_height:
            print('\ny coordinate is out of bounds - valid y coordinates are between 1 and ' + str(self.canvas_height) + ', inclusive')
            return False
        else:
            return True

    #check if coordinates for line correspond to either horizontal or vertical line
    def check_line(self, x1, y1, x2, y2):
        if x1 != x2 and y1 != y2:
            print('\nOnly horizontal or vertical lines can be drawn i.e. either x1=x2 or y1=y2')
            return False
        else:
            return True

    #check if coordinates for rectangle are correct i.e. x1!=x2 and y1!=y2
    def check_rectangle(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            print('\nA rectangle cannot be drawn if x1=x2 or y1=y2')
            return False
        else:
            return True

    #check if coordinates provided for bucket fill is blank
    def check_bucket(self, i, j):
        if self.canvas[i, j] == 'x':
            print('\nA point on a line is selected so no points will be filled')
            return False
        else:
            return True

    #create canvas of width w and height h as numpy array with shape (h, w)
    def create_canvas(self, w, h):
        r = h
        c = w
        canvas = np.full([r, c], ' ')
        return canvas

    #print canvas by converting it from array to string and add borders
    def print_canvas(self, canvas):
        r = canvas.shape[0]
        c = canvas.shape[1]
        top = ''.join(['-' for i in range(c+2)])
        bottom = ''.join(['-' for i in range(c+2)])
        canvas_s = top + '\n'
        for i in range(r):
            canvas_s = canvas_s + '|' + ''.join(map(str, canvas[i])) + '|\n'
        canvas_s = canvas_s + bottom
        print(canvas_s)
        return canvas_s

    #convert coordinates to numpy index and use min, max to reverse order of coordinates if x2>x1 or y2>y1
    def convert_coordinates(self, *args):
        if len(args) == 4:
            x1, y1, x2, y2 = args
            r1 = min(y1, y2) - 1
            r2 = max(y1, y2)
            c1 = min(x1, x2) - 1
            c2 = max(x1, x2)
            return r1, r2, c1, c2
        else:
            x, y = args
            r = y - 1
            c = x - 1
            return r, c

    #draw vertical or horizontal line by inserting x into corresponding indices of array
    def draw_line(self, x1, y1, x2, y2):
        r1, r2, c1, c2 = self.convert_coordinates(x1, y1, x2, y2)
        self.canvas[r1:r2, c1:c2] = 'x'

    #draw rectangle by drawing 4 lines using draw_line function
    def draw_rectangle(self, x1, y1, x2, y2):
        self.draw_line(x1, y1, x2, y1)
        self.draw_line(x2, y1, x2, y2)
        self.draw_line(x2, y2, x1, y2)
        self.draw_line(x1, y2, x1, y1)

    #fill all contiguous points of (x, y) with character c by recursively calling itself on all 4 surrounding points
    def fill_bucket(self, i, j, c):

        #base case - stop recursion if x is found or if point is already filled
        if self.canvas[i, j] == 'x' or self.canvas[i, j] == c:
            return

        #fill point (i, j) with character c
        self.canvas[i, j] = c

        #recurse left
        if j > 0:
            self.fill_bucket(i, j-1, c)

        #recurse right
        if j < self.canvas_width-1:
            self.fill_bucket(i, j+1, c)

        #recurse up
        if i > 0:
            self.fill_bucket(i-1, j, c)

        #recurse down
        if i < self.canvas_height-1:
            self.fill_bucket(i+1, j, c)

if __name__ == '__main__':
    my_drawing = Drawing()
    my_drawing.draw()
