import SqliteGateway
import UnitPlotHelper
import matplotlib.pyplot as plt

### Program ###

lifeTime = 150
startingGeneration = 60
dbFilePath = r"D:\Codes\Test\NeuralNetworkDatabase.txt"

# # Create connection to DB
# SqliteGateway.create_connection(dbFilePath)
# # Fetch last simulation index
# lastSimulationIndex = SqliteGateway.get_last_simulation()
# # Fetch generation IDs for given simulation
# generations = SqliteGateway.get_generations(lastSimulationIndex)
#
# for generation in generations:
#     if generation < startingGeneration:
#         continue
#     UnitPlotHelper.draw(lastSimulationIndex, generation, lifeTime)


x_max = 20
y_max = 20
r = 3

n_abs = x_max // r
n_ord = 2 * y_max // r

x_plot = []
y_plot = []

for i in range(-n_abs, n_abs):
    if i % 2 == 0:
        for j in range(-n_ord, n_ord):
            if j % 2 == 1:
                continue
            else:
                x_plot.append(r * i)
                y_plot.append(r * j / 2)
    else:
        for j in range(-n_ord, n_ord):
            if j % 2 == 0:
                continue
            else:
                x_plot.append(r * i)
                y_plot.append(r * j / 2)

plt.plot(x_plot, y_plot, 'rx')
plt.show()
