import tkinter as tk
from tkinter import font
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from app_flow import AppFlow
from map import obtain_coordinates
from tkinter import ttk
from tkinter import messagebox


class AppGUI(tk.Tk):
    school_address = ""

    def __init__(self):
        super().__init__()
        self.title("Optimize School Routes")
        # self.geometry("1200x800")
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
        style.configure("TLabel", padding=6, background="#17ECFA")

        ttk.Label(self, text="Nombre de la Escuela").grid(
            row=0, column=0, padx=30, pady=15
        )
        self.address_scholl_entry = ttk.Entry(self, width=80)
        self.address_scholl_entry.grid(row=1, column=0, padx=0, pady=10)

        ttk.Label(self, text="Direcciones").grid(row=2, column=0, padx=30, pady=15)
        self.address_entry = ttk.Entry(self, width=80)
        self.address_entry.grid(row=3, column=0, padx=30, pady=10)

        add_button = ttk.Button(self, text="Añadir Dirección", command=self.add_address)
        add_button.grid(row=3, column=2, padx=10, pady=10)

        add_button_scholl = ttk.Button(
            self, text="Añadir Escuela", command=self.add_address_scholl
        )
        add_button_scholl.grid(row=1, column=2, padx=10, pady=10)

        optimize_button = ttk.Button(
            self, text="Generar Ruta", command=self.optimize_route
        )
        optimize_button.grid(row=4, column=2, columnspan=15, padx=50, pady=10)

        self.result_text = tk.Text(self, height=10, width=70)
        self.result_text.grid(row=4, column=0, columnspan=1, padx=20, pady=80)

        ttk.Label(self, text="Información Algoritmo TSP").grid(
            row=0, column=62, padx=30, pady=0
        )

        style.configure("TFrame", padding=6, background="#000000")
        # Crear un Frame como contenedor para el Text
        text_frame = ttk.Frame(self, borderwidth=4, relief="groove")
        text_frame.grid(row=1, column=60, columnspan=5, rowspan=5, padx=25, pady=0)

        # Crear el Text widget dentro del Frame
        result_text_info_of_graph = tk.Text(
            text_frame, height=20, width=42, wrap="word"
        )
        result_text_info_of_graph.pack(expand=True, fill="both")

        # Configurar formato del texto
        bold_font = tk.font.Font(
            result_text_info_of_graph, result_text_info_of_graph.cget("font")
        )
        bold_font.configure(weight="bold", size=14, family="Arial")

        # Insertar texto con formato
        texto = "El problema del viajante (por sus siglas en inglés TSP) consiste en encontrar el camino único más corto que, dada una lista de ciudades y las distancias entre ellas, visita todas las ciudades una sola vez y regresa a la ciudad de origen."

        result_text_info_of_graph.insert(tk.END, texto)

        # Aplicar formato al texto insertado
        result_text_info_of_graph.tag_configure("bold", font=bold_font)
        result_text_info_of_graph.tag_add("bold", "1.0", "end-1c")

        # Justificar el texto
        result_text_info_of_graph.tag_configure("justify", justify="center")
        result_text_info_of_graph.tag_add("justify", "1.0", "end-1c")

        # Hacer el Text widget no editable
        result_text_info_of_graph.configure(state="disabled")

        self.center_window()

    def center_window(self):
        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Obtener las dimensiones de la ventana
        window_width = 1200
        window_height = 600

        # Calcular las coordenadas para centrar la ventana
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)

        # Establecer la geometría de la ventana para centrarla
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def add_address_scholl(self):
        self.school_address = (
            self.address_scholl_entry.get() + ", Tunja, Boyaca, Colombia"
        )
        if self.school_address:
            self.app.get_distance_between_addresses_and_school_address(
                self.school_address
            )
            self.address_scholl_entry.delete(0, tk.END)
            self.address_scholl_entry.config(state=tk.DISABLED)

    def add_address(self):
        address = self.address_entry.get()
        if self.school_address == "":
            messagebox.showwarning("Error", "No se ha agreado una escuela")
        elif address == "":
            messagebox.showwarning("Error", "Debes ingresar un nombre o una dirección")

        else:
            address = self.address_entry.get() + ", Tunja, Boyaca, Colombia"
            if address:
                if obtain_coordinates(address) == None:
                    messagebox.showinfo(
                        "Error", f"Dirección: '{address}' no se ha encontrado."
                    )
                    self.address_entry.delete(0, tk.END)
                else:
                    self.app.create_address(address)
                    self.address_entry.delete(0, tk.END)
                    messagebox.showinfo("Éxito", f"Dirección: '{address}' agregada.")

    def optimize_route(self):
        messagebox.showinfo("Notificación", "Generando ruta optima")
        self.add_address_scholl()
        self.app.calculate_time()
        self.app.get_distance_between_addresses()
        self.app.create_completed_address()
        result = self.app.creation_tsp(self.app.dictionary_graph())
        print(f"Ruta Optima: {result}")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

        # self.draw_tsp_graph(result)
        messagebox.showinfo("Notificación", "Ruta optima generada")
        # self.address_scholl_entry.config(state=tk.NORMAL)
        self.show_tsp_graph(result)
        self.app.reset_values()
        self.address_scholl_entry.config(state=tk.NORMAL)
        self.address_scholl_entry.insert(0, "")

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

        # Dibuja el grafo
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

        # Añade etiquetas a las aristas con números (índices de la ruta)
        edge_labels = {
            (tsp_result[i], tsp_result[i + 1]): i + 1
            for i in range(len(tsp_result) - 1)
        }
        edge_labels[(tsp_result[-1], tsp_result[0])] = len(
            tsp_result
        )  # Para el último salto al primer nodo
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

        plt.title("TSP Route")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    app_gui = AppGUI()
    app_gui.mainloop()
