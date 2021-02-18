# Problem 4
# Mikołaj Koszczyc 145180 Bioinformatyka rok II

import generator
import random

def evaporate(rate = 0.2, t_init = 1):
    for i in range(len(pheromones)):
        for j in range(len(pheromones[i])):
            pheromones[i][j] = (1-rate)*pheromones[i][j] + rate*t_init # t_init = initial value of pheromone - cokolwiek to znaczy

def sillyAnt():
    # zaczyna z losowego wierzcholka
    start = random.randint(0,len(graph)) 
    sillyPath = []

    # tworzy pierwszą ścieżkę błądząc między wierzchołkami
    currVertex = start
    print(f'\n{graph[currVertex]}')
    
    print(f'CurrVertex = {currVertex}: {list(set(graph[currVertex])-set(sillyPath))}') # wierzchołki które nie zawierają się w ścieżce
    
    sillyPath.append(currVertex)
    # while list(set(graph[currVertex])-set(sillyPath)):
    
    
    # TODO: CHECK THIS SHIT
    # for item in graph[currVertex]:
    #     if item in sillyPath:
    #         continue
    #     else:
    #         choices = list(set(graph[currVertex])-set(sillyPath))
    #     # print(choices[1])
    #         currVertex = random.randint(0,len(choices))
    #         sillyPath.append(currVertex)
    #         print(sillyPath)
    # print(f'CurrVertex = {currVertex}: {set(graph[currVertex])-set(sillyPath)}') # wierzchołki które nie zawierają się w ścieżce

    


def PrintPheromones():
    print ('\nPheromones:')        
    for line in pheromones:
        print(line)

# TODO: Generate graph based on user input
graph = generator.GenerateGraph(10)
matrix = generator.CreateMatrix(graph)
generator.SaveMatrix(matrix)


x = 5 #

pheromones = [[5 for i in range(len(graph))] for j in range(len(graph))] # 2D array filled with zeros
# for i in range(len(graph)):
#     for j in range(len(graph[i])):

# PrintPheromones()

print ('\nGraph - adjacency list:')        
generator.PrintGraph(graph)

# TODO: ACO - metaheuristic

# Pierwsza iteracja
sillyAnt()

# Poprawianie rozwiazania
while True:
    