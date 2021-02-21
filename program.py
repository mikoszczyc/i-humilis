# Problem 4
# Mikołaj Koszczyc 145180 Bioinformatyka rok II

import generator
import random
import time

def evaporate(rate = 0.2, t_init = 1):
    for i in range(len(pheromones)):
        for j in range(len(pheromones[i])):
            pheromones[i][j] = (1-rate)*pheromones[i][j] + rate*t_init # t_init = initial value of pheromone - cokolwiek to znaczy
            if pheromones[i][j] < 0:
                pheromones[i][j] = 0

def markWithPheromones(path, amount = 1):
    for i in range(len(path)-1):
        j = i+1
        pheromones[path[i]][path[j]] += amount*10 # wartosc jest najwieksza dla najlepszego rozwiazania i potem maleje

def sillyAnt(graph):
    # zaczyna z losowego wierzcholka
    start = random.randint(0,len(graph)-1) 
    sillyPath = []

    # tworzy pierwszą ścieżkę błądząc między wierzchołkami
    currVertex = start
    print(f'currVertex = {currVertex}')
    sillyPath.append(currVertex)
    
    start_time = time.time()
    while len(sillyPath) < len(graph) and time.time() - start_time < 2:
        # print(f'rand 0,{len(graph[currVertex])-1}')
        max = len(graph[currVertex]) # ilosc sasiadow

        # lista sąsiadów - wierzchołki w ścieżce
        choices = list(set(graph[currVertex]) - set(sillyPath))
        # print(f'choices = {choices}')
        i = random.randint(0, max-1) # losuje sąsiada
        nextVertex = graph[currVertex][i] # przypisuje sąsiada jako kolejny wierzcholek
        if nextVertex not in sillyPath:
            sillyPath.append(nextVertex)
            currVertex = nextVertex
    
    return sillyPath

def brainyAnt(graph, iteration):
    # smart ant code here
    # 47:00 na nagraniu zaczyna opowiadać o mądrych mrówkach
    
    # TODO: 
    # mrówka zaczyna od losowego wierzchołka
    start = random.randint(0, len(graph)-1)
    currVertex = start
    smartPath = []
    smartPath.append(currVertex)
    start_time = time.time()
    while len(smartPath) < len(graph) and time.time() - start_time < 3:
        max = len(graph[currVertex])
        
        # czy mrówka korzysta z macierzy feromonowej? (T/N) zależy od ilości wykonanych iteracji
        # w początkowych iteracjach prawdopodobieństwo powinno być niskie ALE NIE 0
        roll = random.randint(1,100)
        if iteration < 5:
            threshold = 10
        else:
            threshold = 70 # zakładam, że powyżej progu iteracji mrówki chętniej wybierają macierz

        if roll < threshold:
            # mrówka korzysta z zawartosci macierzy feromonowej
            print("Using pheromone matrix")

            x = []
            for i in range(max):
                # sprawdzam wagi wszystkich polaczen
                for j in range(int(pheromones[currVertex][graph[currVertex][i]])):
                    x.append(i)
            
            # print(f'X = {x}')
            if len(x) != 0:
                nextVertex = random.choice(x)
            else:
                 continue
            
            if nextVertex not in smartPath:
                smartPath.append(nextVertex)
                currVertex = nextVertex
                # print(f'currVertex = {currVertex} smartPath = {smartPath}')        

        else:
            # mrówka nie korzysta z feromonów 
            print("Not using pheromones")
            # wybiera losowo kolejną ścieżkę
            # TODO:
            # UWAGA: Może się okazać, że mrówka wylosuje uzyta sciezke i nic nie zrobi

            i = random.randint(0, max-1) # TODO: tutaj są cały czas problemy - chyba naprawione
            nextVertex = graph[currVertex][i]
            if nextVertex not in smartPath: # and len(graph[nextVertex]) > 1 - czasami znaleziona sciezka jest bardzo krotka
                smartPath.append(nextVertex)
                currVertex = nextVertex
            # ALE potem może znowu podjąć decyzję o używaniu feromonów

    return smartPath
    

    # mrówka korzysta z feromonów
    # losowana jest liczba (1,100) /roll(), trzeba podzielić to na przedziały i wybrać na tej podstawie kolejną krawędź
    # im większa wartość feromonów tym większa szansa na wybranie ścieżki
    # np. 3 - 1 = 75% - 25%

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

# TODO: Generate graph based on user input
graph = generator.GenerateGraph(10)
matrix = generator.CreateMatrix(graph,1,100)
generator.SaveMatrix(matrix)

x = 5 # mnoznik kary
ants = 20 # ilosc mrowek

pheromones = [[0 for i in range(len(graph))] for j in range(len(graph))] # 2D array filled with zeros

# PrintPheromones()

print ('\nGraph - adjacency list:')        
generator.PrintGraph(graph)

# TODO: ACO - metaheuristic
enhancement_time = (int(input("Czas dzialania algorytmu [s]: ")))

# Pierwsza iteracja
# Puszczamy np. 20 głupich mrówek

solutions = []

for i in range(ants):
    solution = sillyAnt(graph)
    # print(solution)
    solutions.append(solution)

# Obliczamy koszt każdego rozwiazania
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

test = list(zip(solutions,quality))

# Zapisujemy najlepsze rozwiazanie i zaznaczamy ścieżki feromonami
test.sort(key=lambda x:x[1]) # sortowanie wg. jakosci sciezki
bestSolution = test[0] # najlepsze rozwiązanie po 1 przejściu

luckySillyAnts = int(ants/5) # 20% najlepszych głupich mrówek miało szczęście i zaznaczyły ścieżkę feromonami
for i in range(luckySillyAnts):
    markWithPheromones(test[i][0],1-i/5/2) # wartosc feromonu spada razem z jakoscia polaczenia

SavePheromones()

start_time = time.time()
# Poprawianie rozwiazania
while time.time() - start_time < enhancement_time:
    # pojedyncza iteracja:
    quality = []
    for i, ant in enumerate(range(ants)):
        solution = brainyAnt(graph, i)
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

    test = list(zip(solutions,quality))