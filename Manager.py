import SqliteGateway
import UnitPlotHelper
import BrainReader
import matplotlib.pyplot as plt

# Main methods
def DrawSmallLife(startingGenerationId, dbFilePath):
    # Create connection to DB
    SqliteGateway.create_connection(dbFilePath)

    # Fetch last simulation
    lastSimulation = SqliteGateway.get_last_simulation()

    # Map parameters
    simulationId = lastSimulation[0]
    environmentLimits = get_environment_limits(lastSimulation)
    selectionShape = lastSimulation[2]
    selectionConstraints = lastSimulation[3]
    unitLifeTime = lastSimulation[4]

    # Fetch generation IDs for given simulation
    generationIds = SqliteGateway.get_generation_ids_for_simulation(simulationId)
    for generationId in generationIds:
        if generationId < startingGenerationId:
            continue
        # Fetch unit steps for that generation
        unitSteps = SqliteGateway.get_unit_steps_for_generation(simulationId, generationId)
        UnitPlotHelper.draw(simulationId, generationId, unitSteps, environmentLimits, selectionShape, selectionConstraints, unitLifeTime)

# tools
def get_environment_limits(simulation):
    result = []
    limits = simulation[1].split(':')
    scope = int((len(limits) - 1)/2)
    for i in range(scope):
        result.append([float(limits[2 * i].replace(',', '.')), float(limits[2 * i + 1].replace(',', '.'))])
    return result

# WIP
def DrawBrain():
    antBrainFilePath = r"D:\Codes\Test\AntWinners\200.txt"
    inputNumber = 25
    neutrals = [5, 3]
    outputNumber = 6
    layers = [inputNumber, neutrals, outputNumber]
    BrainReader.DrawBrain(antBrainFilePath, 5, layers)

    plt.show()