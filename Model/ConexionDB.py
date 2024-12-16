import mariadb as sql

class ConexionDB():
    """
    Clase para gestionar la conexión con la base de datos MariaDB.
    Proporciona métodos para crear, cerrar y obtener la conexión, 
    así como para obtener las configuraciones de la conexión (host, usuario, etc.).

    Atributos:
        __host: Dirección del servidor de base de datos (localhost por defecto).
        __user: Usuario para la conexión (root por defecto).
        __password: Contraseña del usuario (vacío por defecto).
        __port: Puerto de conexión a la base de datos (3306 por defecto).
        __database: Nombre de la base de datos a la que conectarse (juegos por defecto).
        __conection: Instancia de la conexión a la base de datos.
    """

    def __init__(self):
        """
        Inicializa la clase con la configuración predeterminada para la conexión a la base de datos.
        """
        self.__host = "127.0.0.1"  # Cambia si el servidor está en un host remoto.
        self.__user = "root"  # Cambia si el usuario es diferente.
        self.__password = ""
        self.__port = 3306
        self.__database = "juegos"
        self.__conection = None

    def crearConexion(self):
        """
        Crea una conexión a la base de datos utilizando la configuración proporcionada.
        
        :raises mariadb.Error: Si ocurre un error al establecer la conexión.
        """
        try:
            self.__conection = sql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                port=self.__port,
                database=self.__database
            )
        except sql.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise

    def cerrarConexion(self):
        """
        Cierra la conexión a la base de datos si está abierta.
        """
        if self.__conection:
            self.__conection.close()
            self.__conection = None

    def getConection(self):
        """
        Devuelve la conexión a la base de datos.
        
        :return: Conexión a la base de datos.
        """
        return self.__conection

    def getHost(self):
        """
        Devuelve la dirección del host de la base de datos.

        :return: Dirección del host.
        """
        return self.__host

    def getUser(self):
        """
        Devuelve el nombre de usuario utilizado para la conexión.

        :return: Nombre de usuario.
        """
        return self.__user

    def getPassword(self):
        """
        Devuelve la contraseña utilizada para la conexión.

        :return: Contraseña.
        """
        return self.__password

    def getPort(self):
        """
        Devuelve el puerto utilizado para la conexión.

        :return: Puerto de conexión.
        """
        return self.__port

    def getDatabase(self):
        """
        Devuelve el nombre de la base de datos a la que se conecta.

        :return: Nombre de la base de datos.
        """
        return self.__database
