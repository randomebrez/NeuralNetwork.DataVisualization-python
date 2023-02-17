import SqliteGateway
import UnitPlotHelper

### Program ###

lifeTime = 150
startingGeneration = 19
dbFilePath = r"D:\Codes\Test\NeuralNetworkDatabase.txt"

# Create connection to DB
SqliteGateway.create_connection(dbFilePath)
# Fetch last simulation index
lastSimulationIndex = SqliteGateway.get_last_simulation()
# Fetch generation IDs for given simulation
generations = SqliteGateway.get_generations(lastSimulationIndex)

for generation in generations:
    if generation < startingGeneration:
        continue
    UnitPlotHelper.draw(lastSimulationIndex, generation, lifeTime)
