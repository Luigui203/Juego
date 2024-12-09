import tkinter as tk
from tkinter import messagebox
from Controller.Usuario import Usuario

class Registrar:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0, 0)
        self.ventana.config(width=440, height=350)
        self.ventana.title("Registrar Usuario")

        # Crear campos
        self.lblTitulo = tk.Label(self.ventana, text="Registrar Nuevo Usuario")
        self.lblTitulo.place(relx=0.5, y=50, anchor="center")

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*: ")
        self.lblUsuario.place(x=100, y=125, width=70, height=25)

        self.lblCorreo = tk.Label(self.ventana, text="Correo*: ")
        self.lblCorreo.place(x=100, y=160, width=70, height=25)

        self.lblPassword = tk.Label(self.ventana, text="Password*: ")
        self.lblPassword.place(x=100, y=200, width=70, height=25)

        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(x=190, y=125, width=150, height=25)

        self.txtCorreo = tk.Entry(self.ventana)
        self.txtCorreo.place(x=190, y=160, width=150, height=25)

        self.txtPassword = tk.Entry(self.ventana, show="*")
        self.txtPassword.place(x=190, y=200, width=150, height=25)

        # Botones
        self.btnRegistrar = tk.Button(self.ventana, text="Registrar", command=self.registrar_usuario)
        self.btnRegistrar.place(x=140, y=275, width=70, height=25)

        self.btnVolver = tk.Button(self.ventana, text="Volver", command=self.volver_login)
        self.btnVolver.place(x=230, y=275, width=70, height=25)

    def registrar_usuario(self):
        nombre = self.txtUsuario.get()
        correo = self.txtCorreo.get()
        password = self.txtPassword.get()

        if not nombre or not correo or not password:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        
        if "@" not in correo or "." not in correo:
            messagebox.showerror("Error", "El correo no es válido.")
            return
        
        miUsuario = Usuario()
        resultado = miUsuario.crearUsuario(nombre, correo, password)

        if "exitosamente" in resultado:
            messagebox.showinfo("Éxito", resultado)
            self.ventana.destroy()  # Cerrar la ventana de registro
            from View.Loggin import Loggin  # Importa Loggin para volver a la ventana de login
            login = Loggin()  # Crear nueva instancia de Loggin
            login.ventana.mainloop()  # Ejecutar el mainloop de la nueva ventana de login
        else:
            messagebox.showerror("Error", resultado)

    def volver_login(self):
        self.ventana.destroy()
        from View.Loggin import Loggin
        login = Loggin()
        login.ventana.mainloop()
