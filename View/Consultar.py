import tkinter as tk
from tkinter import ttk
from Controller.Usuario import Usuario

class ConsultarRanking:
    """
    Clase para crear una ventana que muestra el ranking de jugadores, con sus nombres y puntajes.

    Utiliza Tkinter para crear la interfaz gráfica y muestra los datos del ranking 
    utilizando un widget `Treeview` de Tkinter.

    Atributos:
        ventana: Ventana principal que contiene el ranking.
        usuario: Instancia de la clase Usuario, que maneja la lógica relacionada con los jugadores y la base de datos.
        lblTitulo: Etiqueta que muestra el título "Ranking de Jugadores".
        tabla: Tabla (Treeview) que muestra el ranking con dos columnas: "Nombre" y "Puntaje".
        listaRanking: Lista de tuplas que contienen los nombres de los jugadores y sus puntajes, obtenida de la base de datos.
        scrollbar: Barra de desplazamiento para la tabla, que permite visualizar más registros si es necesario.
    """

    def __init__(self):
        """
        Inicializa la ventana para mostrar el ranking y configura todos los componentes de la interfaz gráfica.

        Se conecta con la clase `Usuario` para obtener los datos del ranking de jugadores y los muestra 
        en un `Treeview` con dos columnas: Nombre y Puntaje.
        """
        self.ventana = tk.Toplevel()
        self.ventana.title("Ranking de Jugadores")  # Título de la ventana
        self.ventana.config(width=600, height=400)  # Configuración de tamaño de la ventana
        self.ventana.resizable(0, 0)  # La ventana no será redimensionable
        self.ventana.iconbitmap(r"iconos\valle.ico")

        self.usuario = Usuario()  # Instancia de la clase Usuario, que contiene la lógica de negocio

        # Crear el título de la ventana
        self.lblTitulo = tk.Label(self.ventana, text="Ranking de Jugadores", font=("Arial", 16))
        self.lblTitulo.pack(pady=10)

        # Crear la tabla de rankings (Treeview)
        self.tabla = ttk.Treeview(self.ventana, columns=["Nombre", "Puntaje"], show="headings")
        self.tabla.heading("Nombre", text="Nombre")  # Encabezado de la columna de nombres
        self.tabla.heading("Puntaje", text="Puntaje")  # Encabezado de la columna de puntajes

        # Obtener los datos del ranking llamando al método consultarRanking() de la clase Usuario
        self.listaRanking = self.usuario.consultarRanking()

        # Insertar cada fila del ranking en la tabla
        for ranking in self.listaRanking:
            self.tabla.insert("", "end", values=(ranking[0], ranking[1]))  # Inserta el nombre y puntaje

        # Empaquetar la tabla en la ventana, con ajuste de tamaño
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Agregar un scrollbar (barra de desplazamiento) a la tabla para permitir el desplazamiento vertical
        self.scrollbar = ttk.Scrollbar(self.ventana, orient="vertical", command=self.tabla.yview)
        self.tabla.config(yscrollcommand=self.scrollbar.set)  # Configura la tabla para que utilice el scrollbar
        self.scrollbar.pack(side="right", fill="y")  # Empaquetar la barra de desplazamiento a la derecha

        # Iniciar el bucle principal de la interfaz gráfica
        self.ventana.mainloop()
