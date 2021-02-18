# Skrypt generuje spójny graf nieskierowany z wagami z przedziału podanego przez użytkownika.
import random



def GenerateGraph(V, mindeg = 1, maxdeg = 6):
    """Generuje graf o [V] liczbie wierzcholow"""
    
    adj_lst = [[] for i in range(V)]
    graf = []
    for i in range(V):
        if len(adj_lst[i]) > mindeg:
            i_deg = random.randint(len(adj_lst[i]), maxdeg) # both included
        else:
            i_deg = random.randint(mindeg, maxdeg) # both included
        
        print(f'deg({i}) = {i_deg}')

        for iter in range(i_deg):
            while True:
                neighbour = random.randrange(0,V) # losuje sasiada
                if(len(adj_lst[neighbour]) < maxdeg and neighbour != i):
                    break
                
            if(len(adj_lst[neighbour])+1 <= maxdeg and len(adj_lst[i])+1 <= maxdeg):
                adj_lst[neighbour].append(i)
                adj_lst[i].append(neighbour)
            
    for sublst in adj_lst:
        sublst = list(dict.fromkeys(sublst))
        graf.append(sublst)
    return graf
def PrintGraph(graph):
    for line in graph:
        print(line)

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

# print(GenerateGraph(10))
if __name__ == '__main__':
    G = GenerateGraph(20,1,6)
    matrix = CreateMatrix(G, 1, 100)
    for i, sublst in enumerate(G):
        print(f'{i}: {sublst}')

    SaveMatrix(matrix)