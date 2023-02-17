import numpy as np
import functools
import SqliteGateway

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from matplotlib.animation import FuncAnimation

def format_unit_steps(unitSteps):
    xPos = []
    yPos = []
    for step in unitSteps:
        position = step[3].split(";")
        xPos.append(float(position[0].replace(',', '.')))
        yPos.append(float(position[1].replace(',', '.')))
    return xPos, yPos

def animate(i, figure, axis, unitPositions, unitDrawColors, lifeTime):
    axis.clear()
    if i == lifeTime - 1:
        plt.close(figure)
        return

    plt.title("Step {0}".format(i))
    # Get the point from the points list at index i
    for key in unitPositions.keys():
        position = unitPositions[key]
        # Plot that point using the x and y coordinates
        axis.plot(position[0][i-1], position[1][i-1], color=unitDrawColors[key], marker='o')
    # Set the x and y axis to display a fixed range
    axis.set_xlim([-50, 50])
    axis.set_ylim([-50, 50])

def get_colors(unitIds):
    result = {}
    colors = iter(cm.rainbow(np.linspace(0, 1, len(unitIds))))
    for id in unitIds:
        result[id] = next(colors)
    return result

def draw(simulationIndex, generationId, lifeTime):
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(5, 5)

    unitSteps = SqliteGateway.get_unit_steps_for_generation(simulationIndex, generationId)
    positions = {}
    for unitId in unitSteps.keys():
        positions[unitId] = format_unit_steps(unitSteps[unitId])

    colors = get_colors(unitSteps.keys())
    anim = FuncAnimation(fig, functools.partial(animate, figure=fig, axis=ax, unitPositions=positions, unitDrawColors=colors, lifeTime=lifeTime), frames=lifeTime, interval=1, repeat=False)

    plt.suptitle("Simulation {0} | Generation {1}".format(simulationIndex, generationId))
    plt.show()