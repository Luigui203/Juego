from Model.ConexionDB import ConexionDB
import tkinter as tk
from tkinter import messagebox as mb
import datetime

class Usuario():
    """
    Clase que representa a un usuario del juego.
    Permite gestionar las acciones de inicio de sesión, creación de usuario, 
    y el manejo de puntajes (guardar y consultar).

    Atributos:
        nombre: Nombre del usuario.
        correo: Correo electrónico del usuario.
        clave: Contraseña del usuario.
    """

    def __init__(self):
        """
        Inicializa un objeto Usuario.
        """
        self.nombre = None
        self.correo = None
        self.clave = None

    def iniciarSesion(self, nombreUsuario, password, loggin):
        """
        Permite iniciar sesión en el sistema con un nombre de usuario y una contraseña.
        
        :param nombreUsuario: Nombre del usuario para iniciar sesión.
        :param password: Contraseña del usuario.
        :param loggin: El objeto o función encargada de gestionar la interfaz de inicio de sesión.
        :return: True si las credenciales son correctas, False si no lo son.
        """
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM jugador WHERE nombre = %s AND clave = %s", (nombreUsuario, password))
            usuario = cursor.fetchone()

            if usuario:
                self.nombre = usuario[1]
                self.correo = usuario[2]
                self.clave = usuario[3]
                mb.showinfo("Información", "¡Acceso concedido!")
                return True
            else:
                mb.showerror("Error", "Usuario o contraseña incorrectos")
                return False
        except Exception as e:
            mb.showerror("Error", f"Error al iniciar sesión: {e}")
            return False
        finally:
            cursor.close()
            con.close()


    def guardarPuntaje(self, nombreUsuario, puntaje):
        """
        Guarda o actualiza el puntaje del usuario en la base de datos.
        Si el nuevo puntaje es mayor que el anterior, se actualiza la fecha y el puntaje.

        :param nombreUsuario: Nombre del usuario para el cual se va a guardar el puntaje.
        :param puntaje: Puntaje obtenido por el usuario.
        """
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()

        try:
            # Obtener el id del jugador
            cursor.execute("SELECT id FROM jugador WHERE nombre = %s", (nombreUsuario,))
            jugador = cursor.fetchone()

            if jugador:
                id_jugador = jugador[0]
                # Obtener el puntaje actual del jugador
                cursor.execute("SELECT puntaje FROM puntuaciones WHERE id_jugador = %s", (id_jugador,))
                puntaje_actual = cursor.fetchone()

                if puntaje_actual:
                    puntaje_actual = puntaje_actual[0]
                    # Verificar si el nuevo puntaje es mayor
                    if puntaje > puntaje_actual:
                        fecha_actual = datetime.datetime.now()  # Fecha y hora actuales
                        cursor.execute(
                            "UPDATE puntuaciones SET puntaje = %s, fecha = %s WHERE id_jugador = %s",
                            (puntaje, fecha_actual, id_jugador)
                        )
                        con.commit()  # Confirmar cambios
                        print(f"Puntaje y fecha actualizados para {nombreUsuario}: {puntaje}, Fecha: {fecha_actual}")
                    else:
                        print(f"El puntaje {puntaje} no supera el puntaje actual de {puntaje_actual}. No se actualizó.")
                else:
                    # Si no hay puntaje previo, se inserta uno nuevo con la fecha actual
                    fecha_actual = datetime.datetime.now()  # Fecha y hora actuales.
                    cursor.execute(
                        "INSERT INTO puntuaciones (id_jugador, puntaje, fecha) VALUES (%s, %s, %s)",
                        (id_jugador, puntaje, fecha_actual)
                    )
                    con.commit()
                    print(f"Primer puntaje registrado para {nombreUsuario}: {puntaje}, Fecha: {fecha_actual}")
            else:
                print(f"Jugador con nombre {nombreUsuario} no encontrado")
        except Exception as e:
            print(f"Error al guardar el puntaje: {e}")
        finally:
            cursor.close()
            con.close()


    def crearUsuario(self, nombreUsuario, correo, password):
        """
        Crea un nuevo usuario en la base de datos si no existe. Verifica que el correo y 
        el nombre de usuario no estén en uso antes de proceder.

        :param nombreUsuario: Nombre del usuario.
        :param correo: Correo electrónico del usuario.
        :param password: Contraseña del usuario.
        :return: Mensaje indicando el resultado de la operación.
        """
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()

        try:
            # Verificar si el correo ya existe
            cursor.execute("SELECT * FROM jugador WHERE correo = %s", (correo,))
            correo_existente = cursor.fetchone()

            if correo_existente:
                return f"El correo '{correo}' ya está asociado a otro usuario."

            # Verificar si el nombre de usuario ya existe
            cursor.execute("SELECT * FROM jugador WHERE nombre = %s", (nombreUsuario,))
            usuario_existente = cursor.fetchone()

            if usuario_existente:
                return f"El nombre de usuario '{nombreUsuario}' ya está en uso. Por favor, elige otro."

            # Insertar el nuevo usuario
            cursor.execute(
                "INSERT INTO jugador (nombre, correo, clave) VALUES (%s, %s, %s)",
                (nombreUsuario, correo, password)  
            )
            con.commit()
            return f"Usuario '{nombreUsuario}' creado exitosamente."
        except Exception as e:
            return f"Error al crear el usuario: {e}"
        finally:
            cursor.close()
            con.close()

    def consultarRanking(self):
        """
        Recupera el ranking de los jugadores, ordenado por el puntaje.
        
        :return: Lista de jugadores con sus puntajes, ordenada de mayor a menor puntaje.
        """
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()

        try:
            cursor.execute("""
                SELECT jugador.nombre, puntuaciones.puntaje
                FROM jugador
                JOIN puntuaciones ON jugador.id = puntuaciones.id_jugador
                ORDER BY puntuaciones.puntaje DESC
            """)
            ranking = cursor.fetchall()
            return ranking
        except mariadb.OperationalError as e:
            print(f"Error al conectar a la base de datos: {e}")
            # Mostrar un mensaje de error en la ventana del ranking
            mb.showerror("Error de conexión", "No se pudo conectar a la base de datos. Verifica que el servidor esté en ejecución.")
            return []
        except Exception as e:
            print(f"Error al consultar el ranking: {e}")
            return []
        finally:
            cursor.close()
            con.close()
