from itertools import permutations
import networkx as nx
import matplotlib.pyplot as plt


# Función para calcular la distancia total de una ruta
def calcular_distancia(ruta, grafo):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += grafo[ruta[i]][ruta[i + 1]]
    distancia_total += grafo[ruta[-1]][ruta[0]]  # Regresar al nodo origen
    return distancia_total


# Función para encontrar la ruta más corta
def tsp(grafo):
    nodos = list(grafo.keys())
    rutas_posibles = permutations(nodos)
    ruta_optima = min(rutas_posibles, key=lambda ruta: calcular_distancia(ruta, grafo))
    return ruta_optima


# Definir el grafo
grafo = {
    "Escuela": {"Escuela": 0, "Direccion1": 4, "Direccion2": 3},
    "Direccion1": {"Escuela": 6, "Direccion1": 0, "Direccion2": 5},
    "Direccion2": {"Escuela": 7, "Direccion1": 8, "Direccion2": 0},
}

ruta_optima = tsp(grafo)
print("Ruta óptima:", ruta_optima)


class Direccion:
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo = tiempo


# Crear un grafo completo aleatorio con 5 nodos representados por objetos Direccion
G = nx.complete_graph(5)

# Asignar objetos Direccion como nodos y atributos de tiempo como pesos de aristas
for node in G.nodes():
    G.nodes[node]["direccion"] = Direccion(nombre=f"Direccion{node}", tiempo=node + 1)

# Resolver el problema del Viajante Comerciante (TSP)
tsp_tour_nodes = nx.approximation.traveling_salesman_problem(
    G, weight="tiempo", cycle=True
)

# Obtener objetos Direccion para los nodos en la ruta óptima
direcciones_tour = [G.nodes[node]["direccion"] for node in tsp_tour_nodes]

# Crear un nuevo grafo dirigido para representar la ruta óptima
ruta_grafo = nx.DiGraph()

# Agregar nodos y aristas a la nueva gráfica
for i in range(len(direcciones_tour) - 1):
    ruta_grafo.add_node(direcciones_tour[i].nombre)
    ruta_grafo.add_node(direcciones_tour[i + 1].nombre)
    ruta_grafo.add_edge(
        direcciones_tour[i].nombre,
        direcciones_tour[i + 1].nombre,
        weight=direcciones_tour[i].tiempo,
    )

# Visualizar el grafo de la ruta óptima
pos = nx.spring_layout(ruta_grafo)
nx.draw(
    ruta_grafo,
    pos,
    with_labels=True,
    node_size=1000,
    node_color="skyblue",
    font_size=10,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=2,
    alpha=0.7,
    arrowsize=20,
)
labels = nx.get_edge_attributes(ruta_grafo, "weight")
nx.draw_networkx_edge_labels(ruta_grafo, pos, edge_labels=labels)
plt.title("Ruta Óptima")
plt.show()
