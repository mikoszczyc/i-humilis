# Skrypt generuje spójny graf nieskierowany z wagami z przedziału podanego przez użytkownika.

import random
import time

def GenerateGraph(V, mindeg = 1, maxdeg = 6):
    """Generuje graf o [V] liczbie wierzcholow"""
    
    adj_lst = [[] for i in range(V)]
    graf = []
    for i in range(V):
        # losowanie stopnia dla wierzchołka
        if len(adj_lst[i]) > mindeg:
            i_deg = random.randint(len(adj_lst[i]), maxdeg) # both included
        else:
            i_deg = random.randint(mindeg, maxdeg) # both included
        
        # print(f'deg({i}) = {i_deg}')

        # dodawanie krawedzi do wierzcholka aby wypelnic jego stopien
        for iter in range(i_deg): # od 0 do i_deg-1 - w efekcie ilosc sie zgadza
            start_time = time.time()
            while len(adj_lst[i]) < i_deg:
                neighbour = random.randrange(0,V) # losuje sasiada
                if neighbour != i and len(adj_lst[neighbour]) < maxdeg:
                    adj_lst[neighbour].append(i)
                    adj_lst[i].append(neighbour)
                    # print("Vertex added")
                curr_time = time.time()
                if curr_time - start_time > 3:
                    break
                
            
    for sublst in adj_lst:
        sublst = list(dict.fromkeys(sublst))
        graf.append(sublst)
    
    # print('return graf')
    return graf
def PrintGraph(graph):
    for i, line in enumerate(graph,start=0):
        print(f'{i}:{line}')

def CreateMatrix(graph, minw = 1, maxw = 1):
    '''Creates matrix of provided graph \n
    Graph can be weighted using [minw] as minimum weight and [maxw] as maximum weight.\n
    Otherwise graph isn't weighted (every edge has weight = 1)
    '''

    matrix = [[0 for i in range(len(graph))] for j in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if matrix[i][graph[i][j]] == 0:
                # matrix[i][graph[i][j]] = 1
                if minw != maxw:
                    weight = random.randrange(minw, maxw+1)
                else:
                    weight = 1
                matrix[i][graph[i][j]] = weight
                matrix[graph[i][j]][i] = weight

    return matrix
def SaveMatrix(matrix):
    fh = open('graph.txt','w')
    for line in matrix:
        line = str(line)
        fh.write(line.lstrip('[').rstrip(']'))
        fh.write('\n')
    fh.close()
def PrintMatrix(matrix):
    for line in matrix:
        line = str(line)
        print(line.lstrip('[').rstrip(']'))

if __name__ == '__main__':
    G = GenerateGraph(20,1,6)
    matrix = CreateMatrix(G, 1, 100)
    for i, sublst in enumerate(G):
        print(f'{i}: {sublst}')

    SaveMatrix(matrix)