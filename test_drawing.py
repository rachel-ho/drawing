import drawing as dw
import numpy as np

d = dw.Drawing()

def test_check_input():
    # command for creating canvas
    assert d.check_input(['C', '3', '2']) == True
    assert d.check_input(['c', '4', '1']) == True
    assert d.check_input(['C', '1', '2', '3']) == False
    assert d.check_input(['C', '2'] ) == False
    assert d.check_input(['C', 'a', '2']) == False
    assert d.check_input(['C', '-1', '9']) == False
    assert d.check_input(['C', '1', '9.1']) == False
    # command for drawing line
    assert d.check_input(['L', '1', '2', '3', '4']) == True
    assert d.check_input(['l', '2', '3', '3', '4']) == True
    assert d.check_input(['L', '1', '2', '3', '4', '5']) == False
    assert d.check_input(['L', '1', '2', '3']) == False
    assert d.check_input(['L', 'a', '2', '3', '4']) == False
    assert d.check_input(['L', '1', '2', '3', '-4']) == False
    assert d.check_input(['L', '1', '2', '3.2', '4']) == False
    # command for drawing rectangle
    assert d.check_input(['R', '1', '2', '3', '4']) == True
    assert d.check_input(['r', '2', '3', '3', '4']) == True
    assert d.check_input(['R', '1', '2', '3', '4', '5']) == False
    assert d.check_input(['R', '1', '2', '3']) == False
    assert d.check_input(['R', 'a', '2', '3', '4']) == False
    assert d.check_input(['R', '1', '2', '3', '-4']) == False
    assert d.check_input(['R', '1', '2', '3.2', '4']) == False
    # command for filling bucket
    assert d.check_input(['B', '1', '2', 'o']) == True
    assert d.check_input(['B', '1', '2', '*']) == True
    assert d.check_input(['B', '1', '2', '3']) == True
    assert d.check_input(['b', '1', '2', 'o']) == True
    assert d.check_input(['B', '1', '2', '3', 'o']) == False
    assert d.check_input(['B', '1', 'o']) == False
    assert d.check_input(['B', '1', 'a', 'o']) == False
    assert d.check_input(['B', '-1', '2', 'o']) == False
    assert d.check_input(['B', '1.1', '2', 'o']) == False
    assert d.check_input(['B', '1', '2', 'two']) == False
    # command for quitting
    assert d.check_input(['Q']) == True
    assert d.check_input(['q']) == True
    assert d.check_input(['Q', '1']) == False
    assert d.check_input(['Q', 'a']) == False
    # random command
    assert d.check_input(['O']) == False
    assert d.check_input(['CL', '1', '2']) == False
    assert d.check_input(['hello']) == False


def test_check_bounds():
    d.canvas_width = 3
    d.canvas_height = 3
    assert d.check_bounds(1, 1)  == True
    assert d.check_bounds(1, 2)  == True
    assert d.check_bounds(3, 1)  == True
    assert d.check_bounds(3, 2)  == True
    # x out of bounds
    assert d.check_bounds(0, 2)  == False
    assert d.check_bounds(4, 2)  == False
    # y out of bounds
    assert d.check_bounds(1, 0)  == False
    assert d.check_bounds(1, 4)  == False
    # x and y out of bounds
    assert d.check_bounds(0, 0)  == False
    assert d.check_bounds(4, 4)  == False
    assert d.check_bounds(4, 0)  == False
    assert d.check_bounds(0, 4)  == False


def test_check_line():
    # point
    assert d.check_line(1, 1, 1, 1) == True
    assert d.check_line(3, 1, 3, 1) == True
    assert d.check_line(1, 2, 1, 2) == True
    assert d.check_line(3, 2, 3, 2) == True
    # vertical line
    assert d.check_line(1, 1, 1, 2) == True
    assert d.check_line(3, 1, 3, 2) == True
    assert d.check_line(2, 2, 2, 1) == True
    # horizontal line
    assert d.check_line(1, 1, 3, 1) == True
    assert d.check_line(2, 2, 3, 2) == True
    assert d.check_line(3, 2, 1, 2) == True
    # not vertical or horizontal line
    assert d.check_line(1, 1, 2, 2) == False
    assert d.check_line(2, 1, 3, 2) == False


