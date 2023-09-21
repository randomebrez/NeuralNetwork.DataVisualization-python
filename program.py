import random

import Manager
import Computation

# PARAMETERS #
dbFilePath = r"D:\Codes\VisualStudio\NeuralNetwork_Test_cSharp\dataBase.db"
startingGeneration = 50
simuMin = 11
simuMax = simuMin + 10
Manager.DrawSmallLife(startingGeneration, dbFilePath, 0)


fileName = r"D:\Codes\Python\NeuralNetwork.DataAnalyst-python\Decompositions.txt"
geneNumber = 15
genomeLength = 60



### Program ###
#Computation.generate_gnk(fileName, 30, 4)
# result = Computation.k_genome_probabilities_compute(geneNumber, genomeLength)
# print(result)
# sum = 0
# for proba in result:
#     sum += proba
# print(sum)



#Manager.draw_simulation_progression_curve(dbFilePath, simuMin, simuMax)
