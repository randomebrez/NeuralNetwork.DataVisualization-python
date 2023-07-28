import numpy as np

def translate_list(list, delta):
    result = []
    for i in range(len(list)):
        result.append(list[i] + delta)
    return result


def circle_draw(center, radius):
    theta = np.linspace(0, 2 * np.pi, 1000)
    ord = []
    abs = []
    for t in theta:
        abs.append(center[0] + radius * np.cos(t))
        ord.append(center[1] + radius * np.sin(t))
    return abs, ord

def rectangle_draw(xMin, xMax, yMin, yMax):
    ord = [yMin, yMin, yMax, yMax, yMin]
    abs = [xMin, xMax, xMax, xMin, xMin]
    return abs, ord

def get_selection_shape(shape_enum, constraints):
    abs, ord = [], []
    splitConstraints = constraints.split(':')
    if (shape_enum == "Circular"):
        abs, ord = circle_draw([float(splitConstraints[0].replace(',', '.')), float(splitConstraints[1].replace(',', '.'))], float(splitConstraints[2].replace(',', '.')))
    elif(shape_enum == "Rectangle"):
        abs, ord = rectangle_draw(float(splitConstraints[0].replace(',', '.')), float(splitConstraints[1].replace(',', '.')), float(splitConstraints[2].replace(',', '.')), float(splitConstraints[3].replace(',', '.')))

    return abs, ord

def format_unit_steps(unitSteps):
    xPos, yPos = [], []
    for step in unitSteps:
        positions = step[3].split("!")
        for position in positions[:-1]:
            coordinates = position.split(":")
            xPos.append(float(coordinates[0].replace(',', '.')))
            yPos.append(float(coordinates[1].replace(',', '.')))
    return xPos, yPos