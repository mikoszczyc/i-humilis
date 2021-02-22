# Problem 4
# Mikołaj Koszczyc 145180 Bioinformatyka rok II

import generator
import random
import time
import math

V = 100 # ilosc wierzcholkow
x = 5 # mnoznik kary
ants = 30 # ilosc mrowek
enhancement_time = 10

def sillyAnt(graph):
    # zaczyna z losowego wierzcholka
    start = random.randint(0,len(graph)-1)
    vertices = set([i for i in range(len(graph))])
    sillyPath = []

    # tworzy pierwszą ścieżkę błądząc między wierzchołkami
    currVertex = start
    sillyPath.append(currVertex)
    
    while vertices-set(sillyPath):
        max = len(graph[currVertex]) # ilosc sasiadow
        # lista sąsiadów - wierzchołki w ścieżce
        choices = list(set(graph[currVertex]) - set(sillyPath))
        if choices:
            nextVertex = random.choice(choices)
        
        else:
            i = random.randint(0, max-1) # losuje sasiada
            nextVertex = graph[currVertex][i]
        sillyPath.append(nextVertex)
        currVertex = nextVertex

    return sillyPath

def brainyAnt(graph, iteration):
    # Mrówka zaczyna od losowego wierzchołka
    start = random.randint(0, len(graph)-1)
    smartPath = []
    vertices = set([i for i in range(len(graph))])
    start_time = time.time()

    currVertex = start
    smartPath.append(currVertex)
    while vertices-set(smartPath):
        max = len(graph[currVertex]) # ilosc sasiadow
        
        # czy mrówka korzysta z macierzy feromonowej? (T/N) zależy od ilości wykonanych iteracji
        # w początkowych iteracjach prawdopodobieństwo powinno być niskie ALE NIE 0
        roll = random.randint(1,100)
        if iteration < 10:
            threshold = 10
        else:
            threshold = 70 # zakładam, że powyżej progu iteracji mrówki chętniej wybierają macierz
        

        choices = list(set(graph[currVertex]) - set(smartPath))
        if roll < threshold:
            # mrówka korzysta z macierzy feromonowej
            # print("Using pheromone matrix")
            phLevels = {} # lista do której zapisuję poziomy feromonów na każdej ścieżce
            x = []

            
            if choices:
                # feromony na drodze do sąsiadów
                for i in choices:
                    phLevels[i] = pheromones[currVertex][i]
                    for j in range(int(phLevels[i])):
                        x.append(i)
                if len(x):
                    nextVertex = random.choice(x)
                else:
                    continue
            else:
                for i in range(max):
                    phLevels[i] = pheromones[currVertex][i]
                    for j in range(int(phLevels[i])):
                        x.append(i)
                if len(x):
                    nextVertex = random.choice(x)
                else:
                    continue
        else:
            # mrówka nie korzysta z macierzy feromonowej
            if choices:
                nextVertex = random.choice(choices)
        
            else:
                i = random.randint(0, max-1) # losuje sasiada
                nextVertex = graph[currVertex][i]
                    
        smartPath.append(nextVertex)
        currVertex = nextVertex

    return smartPath

def markWithPheromones(path, amount = 10):
    najwiekszy = pheromones[path[0]][path[1]]
    najmniejszy = 100
    for i in range(len(path)-1):
        j = i+1
        pheromones[path[i]][path[j]] += amount * 1/j # wartosc jest najwieksza dla najlepszego rozwiazania i potem maleje
        if pheromones[path[i]][path[j]] > najwiekszy:
            najwiekszy = pheromones[path[i]][path[j]]
        elif pheromones[path[i]][path[j]] < najmniejszy:
            if pheromones[path[i]][path[j]] == 0:
                continue
            najmniejszy = pheromones[path[i]][path[j]]
    if najwiekszy/najmniejszy > 20:
        flatten(path)

def evaporate(rate = 0.2):
    for i in range(len(pheromones)):
        for j in range(len(pheromones[i])):
            pheromones[i][j] = (1-rate)*pheromones[i][j]
            if pheromones[i][j] < 0:
                pheromones[i][j] = 0

def flatten(path):
    for i in range(len(path)-1):
        j = i+1
        if(pheromones[path[i]][path[j]] < 1):
            continue
        pheromones[path[i]][path[j]] = 1 + math.log2(float(pheromones[path[i]][path[j]]))

