# Skrypt generuje spójny graf nieskierowany z wagami z przedziału podanego przez użytkownika.
import random



def GenerateGraph(V, mindeg = 1, maxdeg = 6):
    """Generuje graf o [V] liczbie wierzcholow"""
    
    # for i in range(len(matrix)):
    #     i_deg = random.randrange(mindeg,maxdeg+1)
    #     for j in range(len(matrix[i])):
    #         if i == j: continue
            
    #         # matrix[i][j] = random.randrange(mindeg, maxdeg+1)


    # return matrix

    adj_lst = [[] for i in range(V)]
    graf = []
    for i in range(V):
        if len(adj_lst[i]) > mindeg:
            i_deg = random.randrange(len(adj_lst[i]), maxdeg)
        else:
            i_deg = random.randrange(mindeg, maxdeg)
        
        print(f'deg({i}) = {i_deg}')

        for iter in range(i_deg):
            while True:
                neighbour = random.randrange(V) # losuje sasiada
                if(len(adj_lst[neighbour]) < maxdeg and neighbour != i):
                    break
                
            if(len(adj_lst[neighbour]) < maxdeg-1):
                adj_lst[neighbour].append(i)
                adj_lst[i].append(neighbour)
            
    for sublst in adj_lst:
        sublst = list(dict.fromkeys(sublst))
        graf.append(sublst)
    return graf

def CreateMatrix(graph):
    matrix = [[0 for i in range(len(graph))] for j in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if matrix[i][graph[i][j]] == 0:
                matrix[i][graph[i][j]] = 1

    return matrix
# print(GenerateGraph(10))
if __name__ == '__main__':
    G = GenerateGraph(10)
    matrix = CreateMatrix(G)
    for i, sublst in enumerate(G):
        print(f'{i}: {sublst}')

    for line in matrix:
        for symbol in line:
            print(symbol, end=',')
        print()