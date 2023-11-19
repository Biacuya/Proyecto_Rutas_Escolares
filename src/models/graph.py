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


grafo = {
    "scholl": {
        "Calle 17, Tunja, Boyaca, Colombia": 6.45,
        "Calle 13, Tunja, Boyaca, Colombia": 4.51,
        "Calle 27, Tunja, Boyaca, Colombia": 7.51,
        "Los Hongos, Tunja, Boyaca, Colombia": 9.74,
    },
    "Calle 17, Tunja, Boyaca, Colombia": {
        "Calle 17, Tunja, Boyaca, Colombia": 0.0,
        "Calle 27, Tunja, Boyaca, Colombia": 2.77,
        "Calle 13, Tunja, Boyaca, Colombia": 1.46,
        "Los Hongos, Tunja, Boyaca, Colombia": 3.29,
        "scholl": 6.45,
    },
    "Calle 13, Tunja, Boyaca, Colombia": {
        "Calle 17, Tunja, Boyaca, Colombia": 1.46,
        "Calle 13, Tunja, Boyaca, Colombia": 0.0,
        "Calle 27, Tunja, Boyaca, Colombia": 0.0,  # Agregada subclave faltante
        "Los Hongos, Tunja, Boyaca, Colombia": 2.56,
        "scholl": 6.45,
    },
    "Calle 27, Tunja, Boyaca, Colombia": {
        "Calle 17, Tunja, Boyaca, Colombia": 2.77,
        "Calle 13, Tunja, Boyaca, Colombia": 3.28,
        "Calle 27, Tunja, Boyaca, Colombia": 0.0,
        "Los Hongos, Tunja, Boyaca, Colombia": 5.78,
        "scholl": 6.45,
    },
    "Los Hongos, Tunja, Boyaca, Colombia": {
        "Calle 17, Tunja, Boyaca, Colombia": 3.29,
        "Calle 27, Tunja, Boyaca, Colombia": 5.78,
        "Calle 13, Tunja, Boyaca, Colombia": 2.56,
        "scholl": 6.45,
    },
}



# Luego llama a la función tsp con el diccionario grafo
ruta_optima = tsp(grafo)
print("Ruta óptima:", ruta_optima)

# class Direccion:
#     def __init__(self, nombre, tiempo):
#         self.nombre = nombre
#         self.tiempo = tiempo


# # Crear instancias de la clase Direccion
# direccion1 = Direccion("Direccion1", 6)
# direccion2 = Direccion("Direccion2", 3)
# direccion3 = Direccion("Direccion3", 1)
# direccion4 = Direccion("Direccion4", 4)
# direccion5 = Direccion("Direccion5", 5)

# # Crear un grafo completo aleatorio con 5 nodos representados por objetos Direccion
# G = nx.complete_graph(5)

# # Asignar objetos Direccion como nodos y atributos de tiempo como pesos de aristas
# for node in G.nodes():
#     if "direccion" not in G.nodes[node]:
#         G.nodes[node]["direccion"] = Direccion(
#             nombre=f"Direccion{node}", tiempo=node + 1
#         )

# # Resolver el problema del Viajante Comerciante (TSP)
# tsp_tour_nodes = nx.approximation.traveling_salesman_problem(
#     G, weight="tiempo", cycle=True
# )

# # Obtener objetos Direccion para los nodos en la ruta óptima
# direcciones_tour = [
#     G.nodes[node]["direccion"]
#     for node in tsp_tour_nodes
#     if "direccion" in G.nodes[node]
# ]

# # Crear un nuevo grafo dirigido para representar la ruta óptima
# ruta_grafo = nx.DiGraph()

# # Agregar nodos y aristas a la nueva gráfica
# for i in range(len(direcciones_tour) - 1):
#     direccion_actual = direcciones_tour[i]
#     siguiente_direccion = direcciones_tour[i + 1]

#     # Agregar nodo actual y siguiente nodo al grafo
#     ruta_grafo.add_node(direccion_actual.nombre, tiempo=direccion_actual.tiempo)
#     ruta_grafo.add_node(siguiente_direccion.nombre, tiempo=siguiente_direccion.tiempo)

#     # Agregar arista con atributos de peso al grafo
#     peso_arista = (
#         direccion_actual.tiempo
#     )  # Puedes personalizar esto según tus necesidades
#     ruta_grafo.add_edge(
#         direccion_actual.nombre, siguiente_direccion.nombre, weight=peso_arista
#     )

# # Visualizar el grafo de la ruta óptima
# pos = nx.spring_layout(ruta_grafo)
# nx.draw(
#     ruta_grafo,
#     pos,
#     with_labels=True,
#     node_size=1000,
#     node_color="skyblue",
#     font_size=10,
#     font_color="black",
#     font_weight="bold",
#     edge_color="gray",
#     width=2,
#     alpha=0.7,
#     arrowsize=20,
# )
# labels = nx.get_edge_attributes(ruta_grafo, "weight")
# nx.draw_networkx_edge_labels(ruta_grafo, pos, edge_labels=labels)
# plt.title("Ruta Óptima con Aproximación al TSP")
# plt.show()
