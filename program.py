# Problem 4
# Mikołaj Koszczyc 145180 Bioinformatyka rok II

import generator

# TODO: Generate graph based on user input
graph = generator.GenerateGraph(10)
matrix = generator.CreateMatrix(graph)
# TODO: ACO - heuristic

x = 5 #

pheromones = [[0 for i in range(len(graph))] for j in range(len(graph))] # 2D array filled with 0s
# for i in range(len(graph)):
#     for j in range(len(graph[i])):
        
for line in pheromones:
    print(line)