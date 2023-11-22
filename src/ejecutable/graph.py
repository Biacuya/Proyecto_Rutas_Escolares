from itertools import permutations


def calculate_distance(route, graph):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += graph[route[i]][route[i + 1]]
    total_distance += graph[route[-1]][route[0]]
    return total_distance


def tsp(graph):
    nodos = list(graph.keys())
    routes_posibles = permutations(nodos)
    route_optima = min(
        routes_posibles, key=lambda route: calculate_distance(route, graph)
    )
    return route_optima
