import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # Para redimensionar imágenes
import subprocess  # Para ejecutar el juego
from Controller.Usuario import Usuario
from Tooltip import Tooltip
from View.Registrar import Registrar
from View.Consultar import ConsultarRanking


class Loggin:
    def consultarRanking(self, event):
        # Llamar a la ventana del ranking
        ranking_ventana = ConsultarRanking()

    def validarCampos(self, event):
        if len(self.txtUsuario.get()) >= 5 and len(self.txtPassword.get()) >= 5:
            if len(self.txtUsuario.get()) <= 25 and len(self.txtPassword.get()) <= 25:
                self.btnIngresar.config(state="normal")
            elif len(self.txtUsuario.get()) <= 25 and len(self.txtPassword.get()) >= 25:
                self.txtPassword.delete(len(self.txtPassword.get()) - 1, tk.END)
            elif len(self.txtUsuario.get()) >= 25 and len(self.txtPassword.get()) <= 25:
                self.txtUsuario.delete(len(self.txtUsuario.get()) - 1, tk.END)
        else:
            self.btnIngresar.config(state="disabled")

    def validarUsuario(self, event):
        caracter = event.keysym
        if caracter.isalpha() or caracter == '.' or caracter == "BackSpace":
            self.txtUsuario.config(bg="#ffffff", fg="#000000")

    def verCaracteres(self, event):
        if self.bandera:
            self.txtPassword.config(show='*')
            self.btnVer.config(text="Ver")
            self.bandera = False
        else:
            self.txtPassword.config(show='')
            self.btnVer.config(text="Ocultar")
            self.bandera = True

    def ingresar(self, event=None):
        miUsuario = Usuario()
        usuario = self.txtUsuario.get()
        if miUsuario.iniciarSesion(usuario, self.txtPassword.get(), self.ventana):
            self.ventana.destroy()
            self.iniciar_juego(usuario)

    def iniciar_juego(self, nombreUsuario):
        subprocess.run(["python", "juego.py", nombreUsuario])

    def abrir_ventana_registro(self, event):
        self.ventana.destroy()
        registrar_ventana = Registrar()
        registrar_ventana.ventana.mainloop()

    def limpiarCampos(self, event=None):
        self.txtUsuario.delete(0, tk.END)
        self.txtPassword.delete(0, tk.END)

    def enter_pressed(self, event):
        if self.txtUsuario.get() and self.txtPassword.get():
            self.ingresar(event)

    def __init__(self):
        def cargar_icono(ruta, ancho, alto):
            """Función para cargar y redimensionar iconos."""
            imagen = Image.open(ruta)
            imagen = imagen.resize((ancho, alto), Image.LANCZOS)
            return ImageTk.PhotoImage(imagen)

        self.ventana = tk.Tk()
        self.ventana.resizable(0, 0)
        self.ventana.config(width=500, height=400)
        self.ventana.title("Inicio de Sesión")
        self.ventana.iconbitmap(r"iconos/valle.ico")
        self.inicio_exitoso = False
        self.bandera = False

        # Cargar y redimensionar iconos
        self.icono_entrar = cargar_icono("imagenes/entrar.png", 20, 20)
        self.icono_limpiar = cargar_icono("imagenes/limpiar.png", 20, 20)
        self.icono_registrar = cargar_icono("imagenes/registrar.png", 20, 20)

        # Estilos personalizados para botones
        style = ttk.Style()
        style.configure("Custom.TButton",
                        font=("Helvetica", 10, "bold"),
                        padding=(10, 6),
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
        Tooltip(self.txtUsuario, "Ingrese su nombre de Usuario.\nmin 5 caracteres.")

        # Contraseña
        self.lblPassword = tk.Label(frame_inputs, text="Password*: ", font=("Helvetica", 10))
        self.lblPassword.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.txtPassword = tk.Entry(frame_inputs, show="*", width=25)
        self.txtPassword.grid(row=1, column=1, padx=10, pady=10)
        self.txtPassword.bind("<KeyRelease>", self.validarCampos)
        self.txtPassword.bind("<Return>", self.ingresar)
        Tooltip(self.txtPassword, "Ingrese su contraseña, debe tener al menos 5 caracteres.")

        # Botón Ver Contraseña
        self.btnVer = ttk.Button(frame_inputs, text="Ver", style="Custom.TButton")
        self.btnVer.grid(row=1, column=2, padx=5, pady=10)
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)

        # Marco para botones
        frame_buttons = ttk.Frame(self.ventana, padding="10")
        frame_buttons.place(relx=0.5, rely=0.75, anchor="center")

        # Botones principales con iconos
        self.btnIngresar = ttk.Button(frame_buttons, text="Ingresar", image=self.icono_entrar, compound="left", style="Custom.TButton")
        self.btnIngresar.grid(row=0, column=0, padx=10, pady=10)
        self.btnIngresar.bind("<Button-1>", self.ingresar)
        Tooltip(self.btnIngresar, "Haz clic para iniciar sesión")

        self.btnLimpiar = ttk.Button(frame_buttons, text="Limpiar", image=self.icono_limpiar, compound="left", style="Custom.TButton")
        self.btnLimpiar.grid(row=0, column=1, padx=10, pady=10)
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Limpiar campos de usuario y contraseña")

        self.btnRegistrar = ttk.Button(frame_buttons, text="Registrarse", image=self.icono_registrar, compound="left", style="Custom.TButton")
        self.btnRegistrar.grid(row=0, column=2, padx=10, pady=10)
        self.btnRegistrar.bind("<Button-1>", self.abrir_ventana_registro)
        Tooltip(self.btnRegistrar, "Registrarse como nuevo usuario")

        self.btnRanking = ttk.Button(frame_buttons, text="Consultar Ranking", style="Custom.TButton")
        self.btnRanking.grid(row=1, column=0, columnspan=3, pady=10)
        self.btnRanking.bind("<Button-1>", self.consultarRanking)
        Tooltip(self.btnRanking, "Consultar ranking de usuarios")

        # Vincular Enter para toda la ventana
        self.ventana.bind("<Return>", self.enter_pressed)

        self.ventana.mainloop()
