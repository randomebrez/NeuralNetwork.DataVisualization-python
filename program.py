import Manager

# PARAMETERS #
dbFilePath = r"D:\Codes\VisualStudio\NeuralNetwork_Test_cSharp\dataBase.db"
startingGeneration = 160
simuMin = 1
simuMax = simuMin + 10


### Program ###
Manager.draw_simulation_progression_curve(dbFilePath, simuMin, simuMax)
#Manager.DrawSmallLife(startingGeneration, dbFilePath)