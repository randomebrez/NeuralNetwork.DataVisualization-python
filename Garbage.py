import numpy as np

def translateY(ordonnees, delta):
    newOrdonnes = []
    for ord in ordonnees:
        newOrdonnes.append(ord + delta)
    return newOrdonnes


def translateX(abscisses, delta):
    newAbscisses = []
    for abs in abscisses:
        newAbscisses.append(abs + delta)
    return newAbscisses


def populate():
    xPos = []
    yPos = []
    for i in range(6):
        for j in range(6):
            xPos.append(np.cos(np.pi / 10 + np.pi / 90 + i * np.pi / 3 + j * np.pi / 45))
            yPos.append(np.sin(np.pi / 10 + np.pi / 90 + i * np.pi / 3 + j * np.pi / 45))
    return xPos, yPos


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


# file = open("C:\\Users\\Salocin\\Desktop\\Test\\neuralTework.txt", "r")
# lines = file.readlines()
# generations = []
# means = []
# maxValue = []
# zeroValue = []
# deuxValue = []
# quatreValue = []
# sixValue = []
# for i in range(len(lines)):
#     splittedLine = lines[i].split(';')
#     generations.append(float(splittedLine[0]))
#     means.append(float(splittedLine[1]))
#     total = float(splittedLine[2]) + float(splittedLine[3]) + float(splittedLine[4]) + float(splittedLine[5]) + float(splittedLine[6])
#     maxValue.append(100 * float(splittedLine[2]) / total)
#     zeroValue.append(100 * float(splittedLine[3]) / total)
#     deuxValue.append(100 * float(splittedLine[4]) / total)
#     quatreValue.append(100 * float(splittedLine[5]) / total)
#     sixValue.append(100 * float(splittedLine[6]) / total)
#
# plt.subplot(2, 1, 1)
# plt.plot(generations, means, 'b.')
# plt.axis([0, len(generations), 0, 100])
# # plt.axis([-50, 50, -50, 50])
#
# plt.subplot(2, 1, 2)
# plt.plot(generations, zeroValue, 'r.')
# plt.plot(generations,maxValue, 'g.')
# plt.plot(generations, deuxValue, 'b.')
# plt.plot(generations, quatreValue, 'y.')
# plt.plot(generations, sixValue, 'k.')
# plt.axis([0, len(generations), -1, 110])
#
# plt.show()