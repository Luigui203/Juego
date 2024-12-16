import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess  # Para ejecutar el juego
from Controller.Usuario import Usuario
from Tooltip import Tooltip
from View.Registrar import Registrar
from View.Consultar import ConsultarRanking  # Importamos la clase que muestra el ranking

class Loggin():

    def consultarRanking(self):
        # Llamar a la ventana del ranking
        ranking_ventana = ConsultarRanking()

    def validarCampos(self, event):
        if len(self.txtUsuario.get()) >= 5 and len(self.txtPassword.get()) >= 5:
            if len(self.txtUsuario.get()) <= 25 and len(self.txtPassword.get()) <= 25:
                self.btnIngresar.config(state="normal")
            elif len(self.txtUsuario.get()) <= 25 and len(self.txtPassword.get()) >= 25:
                self.txtPassword.delete(len(self.txtPassword.get()) - 1, END)
            elif len(self.txtUsuario.get()) >= 25 and len(self.txtPassword.get()) <= 25:
                self.txtUsuario.delete(len(self.txtUsuario.get()) - 1, END)
        else:
            self.btnIngresar.config(state="disabled")

    def validarUsuario(self, event):
        caracter = event.keysym
        if caracter.isalpha() or caracter == '.' or caracter == "BackSpace":
            self.txtUsuario.config(bg="#ffffff", fg="#000000")
        
    def verCaracteres(self, event):
        if self.bandera == True:
            self.txtPassword.config(show='*')
            self.btnVer.config(text="Ver")
            self.bandera = False
        else:
            self.txtPassword.config(show='')
            self.btnVer.config(text="Ocu")
            self.bandera = True

    def ingresar(self, event):
        # Asegúrate de que el nombre de usuario y la contraseña sean válidos
        miUsuario = Usuario()
        usuario = self.txtUsuario.get()  # Acceder al nombre de usuario antes de cerrar la ventana
        if miUsuario.iniciarSesion(usuario, self.txtPassword.get(), self.ventana):
            self.ventana.destroy()  # Cerrar la ventana de login solo después de validación
            self.iniciar_juego(usuario)  # Pasar el nombre de usuario al iniciar el juego
        
    def iniciar_juego(self, nombreUsuario):
        # Ejecutar juego.py y pasar el nombre de usuario como argumento
        subprocess.run(["python", "juego.py", nombreUsuario])

    def abrir_ventana_registro(self):
        self.ventana.destroy()  # Cerrar la ventana de login
        registrar_ventana = Registrar()  # Crear nueva ventana de registro
        registrar_ventana.ventana.mainloop()  # Ejecutar el mainloop de la nueva ventana

    def limpiarCampos(self):
        # Limpiar los campos de texto
        self.txtUsuario.delete(0, END)
        self.txtPassword.delete(0, END)


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0, 0)
        self.ventana.config(width=500, height=400)
        self.ventana.title("Inicio de Sesión")
        self.inicio_exitoso = False  # Bandera para verificar inicio de sesión exitoso

        self.bandera = False

        # Estilos personalizados para los botones
        style = ttk.Style()
        style.configure("Custom.TButton",
                        font=("Helvetica", 10, "bold"),
                        padding=6,
                        relief="raised",
                        borderwidth=2,
                        focuscolor="none")

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Inicio Sesión", font=("Helvetica", 16, "bold"))
        self.lblTitulo.place(relx=0.5, y=40, anchor="center")

        # Marco principal para entradas
        frame_inputs = ttk.Frame(self.ventana, padding="10")
        frame_inputs.place(relx=0.5, rely=0.4, anchor="center")

        # Usuario
        self.lblUsuario = tk.Label(frame_inputs, text="Usuario*: ", font=("Helvetica", 10))
        self.lblUsuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.txtUsuario = tk.Entry(frame_inputs, width=25)
        self.txtUsuario.grid(row=0, column=1, padx=10, pady=10)
        self.txtUsuario.bind("<KeyRelease>", self.validarCampos)
        self.txtUsuario.bind("<Key>", self.validarUsuario)
        Tooltip(self.txtUsuario, "Ingrese su nombre de Usuario, solo letras minúsculas.\nmin 5 caracteres, max 25 caracteres")

        # Contraseña
        self.lblPassword = tk.Label(frame_inputs, text="Password*: ", font=("Helvetica", 10))
        self.lblPassword.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.txtPassword = tk.Entry(frame_inputs, show="*", width=25)
        self.txtPassword.grid(row=1, column=1, padx=10, pady=10)
        self.txtPassword.bind("<KeyRelease>", self.validarCampos)

        # Botón Ver Contraseña
        self.btnVer = ttk.Button(frame_inputs, text="Ver", style="Custom.TButton")
        self.btnVer.grid(row=1, column=2, padx=5, pady=10)
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)

        # Marco para botones
        frame_buttons = ttk.Frame(self.ventana, padding="10")
        frame_buttons.place(relx=0.5, rely=0.75, anchor="center")

        # Botones principales
        self.btnIngresar = ttk.Button(frame_buttons, text="Ingresar", style="Custom.TButton")
        self.btnIngresar.grid(row=0, column=0, padx=10, pady=10)
        self.btnIngresar.bind("<Button-1>", self.ingresar)

        self.btnLimpiar = ttk.Button(frame_buttons, text="Limpiar", style="Custom.TButton", command=self.limpiarCampos)
        self.btnLimpiar.grid(row=0, column=1, padx=10, pady=10)

        self.btnRegistrar = ttk.Button(frame_buttons, text="Registrarse", style="Custom.TButton", command=self.abrir_ventana_registro)
        self.btnRegistrar.grid(row=0, column=2, padx=10, pady=10)

        self.btnRanking = ttk.Button(frame_buttons, text="Consultar Ranking", style="Custom.TButton", command=self.consultarRanking)
        self.btnRanking.grid(row=1, column=0, columnspan=3, pady=10)

        self.ventana.mainloop()
