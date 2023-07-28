import SqliteGateway
import UnitPlotHelper
import BrainReader
import matplotlib.pyplot as plt

def DrawSmallLife():
    startingGenerationId = 300
    dbFilePath = r"D:\Codes\VisualStudio\NeuralNetwork_Test_cSharp\dataBase.db"
    # dbFilePath = r"C:\Users\nico-\Documents\Codes\Tests\NeuralNetworkDatabase.txt"
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
    generationIds = SqliteGateway.get_generations(simulationId)
    for generationId in generationIds:
        if generationId < startingGenerationId:
            continue
        # Fetch unit steps for that generation
        unitSteps = SqliteGateway.get_unit_steps_for_generation(simulationId, generationId)
        UnitPlotHelper.draw(simulationId, generationId, unitSteps, environmentLimits, selectionShape, selectionConstraints, unitLifeTime)

def get_environment_limits(simulation):
    limits = simulation[1].split(':')
    return [[float(limits[0].replace(',', '.')), float(limits[1].replace(',', '.'))], [float(limits[2].replace(',', '.')), float(limits[3].replace(',', '.'))]]


def DrawBrain():
    antBrainFilePath = r"D:\Codes\Test\AntWinners\200.txt"
    inputNumber = 25
    neutrals = [5, 3]
    outputNumber = 6
    layers = [inputNumber, neutrals, outputNumber]
    BrainReader.DrawBrain(antBrainFilePath, 5, layers)

    plt.show()


### Program ###

DrawSmallLife()
##DrawBrain()
#UnitPlotHelper.PlotTanh(10)
#UnitPlotHelper.PlotSigmoid(100)



