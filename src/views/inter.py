import tkinter as tk
import sys
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sys.path.append("../models")
from tkinter import ttk
from app_flow import AppFlow


class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Optimize School Routes")
        self.geometry("800x600")
        self.configure(bg="#19BEE5")

        self.app = AppFlow()

        style = ttk.Style()
        style.configure(
            "TButton",
            padding=6,
            relief="flat",  # Bordes romos
            background="#000000",  # Color de fondo
            foreground="#000000",  # Color del texto
            font=("Arial", 12),
        )
        ttk.Label(self, text="Nombre de la Escuela").grid(
            row=0, column=0, padx=30, pady=15, sticky="w"
        )
        self.address_scholl_entry = ttk.Entry(self, width=80)
        self.address_scholl_entry.grid(row=1, column=0, padx=0, pady=10)

        ttk.Label(self, text="Direcciones").grid(
            row=2, column=0, padx=30, pady=15, sticky="w"
        )
        self.address_entry = ttk.Entry(self, width=80)
        self.address_entry.grid(row=3, column=0, padx=30, pady=10)

        add_button = ttk.Button(self, text="Add Address", command=self.add_address)
        add_button.grid(row=3, column=1, padx=10, pady=10)

        add_button_scholl = ttk.Button(
            self, text="Add Scholl", command=self.add_address_scholl
        )
        add_button_scholl.grid(row=1, column=1, padx=10, pady=10)

        optimize_button = ttk.Button(
            self, text="Optimize Route", command=self.optimize_route
        )
        optimize_button.grid(row=4, column=1, columnspan=15, padx=50, pady=10)

        self.result_text = tk.Text(self, height=10, width=70)
        self.result_text.grid(row=4, column=0, columnspan=1, padx=20, pady=80)

    def add_address(self):
        address = self.address_entry.get() + ", Tunja, Boyaca, Colombia"
        if address:
            self.app.create_address(address)
            self.address_entry.delete(0, tk.END)
            print(f"Address '{address}' added.")

    def add_address_scholl(self):
        scholl_address = self.address_scholl_entry.get() + ", Tunja, Boyaca, Colombia"
        if scholl_address:
            self.app.get_distance_between_addresses_and_scholl_address(scholl_address)
            self.address_scholl_entry.delete(0, tk.END)
            print(f"Address_scholl '{scholl_address}' added.")

    def optimize_route(self):
        self.add_address_scholl()
        self.app.calculate_time()
        self.app.get_distance_between_addresses()
        self.app.create_completed_address()
        result = self.app.creation_tsp(self.app.dictionary_graph())
        print(f"Ruta Optima: {result}")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

        self.draw_tsp_graph(result)
        self.show_tsp_graph(result)

    def draw_tsp_graph(self, tsp_result):
        G = nx.Graph()
        G.add_nodes_from(tsp_result)

        for i in range(len(tsp_result) - 1):
            G.add_edge(tsp_result[i], tsp_result[i + 1])

        G.add_edge(
            tsp_result[-1], tsp_result[0]
        )  # Conectar el último nodo con el primero para formar un ciclo

        pos = nx.spring_layout(G)
        fig, ax = plt.subplots()
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=700,
            node_color="skyblue",
            font_size=8,
            font_color="black",
            font_weight="bold",
            ax=ax,
        )

        plt.title("TSP Route")
        plt.axis("off")

        return fig

    def show_tsp_graph(self, tsp_result):
        G = nx.Graph()
        G.add_nodes_from(tsp_result)

        for i in range(len(tsp_result) - 1):
            G.add_edge(tsp_result[i], tsp_result[i + 1])

        if tsp_result:
            G.add_edge(
                tsp_result[-1], tsp_result[0]
            )  # Conectar el último nodo con el primero para formar un ciclo

        pos = nx.spring_layout(G)
        plt.figure()
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=700,
            node_color="skyblue",
            font_size=8,
            font_color="black",
            font_weight="bold",
        )
        plt.title("TSP Route")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    app_gui = AppGUI()
    app_gui.mainloop()
