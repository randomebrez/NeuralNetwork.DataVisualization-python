import numpy as np
import matplotlib.pyplot as plt


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


def circleDraw():
    theta = np.linspace(0, 2 * np.pi, 1000)
    ord = []
    abs = []
    for t in theta:
        abs.append(np.cos(t))
        ord.append(np.sin(t))
    return abs, ord


file = open("C:\\Users\\nlouviaux\\Desktop\\Test\\neuralTework.txt", "r")
lines = file.readlines()
generations = []
means = []
maxValue = []
zeroValue = []
deuxValue = []
quatreValue = []
sixValue = []
for i in range(len(lines)):
    splittedLine = lines[i].split(';')
    generations.append(float(splittedLine[0]))
    means.append(float(splittedLine[1]))
    total = float(splittedLine[2]) + float(splittedLine[3]) + float(splittedLine[4]) + float(splittedLine[5]) + float(splittedLine[6])
    maxValue.append(100 * float(splittedLine[2]) / total)
    zeroValue.append(100 * float(splittedLine[3]) / total)
    deuxValue.append(100 * float(splittedLine[4]) / total)
    quatreValue.append(100 * float(splittedLine[5]) / total)
    sixValue.append(100 * float(splittedLine[6]) / total)

plt.subplot(2, 1, 1)
plt.plot(generations, means, 'b.')
plt.axis([0, len(generations), 0, 100])
# plt.axis([-50, 50, -50, 50])

plt.subplot(2, 1, 2)
plt.plot(generations, zeroValue, 'r.')
plt.plot(generations,maxValue, 'g.')
plt.plot(generations, deuxValue, 'b.')
plt.plot(generations, quatreValue, 'y.')
plt.plot(generations, sixValue, 'k.')
plt.axis([0, len(generations), -1, 110])

plt.show()

# width = 1.
# side = 2.
# rectPoints = [[0, 0, width, width, 0], [0, side, side, 0, 0]]
#
# xP = side * np.cos(2*np.pi/5)
# yP = side * np.sin(2*np.pi/5)
# pentaPoints = [[0, side, side + xP, side/2, - xP, 0],
#                [0, 0, yP, yP + side*np.cos(3*np.pi/10), yP, 0]]
#
#
# x = side * np.cos(np.pi/3)
# y = side * np.sin(np.pi/3)
#
# hexaPoints = [[0, side, side + x, side, 0, -x, 0],
#               [0, 0, y, 2 * y, 2 * y, y,0]]
#
# circlePoints = populate()
#
# print(np.linspace(-1,1,100))
#
# circleRopesX = [[1,-1],[0.5,-0.5],[-0.5,0.5]]
# circleRopesY = [[0,0],[np.sqrt(1-0.5**2), - np.sqrt(1-0.5**2)],[np.sqrt(1-0.5**2), - np.sqrt(1-0.5**2)]]
# circlePoints = circleDraw()
#
# plt.plot(circlePoints[0],circlePoints[1],"k-")
# for i in range(len(circleRopesX)):
#     plt.plot(circleRopesX[i], circleRopesY[i], "k-" )
# #plt.plot(rectPoints[0], rectPoints[1], "k-")
# #plt.plot(pentaPoints[0], translateY(pentaPoints[1], side + 1),"k-")
# #plt.plot(translateX(hexaPoints[0],width + 2), hexaPoints[1],"k-")
# #plt.plot(circlePoints[0], circlePoints[1], "x")
# plt.axis("equal")
# plt.axis("off")
#
# plt.show()
