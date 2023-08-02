import math

import numpy as np
import functools
import Helper

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from matplotlib.animation import FuncAnimation

# fct that draw the animation for one generation
# called externally
def draw(simulationIndex, generationId, unitSteps, environmentLimits, selection_shape, selection_constraints, lifeTime):
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(5, 5)

    positions = {}
    colors = get_colors(unitSteps.keys())
    for unitId in unitSteps.keys():
        positions[unitId] = Helper.format_unit_steps(unitSteps[unitId])

    selectionZone = Helper.get_selection_shape(selection_shape, selection_constraints)
    environmentZone = Helper.rectangle_draw(environmentLimits[0][0], environmentLimits[0][1], environmentLimits[1][0], environmentLimits[1][1])
    plotAxisLimits = [[1.1 * environmentLimits[0][0], 1.1 * environmentLimits[0][1]], [1.1 * environmentLimits[1][0], 1.1 * environmentLimits[1][1]]]

    anim = FuncAnimation(fig, functools.partial(animate, figure=fig, axis=ax, unitPositions=positions, unitDrawColors=colors, lifeTime=lifeTime, environmentLimits=plotAxisLimits, environmentZone=environmentZone, selectionZone=selectionZone), frames=lifeTime, interval=1, repeat=False, cache_frame_data=False)

    plt.suptitle("Simulation {0} | Generation {1}".format(simulationIndex, generationId))
    plt.show()

def generation_results_draw(generations, meanScores, survivorNumbers):
    p = len(generations)
    colors = iter(cm.rainbow(np.linspace(0, 1, len(generations))))
    fig, axis = plt.subplots(2,1)
    for i in range(len(generations)):
        color = next(colors)
        axis[0].plot(generations[i], meanScores[i], color=color)
        axis[0].set_title("Mean score")
        axis[1].plot(generations[i], survivorNumbers[i], color=color)
        axis[1].set_title("Survivor number")

    for ax in axis.flat:
        ax.label_outer()

    fig.canvas.manager.full_screen_toggle()
    plt.show()

# fct given as argument for FuncAnimation method in 'draw'
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


# tools
def get_colors(unitIds):
    result = {}
    colors = iter(cm.rainbow(np.linspace(0, 1, len(unitIds))))
    for id in unitIds:
        result[id] = next(colors)
    return result



# Function plot
def curve_draw(list_x, list_y):
    colors = iter(cm.rainbow(np.linspace(0, 1, len(list_x))))
    for i in range (len(list_x)):
        x = list_x[i]
        y = list_y[i]
        plt.plot(x, y, next(colors))
    plt.show()

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


# WIP
def DrawBrain(neuronCoordinates, edges):
    fig, ax = plt.subplots(1, 1)
    for i in range(len(neuronCoordinates)):
        xCircle, yCircle = Garbage.circle_draw([neuronCoordinates[0], neuronCoordinates[1]], 0.2)
        plt.plot(xCircle, yCircle, 'b-')
    for i in range(len(edges)):
        edge = edges[i]
        plt.plot(edge[0], edge[1], edge[2])
    return fig, ax