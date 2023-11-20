from itertools import permutations


def calcular_distancia(ruta, grafo):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += grafo[ruta[i]][ruta[i + 1]]
    distancia_total += grafo[ruta[-1]][ruta[0]]
    return distancia_total


def tsp(grafo):
    nodos = list(grafo.keys())
    rutas_posibles = permutations(nodos)
    ruta_optima = min(rutas_posibles, key=lambda ruta: calcular_distancia(ruta, grafo))
    return ruta_optima
