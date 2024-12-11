from Model.ConexionDB import ConexionDB
import tkinter as tk
from tkinter import messagebox as mb

class Usuario():
    def __init__(self):
        self.nombre = None
        self.correo = None
        self.clave = None

    def iniciarSesion(self, nombreUsuario, password, loggin):
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
                        cursor.execute(
                            "UPDATE puntuaciones SET puntaje = %s WHERE id_jugador = %s",
                            (puntaje, id_jugador)
                        )
                        con.commit()  # Confirmar cambios
                        print(f"Puntaje actualizado para {nombreUsuario}: {puntaje}")
                    else:
                        print(f"El puntaje {puntaje} no supera el puntaje actual de {puntaje_actual}. No se actualizó.")
                else:
                    # Si no hay puntaje previo, se inserta uno nuevo
                    cursor.execute(
                        "INSERT INTO puntuaciones (id_jugador, puntaje) VALUES (%s, %s)",
                        (id_jugador, puntaje)
                    )
                    con.commit()
                    print(f"Primer puntaje registrado para {nombreUsuario}: {puntaje}")
            else:
                print(f"Jugador con nombre {nombreUsuario} no encontrado")
        except Exception as e:
            print(f"Error al guardar el puntaje: {e}")
        finally:
            cursor.close()
            con.close()

    def crearUsuario(self, nombreUsuario, correo, password):
        """
        Crea un nuevo usuario en la base de datos si no existe.
        
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
                (nombreUsuario, correo, password)  # Recuerda que la clave debe estar encriptada
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
        :return: Lista de jugadores con sus puntajes.
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
        except Exception as e:
            print(f"Error al consultar el ranking: {e}")
            return []
        finally:
            cursor.close()
            con.close()

