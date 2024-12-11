import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound
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
        else:
            self.txtUsuario.config(bg="#f5b7b1", fg="#e74c3c")
            winsound.Beep(1700, 333)

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
        self.ventana.config(width=440, height=350)
        self.ventana.title("Inicio de Sesión")
        self.inicio_exitoso = False  # Bandera para verificar inicio de sesión exitoso

        self.bandera = False
        self.caracteresUsuario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.']
        self.caracteresPassword = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.lblTitulo = tk.Label(self.ventana, text="Inicio Sesión")
        self.lblTitulo.place(relx=0.5, y=50, anchor="center")

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*: ")
        self.lblUsuario.place(x=100, y=125, width=70, height=25)

        self.lblPassword = tk.Label(self.ventana, text="Password*: ")
        self.lblPassword.place(x=100, y=200, width=70, height=25)

        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(x=190, y=125, width=150, height=25)
        self.txtUsuario.bind("<KeyRelease>", self.validarCampos)
        self.txtUsuario.bind("<Key>", self.validarUsuario)
        Tooltip(self.txtUsuario, "Ingrese su nombre de Ususrio, solo letras minúsculas.\nmin 5 caracteres, max 25 caracteres")

        self.txtPassword = tk.Entry(self.ventana, show="*")
        self.txtPassword.place(x=190, y=200, width=150, height=25)
        self.txtPassword.bind("<KeyRelease>", self.validarCampos)

        self.btnAyuda = tk.Button(self.ventana, text="Ayuda")
        self.btnAyuda.place(x=320, y=50)

        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", state="disabled")
        self.btnIngresar.place(x=140, y=275, width=70, height=25)
        self.btnIngresar.bind("<Button-1>", self.ingresar)

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", command=self.limpiarCampos)
        self.btnLimpiar.place(x=230, y=275, width=70, height=25)

        self.btnVer = tk.Button(self.ventana, text="Ver")
        self.btnVer.place(x=360, y=200, width=30, height=25)
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)

        self.btnRegistrar = tk.Button(self.ventana, text="Registrarse", command=self.abrir_ventana_registro)
        self.btnRegistrar.place(x=320, y=275, width=70, height=25)

        # Botón de Consultar Ranking
        self.btnRanking = tk.Button(self.ventana, text="Consultar Ranking", command=self.consultarRanking)
        self.btnRanking.place(x=140, y=225, width=150, height=25)

        self.ventana.mainloop()

