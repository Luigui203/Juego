import tkinter as tk
from tkinter import messagebox
from Controller.Usuario import Usuario

class Registrar:
    """
    Clase que representa la ventana de registro de un nuevo usuario en la aplicación.

    A través de esta ventana, el usuario puede ingresar su nombre de usuario, correo electrónico y contraseña
    para registrarse en el sistema. Si la validación es exitosa, los datos se procesan y el usuario es creado.
    Si no, se muestran mensajes de error indicando qué campo debe corregir.
    """

    def __init__(self):
        """
        Inicializa la ventana de registro y los elementos de la interfaz gráfica.

        Se crean los campos de entrada de datos (Usuario, Correo, Contraseña), los botones
        de 'Registrar' y 'Volver', y la etiqueta de título.
        """
        self.ventana = tk.Tk()  # Crea la ventana principal
        self.ventana.resizable(0, 0)  # Desactiva el redimensionamiento
        self.ventana.config(width=440, height=350)  # Establece el tamaño de la ventana
        self.ventana.title("Registrar Usuario")  # Título de la ventana
        self.ventana.iconbitmap(r"iconos\valle.ico")

        # Crear campos de entrada de datos
        self.lblTitulo = tk.Label(self.ventana, text="Registrar Nuevo Usuario")
        self.lblTitulo.place(relx=0.5, y=50, anchor="center")

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*: ")
        self.lblUsuario.place(x=100, y=125, width=70, height=25)

        self.lblCorreo = tk.Label(self.ventana, text="Correo*: ")
        self.lblCorreo.place(x=100, y=160, width=70, height=25)

        self.lblPassword = tk.Label(self.ventana, text="Password*: ")
        self.lblPassword.place(x=100, y=200, width=70, height=25)

        self.txtUsuario = tk.Entry(self.ventana)  # Campo de texto para el nombre de usuario
        self.txtUsuario.place(x=190, y=125, width=150, height=25)

        self.txtCorreo = tk.Entry(self.ventana)  # Campo de texto para el correo
        self.txtCorreo.place(x=190, y=160, width=150, height=25)

        self.txtPassword = tk.Entry(self.ventana, show="*")  # Campo de texto para la contraseña
        self.txtPassword.place(x=190, y=200, width=150, height=25)

        # Botones de acción
        self.btnRegistrar = tk.Button(self.ventana, text="Registrar", command=self.registrar_usuario)
        self.btnRegistrar.place(x=140, y=275, width=70, height=25)

        self.btnVolver = tk.Button(self.ventana, text="Volver", command=self.volver_login)
        self.btnVolver.place(x=230, y=275, width=70, height=25)

        self.ventana.bind("<Return>", self.enter_pressed)


    def registrar_usuario(self, event=None):
        """
        Función que se ejecuta al hacer clic en el botón de "Registrar".

        Obtiene los datos ingresados por el usuario, valida que todos los campos estén completos
        y que el correo sea válido. Si todo es correcto, llama al método de la clase `Usuario` 
        para crear un nuevo usuario. Si ocurre un error, se muestra un mensaje de error.
        """
        nombre = self.txtUsuario.get()  # Obtiene el nombre de usuario del campo
        correo = self.txtCorreo.get()  # Obtiene el correo electrónico
        password = self.txtPassword.get()  # Obtiene la contraseña

        # Verifica que los campos no estén vacíos
        if not nombre or not correo or not password:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Verifica que el nombre de usuario y la contraseña tengan al menos 5 caracteres
        if len(nombre) < 5:
            messagebox.showerror("Error", "El nombre de usuario debe tener al menos 5 caracteres.")
            return
        if len(password) < 5:
            messagebox.showerror("Error", "La contraseña debe tener al menos 5 caracteres.")
            return

        # Verifica si el correo tiene un formato válido
        if "@" not in correo or "." not in correo:
            messagebox.showerror("Error", "El correo no es válido.")
            return

        # Crea una instancia de la clase Usuario y registra el nuevo usuario
        miUsuario = Usuario()
        resultado = miUsuario.crearUsuario(nombre, correo, password)  # Llama a la función para crear usuario

        # Si la creación del usuario fue exitosa, muestra un mensaje y cierra la ventana de registro
        if "exitosamente" in resultado:
            messagebox.showinfo("Éxito", resultado)  # Muestra mensaje de éxito
            self.ventana.destroy()  # Cierra la ventana actual
            from View.Loggin import Loggin  # Importa la clase de login
            login = Loggin()  # Crea una nueva ventana de login
            login.ventana.mainloop()  # Inicia el mainloop de la ventana de login
        else:
            # Si ocurre un error durante la creación del usuario, muestra un mensaje de error
            messagebox.showerror("Error", resultado)

    def enter_pressed(self, event):
        if self.txtUsuario.get() and self.txtCorreo.get() and self.txtPassword.get():  # Si los campos están llenos
            self.registrar_usuario(event)

    def volver_login(self):
        """
        Función que se ejecuta al hacer clic en el botón "Volver".

        Cierra la ventana de registro y abre la ventana de inicio de sesión.
        """
        self.ventana.destroy()  # Cierra la ventana de registro
        from View.Loggin import Loggin  # Importa la clase de login
        login = Loggin()  # Crea una nueva ventana de login
        login.ventana.mainloop()  # Inicia el mainloop de la ventana de login
