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


def nearest_neighbor(graph, start_node=None):
    if start_node is None:
        start_node = list(graph.keys())[0]

    unvisited_nodes = set(graph.keys())
    current_node = start_node
    path = [current_node]
    unvisited_nodes.remove(current_node)

    while unvisited_nodes:
        nearest_neighbor = min(
            unvisited_nodes, key=lambda node: graph[current_node][node]
        )
        path.append(nearest_neighbor)
        unvisited_nodes.remove(nearest_neighbor)
        current_node = nearest_neighbor

    path.append(start_node)  # Regresar al nodo inicial para cerrar el ciclo
    return path
