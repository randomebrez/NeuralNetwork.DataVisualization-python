import math

import numpy as np
import functools
import Garbage

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from matplotlib.animation import FuncAnimation

def format_unit_steps(unitSteps):
    xPos = []
    yPos = []
    for step in unitSteps:
        positions = step[3].split("!")
        for position in positions[:-1]:
            coordinates = position.split(":")
            xPos.append(float(coordinates[0].replace(',', '.')))
            yPos.append(float(coordinates[1].replace(',', '.')))
    return xPos, yPos

def animate(i, figure, axis, unitPositions, unitDrawColors, lifeTime, environmentLimits, environmentZone, selectionZone):
    axis.clear()
    if i == lifeTime - 1:
        plt.close(figure)
        return

    plt.title("Step {0}".format(i))
    plt.plot(selectionZone[0], selectionZone[1], 'g-')
    plt.plot(environmentZone[0], environmentZone[1], 'r-')
    # Get the point from the points list at index i
    for key in unitPositions.keys():
        position = unitPositions[key]
        # Plot that point using the x and y coordinates
        axis.plot(position[0][i-1], position[1][i-1], color=unitDrawColors[key], marker='o')
    # Set the x and y axis to display a fixed range
    axis.set_xlim(environmentLimits[0])
    axis.set_ylim(environmentLimits[1])

def get_colors(unitIds):
    result = {}
    colors = iter(cm.rainbow(np.linspace(0, 1, len(unitIds))))
    for id in unitIds:
        result[id] = next(colors)
    return result

def draw(simulationIndex, generationId, unitSteps, environmentLimits, selection_shape, selection_constraints, lifeTime):
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(5, 5)

    positions = {}
    for unitId in unitSteps.keys():
        positions[unitId] = format_unit_steps(unitSteps[unitId])

    colors = get_colors(unitSteps.keys())
    selectionZone = get_selection_shape(selection_shape, selection_constraints)
    environmentZone = Garbage.rectangle_draw(environmentLimits[0][0], environmentLimits[0][1], environmentLimits[1][0], environmentLimits[1][1])
    plotAxisLimits = [[1.1 * environmentLimits[0][0], 1.1 * environmentLimits[0][1]], [1.1 * environmentLimits[1][0], 1.1 * environmentLimits[1][1]]]
    anim = FuncAnimation(fig, functools.partial(animate, figure=fig, axis=ax, unitPositions=positions, unitDrawColors=colors, lifeTime=lifeTime, environmentLimits=plotAxisLimits, environmentZone=environmentZone, selectionZone=selectionZone), frames=lifeTime, interval=1, repeat=False, cache_frame_data=False)

    plt.suptitle("Simulation {0} | Generation {1}".format(simulationIndex, generationId))
    plt.show()

def get_selection_shape(shape_enum, constraints):

    abs, ord = [], []
    splitConstraints = constraints.split(':')
    if (shape_enum == "Circular"):
        abs, ord = Garbage.circle_draw([float(splitConstraints[0].replace(',', '.')), float(splitConstraints[1].replace(',', '.'))], float(splitConstraints[2].replace(',', '.')))
    elif(shape_enum == "Rectangle"):
        abs, ord = Garbage.rectangle_draw(float(splitConstraints[0].replace(',', '.')), float(splitConstraints[1].replace(',', '.')), float(splitConstraints[2].replace(',', '.')), float(splitConstraints[3].replace(',', '.')))

    return abs, ord

def DrawBrain(neuronCoordinates, edges):
    fig, ax = plt.subplots(1, 1)
    for i in range(len(neuronCoordinates)):
        xCircle, yCircle = Garbage.circle_draw([neuronCoordinates[0], neuronCoordinates[1]], 0.2)
        plt.plot(xCircle, yCircle, 'b-')
    for i in range(len(edges)):
        edge = edges[i]
        plt.plot(edge[0], edge[1], edge[2])
    return fig, ax

def PlotTanh(modifier):
    alpha = (0.5 / modifier) * (math.log(1.9) - math.log(0.1))
    x = np.arange(-1.5 * modifier, 1.5 * modifier, 0.1)
    y = []
    y_mod = []
    y_mod2 = []
    for i in x:
        exp = np.exp(- 2 * i)
        exp_mod = np.exp(- 2 * i * alpha)
        exp_mod2 = np.exp(- 2 * i / alpha)
        y.append((1 - exp)/(1 + exp))
        y_mod.append((1 - exp_mod) / (1 + exp_mod))
        y_mod2.append((1 - exp_mod2) / (1 + exp_mod2))

    #plt.plot(x, y, 'r-')
    plt.plot(x, y_mod, 'b-')
    #plt.plot(x, y_mod2, 'g-')
    plt.show()

def PlotSigmoid(modifier):
    alpha = math.log(9) / modifier
    x = np.arange(-1.5 * modifier, 1.5 * modifier, 0.1)
    y = []
    y_mod = []
    y_mod2 = []
    for i in x:
        exp = np.exp(- i)
        exp_mod = np.exp(- i * alpha)
        exp_mod2 = np.exp(- i / alpha)
        y.append(1 / (1 + exp))
        y_mod.append(1 / (1 + exp_mod))
        y_mod2.append(1 / (1 + exp_mod2))

    plt.plot(x, y, 'r-')
    plt.plot(x, y_mod, 'b-')
    plt.plot(x, y_mod2, 'g-')
    plt.show()
