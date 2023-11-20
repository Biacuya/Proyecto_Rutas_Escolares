import tkinter as tk
import sys

sys.path.append("../models")
from tkinter import ttk
from app_flow import AppFlow


class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Optimize School Routes")

        self.app = AppFlow()

        self.address_entry = ttk.Entry(self, width=40)
        self.address_entry.grid(row=0, column=0, padx=10, pady=10)

        self.address_scholl_entry = ttk.Entry(self, width=40)
        self.address_scholl_entry.grid(row=1, column=0, padx=10, pady=10)

        add_button = ttk.Button(self, text="Add Address", command=self.add_address)
        add_button.grid(row=0, column=2, padx=10, pady=10)

        add_button_scholl = ttk.Button(
            self, text="Add Scholl", command=self.add_address_scholl
        )
        add_button_scholl.grid(row=1, column=2, padx=10, pady=10)

        optimize_button = ttk.Button(
            self, text="Optimize Route", command=self.optimize_route
        )
        optimize_button.grid(row=2, column=2, columnspan=2, pady=10)

        self.result_text = tk.Text(self, height=10, width=50)
        self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def add_address(self):
        address = self.address_entry.get()
        if address:
            self.app.create_address(address)
            self.address_entry.delete(0, tk.END)
            print(f"Address '{address}' added.")

    def add_address_scholl(self):
        scholl_address = self.address_scholl_entry.get()
        if scholl_address:
            self.app.get_distance_between_addresses_and_scholl_address(scholl_address)
            self.address_scholl_entry.delete(0, tk.END)

    def optimize_route(self):
        self.add_address_scholl()
        self.app.calculate_time()
        self.app.get_distance_between_addresses()
        self.app.create_completed_address()
        self.app.creation_tsp(self.app.dictionary_graph())

        result = "Optimized Route:\n"
        for aux in self.app.list_completed_address:
            result += f"{aux.get_name_address()}, Distance: {aux.get_distance_between_address_scholl_address()}, Time: {aux.get_time_list_address()}\n"

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)


if __name__ == "__main__":
    app_gui = AppGUI()
    app_gui.mainloop()