def test_check_rectangle():
    # non vertical or horizontal coordinates
    assert d.check_rectangle(1, 1, 2, 2) == True
    assert d.check_rectangle(1, 1, 3, 2) == True
    assert d.check_rectangle(3, 1, 2, 2) == True
    assert d.check_rectangle(1, 2, 3, 1) == True
    # vertical or horizontal coordinates
    assert d.check_rectangle(1, 1, 1, 2) == False
    assert d.check_rectangle(3, 1, 3, 2) == False
    assert d.check_rectangle(1, 1, 3, 1) == False
    assert d.check_rectangle(2, 2, 3, 2) == False


def test_check_bucket():
    d.canvas = np.full([3, 3], ' ')
    d.canvas[0, 0] = 'x'
    d.canvas[1, 1] = 'x'
    # coordinates with x (non-blank)
    assert d.check_bucket(0, 0) == False
    assert d.check_bucket(1, 1) == False
    # coordinates without x (blank)
    assert d.check_bucket(0, 2) == True
    assert d.check_bucket(1, 2) == True
    assert d.check_bucket(2, 0) == True
    assert d.check_bucket(2, 1) == True


def test_create_canvas():
    # numpy array with shape (h, w)
    assert d.create_canvas(2, 3).shape == (3, 2)
    assert d.create_canvas(10, 5).shape == (5, 10)


def test_print_canvas():
    canvas1 = np.full([3, 3], ' ')
    canvas2 = np.full([3, 2], ' ')
    canvas3 = np.full([3, 4], ' ')
    canvas3[1, 2:4] = 'x'
    assert d.print_canvas(canvas1) == '-----\n|   |\n|   |\n|   |\n-----'
    assert d.print_canvas(canvas2) == '----\n|  |\n|  |\n|  |\n----'
    assert d.print_canvas(canvas3) == '------\n|    |\n|  xx|\n|    |\n------'


def test_convert_coordinates():
    # single pair of coordinates for bucket fill
    assert d.convert_coordinates(1, 1) == (0, 0)
    assert d.convert_coordinates(2, 3) == (2, 1)
    assert d.convert_coordinates(10, 9) == (8, 9)
    # two pairs of coordinates for line
    assert d.convert_coordinates(2, 4, 2, 9) == (3, 9, 1, 2)
    assert d.convert_coordinates(2, 7, 2, 1) == (0, 7, 1, 2)
    assert d.convert_coordinates(5, 4, 8, 4) == (3, 4, 4, 8)
    assert d.convert_coordinates(7, 4, 2, 4) == (3, 4, 1, 7)
    # two pairs of coordinates for rectangle
    assert d.convert_coordinates(2, 4, 3, 9) == (3, 9, 1, 3)
    assert d.convert_coordinates(2, 7, 5, 1) == (0, 7, 1, 5)
    assert d.convert_coordinates(7, 4, 2, 8) == (3, 8, 1, 7)
    assert d.convert_coordinates(7, 5, 2, 3) == (2, 5, 1, 7)


