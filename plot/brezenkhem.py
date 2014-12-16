__author__ = 'Sergey Sobko'

STEP_X, STEP_Y = 1, 1


def draw_line_brezenkhem_by_x(point1, point2):
    """Draws line dot by dot by x-axis using Brezenkhem algorithm"""
    if point1[0] > point2[0]:
        point1, point2 = point2, point1
    x0, x_end = point1[0], point2[0]
    y0, y_end = point1[1], point2[1]
    px = x_end - x0
    y_add = 0
    if y_end < y0:
        y_add = (y0 - y_end) * 2
    y_end += y_add
    py = y_end - y0
    x, y = x0, y0
    step_x, step_y = STEP_X, STEP_Y
    yield (x0, y0)
    yield (x_end, y_end - y_add)
    eps = 2 * py - px
    while x < x_end:
        x += step_x
        if eps > 0:
            y += step_y
        px = x_end - x
        py = y_end - y
        if eps >= 0:
            eps += 2 * (py - px)
        else:
            eps += 2 * py
        if y_add > 0:
            yield (x, py + y_end - y_add)
        else:
            yield (x, y)


def draw_line_brezenkhem_by_y(point1, point2):
    """Draws line dot by dot by y-axis using Brezenkhem algorithm"""
    if point1[1] > point2[1]:
        point1, point2 = point2, point1
    x0, x_end = point1[0], point2[0]
    y0, y_end = point1[1], point2[1]
    py = y_end - y0
    x_add = 0
    if x_end < x0:
        x_add = (x0 - x_end) * 2
    x_end += x_add
    px = x_end - x0
    x, y = x0, y0
    step_x, step_y = STEP_X, STEP_Y
    yield (x0, y0)
    yield (x_end - x_add, y_end)
    eps = 2 * px - py
    while y < y_end:
        y += step_y
        if eps > 0:
            x += step_x
        px = x_end - x
        py = y_end - y
        if eps >= 0:
            eps += 2 * (px - py)
        else:
            eps += 2 * px
        if x_add > 0:
            yield (px + x_end - x_add, y)
        else:
            yield (x, y)


def draw_line_brezenkhem(point1, point2):
    """Draws line dot by dot using Brezenkhem algorithm"""
    if abs(point2[0] - point1[0]) < abs(point2[1] - point1[1]):
        brezenkhem_function = draw_line_brezenkhem_by_y
    else:
        brezenkhem_function = draw_line_brezenkhem_by_x
    for point in brezenkhem_function(point1, point2):
        yield point
