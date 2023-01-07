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

outputDescriptions = {
    -1: "Random",
    0: "Right",
    1: "Left",
    2: "Up",
    3: "Down",
    4: "UpRight",
    5: "UpLeft",
    6: "DownLeft",
    7: "DownRight",
    8: "Stay"
}
file = open("C:\\Users\\nlouviaux\\Desktop\\Test\\neuralTework.txt", "r")
lines = file.readlines()
generations = []
means = []
outputLists = []
totalChoice = int(lines[0])
for i in range(1, len(lines)):
    splittedLine = lines[i].split(';')
    generations.append(float(splittedLine[0]))
    means.append(float(splittedLine[1]))
    for j in range(2, len(splittedLine)):
        if i == 1:
            outputLists.append([100 * float(splittedLine[j]) / totalChoice])
        else:
            outputLists[j-2].append(100 * float(splittedLine[j]) / totalChoice)

file.close()

outputMeans = []
for i in range(len(outputLists)):
    outputMeans.append(sum(outputLists[i])/float(len(outputLists[i])))
bigBossMean = sum(outputMeans)/len(outputLists)

plt.subplot(2, 1, 1)
plt.plot(generations, means, 'b.')
plt.axis([0, len(generations), 0, 100])
# plt.axis([-50, 50, -50, 50])

plt.subplot(2, 1, 2)
for i in range(len(outputLists)):
    label = outputDescriptions[i - 1]
    if outputMeans[i] > bigBossMean:
        label = label.upper()
    plt.plot(generations, outputLists[i], '.', label=label)
plt.legend()
plt.axis([0, len(generations), -1, 110])

plt.show()
