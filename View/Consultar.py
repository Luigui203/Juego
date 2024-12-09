import tkinter as tk
from tkinter import ttk
from Controller.Usuario import Usuario

class ConsultarRanking:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Ranking de Jugadores")
        self.ventana.config(width=600, height=400)
        self.ventana.resizable(0, 0)

        self.usuario = Usuario()

        self.lblTitulo = tk.Label(self.ventana, text="Ranking de Jugadores", font=("Arial", 16))
        self.lblTitulo.pack(pady=10)

        # Crear la tabla de rankings
        self.tabla = ttk.Treeview(self.ventana, columns=["Nombre", "Puntaje"], show="headings")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Puntaje", text="Puntaje")

        # Obtener los datos del ranking
        self.listaRanking = self.usuario.consultarRanking()

        for ranking in self.listaRanking:
            self.tabla.insert("", "end", values=(ranking[0], ranking[1]))

        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Agregar un scrollbar a la tabla
        self.scrollbar = ttk.Scrollbar(self.ventana, orient="vertical", command=self.tabla.yview)
        self.tabla.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        self.ventana.mainloop()