def test_draw_line():
    # horizontal line
    d.canvas = np.full([3, 3], ' ')
    d.draw_line(1, 2, 3, 2)
    assert d.print_canvas(d.canvas) == '-----\n|   |\n|xxx|\n|   |\n-----'
    d.draw_line(2, 1, 2, 1)
    assert d.print_canvas(d.canvas) == '-----\n| x |\n|xxx|\n|   |\n-----'
    d.draw_line(2, 3, 3, 3)
    assert d.print_canvas(d.canvas) == '-----\n| x |\n|xxx|\n| xx|\n-----'
    d.draw_line(1, 3, 3, 3)
    assert d.print_canvas(d.canvas) == '-----\n| x |\n|xxx|\n|xxx|\n-----'
    # vertical line
    d.canvas = np.full([3, 3], ' ')
    d.draw_line(1, 1, 1, 3)
    assert d.print_canvas(d.canvas) == '-----\n|x  |\n|x  |\n|x  |\n-----'
    d.draw_line(3, 1, 3, 1)
    assert d.print_canvas(d.canvas) == '-----\n|x x|\n|x  |\n|x  |\n-----'
    d.draw_line(2, 1, 2, 2)
    assert d.print_canvas(d.canvas) == '-----\n|xxx|\n|xx |\n|x  |\n-----'
    d.draw_line(3, 1, 3, 2)
    assert d.print_canvas(d.canvas) == '-----\n|xxx|\n|xxx|\n|x  |\n-----'
    # vertical & horizontal line
    d.canvas = np.full([3, 3], ' ')
    d.draw_line(1, 2, 2, 2)
    assert d.print_canvas(d.canvas) == '-----\n|   |\n|xx |\n|   |\n-----'
    d.draw_line(2, 1, 2, 3)
    assert d.print_canvas(d.canvas) == '-----\n| x |\n|xx |\n| x |\n-----'
    d.draw_line(3, 3, 1, 3)
    assert d.print_canvas(d.canvas) == '-----\n| x |\n|xx |\n|xxx|\n-----'
    d.draw_line(3, 3, 3, 1)
    assert d.print_canvas(d.canvas) == '-----\n| xx|\n|xxx|\n|xxx|\n-----'


def test_draw_rectangle():
    d.canvas = np.full([4, 4], ' ')
    d.draw_rectangle(1, 1, 2, 2)
    assert d.print_canvas(d.canvas) == '------\n|xx  |\n|xx  |\n|    |\n|    |\n------'
    d.draw_rectangle(3, 1, 4, 3)
    assert d.print_canvas(d.canvas) == '------\n|xxxx|\n|xxxx|\n|  xx|\n|    |\n------'
    d.draw_rectangle(1, 3, 4, 4)
    assert d.print_canvas(d.canvas) == '------\n|xxxx|\n|xxxx|\n|xxxx|\n|xxxx|\n------'


def test_fill_bucket():
    d.canvas = np.full([6, 6], ' ')
    d.canvas_width = 6
    d.canvas_height = 6
    d.draw_line(1, 2, 2, 2)
    d.draw_rectangle(1, 4, 3, 6)
    d.draw_rectangle(4, 1, 6, 4)
    assert d.print_canvas(d.canvas) == '--------\n|   xxx|\n|xx x x|\n|   x x|\n|xxxxxx|\n|x x   |\n|xxx   |\n--------'
    d.fill_bucket(0, 4, '*')
    assert d.print_canvas(d.canvas) == '--------\n|   xxx|\n|xx x x|\n|   x x|\n|xxxxxx|\n|x x   |\n|xxx   |\n--------'
    d.fill_bucket(1, 4, '*')
    assert d.print_canvas(d.canvas) == '--------\n|   xxx|\n|xx x*x|\n|   x*x|\n|xxxxxx|\n|x x   |\n|xxx   |\n--------'
    d.fill_bucket(4, 1, 'o')
    assert d.print_canvas(d.canvas) == '--------\n|   xxx|\n|xx x*x|\n|   x*x|\n|xxxxxx|\n|xox   |\n|xxx   |\n--------'
    d.fill_bucket(1, 4, '@')
    assert d.print_canvas(d.canvas) == '--------\n|   xxx|\n|xx x@x|\n|   x@x|\n|xxxxxx|\n|xox   |\n|xxx   |\n--------'
    d.fill_bucket(0, 2, 'u')
    assert d.print_canvas(d.canvas) == '--------\n|uuuxxx|\n|xxux@x|\n|uuux@x|\n|xxxxxx|\n|xox   |\n|xxx   |\n--------'
    d.fill_bucket(4, 5, '#')
    assert d.print_canvas(d.canvas) == '--------\n|uuuxxx|\n|xxux@x|\n|uuux@x|\n|xxxxxx|\n|xox###|\n|xxx###|\n--------'







































#
