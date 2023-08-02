import Manager
import Computation

# PARAMETERS #
dbFilePath = r"D:\Codes\VisualStudio\NeuralNetwork_Test_cSharp\dataBase.db"
startingGeneration = 500
simuMin = 1
simuMax = simuMin + 10

fileName = r"D:\Codes\Python\NeuralNetwork.DataAnalyst-python\Decompositions.txt"
geneNumber = 4
genomeLength = 7


### Program ###
Computation.print_gnk(fileName, 30)

#Manager.draw_simulation_progression_curve(dbFilePath, simuMin, simuMax)
#Manager.DrawSmallLife(startingGeneration, dbFilePath)