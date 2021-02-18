# Problem 4
# Mikołaj Koszczyc 145180 Bioinformatyka rok II

import generator
import random
import time

def evaporate(rate = 0.2, t_init = 1):
    for i in range(len(pheromones)):
        for j in range(len(pheromones[i])):
            pheromones[i][j] = (1-rate)*pheromones[i][j] + rate*t_init # t_init = initial value of pheromone - cokolwiek to znaczy

def sillyAnt(graph):
    # zaczyna z losowego wierzcholka
    start = random.randint(0,len(graph)) 
    sillyPath = []

    # tworzy pierwszą ścieżkę błądząc między wierzchołkami
    currVertex = start
    print(f'currVertex = {currVertex}')
    sillyPath.append(currVertex)
    print(f'SillyPath = {sillyPath}')
    
    start_time = time.time()
    while len(sillyPath) < len(graph) and time.time() - start_time < 1:
        i = random.randrange(len(graph[currVertex])-1)
        nextVertex = graph[currVertex][i]
        if nextVertex not in sillyPath:
            sillyPath.append(nextVertex)
            currVertex = nextVertex
        
    return sillyPath

def brainyAnt():
    # smart ant code here
    return ant

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

# PrintPheromones()

print ('\nGraph - adjacency list:')        
generator.PrintGraph(graph)

# TODO: ACO - metaheuristic
# enhancement_time = (int(input("Czas dzialania algorytmu [s]: ")))

# Pierwsza iteracja
print(f'First path: {sillyAnt(graph)}')

# # Poprawianie rozwiazania

# start_time = time.time() # początek poprawiania
# curr_time = time.time()
# while curr_time - start_time < enhancement_time:
#     curr_time = time.time()
#     # print("Brrr"+"r"*int(curr_time-start_time))
#     # print(curr_time-start_time)
    