def PrintPheromones():
    print ('\nPheromones:')        
    for line in pheromones:
        print(line)

def SavePheromones():
    fh = open('ph.txt','w')
    for line in pheromones:
        line = str(line)
        fh.write(line.lstrip('[').rstrip(',]'))
        fh.write('\n')
    fh.close()

# # Generate graph based on user input
# graph = generator.GenerateGraph(V)
# matrix = generator.CreateMatrix(graph,1,100)
# generator.SaveMatrix(matrix)
for enhancement_time in range(10,121,10):
    for instance in range(50):
        print(f'{enhancement_time}:inst{instance}')
        fh = open(f'testy/inst{instance}.txt')
        # fh = open('testy/test.txt')
        graph = []
        sublst = []

        
        for ind, line in enumerate(fh, start=0):
            sublst = []
            line = line.strip().split(',')
            for i in range(len(line)):
                line[i] = line[i].strip()
                if line[i] != '0':
                    sublst.append(i)
            graph.append(sublst)

        fh.seek(0)
        matrix = [[0 for i in range(len(graph))] for j in range(len(graph))]
        for ind, line in enumerate(fh, start=0):
            line = line.strip().split(',')
            for ind2 in range(len(line)):
                matrix[ind][ind2] = int(line[ind2].strip())
        fh.close()

        pheromones = [[0 for i in range(len(graph))] for j in range(len(graph))] # 2D array filled with zeros

        # Pierwsza iteracja
        # Puszczamy np. 20 głupich mrówek
        solutions = []
        for i in range(ants):
            solution = sillyAnt(graph)
            # print(solution)
            solutions.append(solution)

        # Obliczamy koszt każdego rozwiązania
        quality = []

        for solution in solutions:
            cost = 0
            for i in range(len(solution)):
                if i+2 < len(solution):
                    if matrix[solution[i]][solution[i+1]] <= matrix[solution[i+1]][solution[i+2]]:
                        cost += matrix[solution[i]][solution[i+1]]
                    else:
                        cost += x * matrix[solution[i]][solution[i+1]]

            quality.append(int(cost))

        ranking = list(zip(solutions,quality))

        # Zapisujemy najlepsze rozwiazanie i zaznaczamy ścieżki feromonami
        ranking.sort(key=lambda x:x[1]) # sortowanie wg. jakosci sciezki
        bestSolution = ranking[0] # najlepsze rozwiązanie po 1 przejściu
        oh = open(f'wyniki/inst{instance}_results.txt','a')
        oh.write(f"r{enhancement_time}:{bestSolution[1]}\t")

        luckySillyAnts = int(ants/5) # 20% najlepszych głupich mrówek miało szczęście i zaznaczyły ścieżkę feromonami
        for i in range(luckySillyAnts):
            markWithPheromones(ranking[i][0],1-i/5/2) # wartosc feromonu spada razem z jakoscia polaczenia

        SavePheromones()

        start_time = time.time()
        iteration = 0
        # Poprawianie rozwiazania
        while time.time() - start_time < enhancement_time:
            iteration += 1
            quality = []
            for ant in range(ants):
                solution = brainyAnt(graph, iteration)
                solutions.append(solution)

            for solution in solutions:
                cost = 0
                for i in range(len(solution)):
                    if i+2 < len(solution):
                        if matrix[solution[i]][solution[i+1]] <= matrix[solution[i+1]][solution[i+2]]:
                            cost += matrix[solution[i]][solution[i+1]]
                        else:
                            cost += x * matrix[solution[i]][solution[i+1]]

                quality.append(int(cost))
            
            ranking = list(zip(solutions,quality))
            # Zapisujemy najlepsze rozwiazanie i zaznaczamy ścieżki feromonami
            ranking.sort(key=lambda x:x[1]) # sortowanie wg. jakosci sciezki
            bestSolution = ranking[0]
            # if iteration % 30 == 0:
            #     print("Iteracja: ",iteration,"best: ",bestSolution)
            evaporate()
        ranking = list(zip(solutions,quality))

        # Zapisujemy najlepsze rozwiazanie i zaznaczamy ścieżki feromonami
        ranking.sort(key=lambda x:x[1]) # sortowanie wg. jakosci sciezki
        bestSolution = ranking[0] # najlepsze rozwiązanie po 1 przejściu
        
        oh.write(f"{enhancement_time}:{bestSolution[1]}\n")
        oh.close()
