import mariadb as sql

class ConexionDB():
    def __init__(self):
        self.__host = "127.0.0.1" #Cambia si el servidor está en un host remoto.
        self.__user = "root" #Cambia si el usuario es diferente.
        self.__password = ""
        self.__port = 3306
        self.__database = "juegos"
        self.__conection = None

    def crearConexion(self):
        self.__conection  = sql.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            port = self.__port,
            database = self.__database
        ) 

    def cerrarConexion(self):
        if self.__conection:
            self.__conection.close()
            self.__conection = None

    def getConection(self):
        return self.__conection

    def getHost(self):
        return self.__host

    def getUser(self):
        return self.__user

    def getPassword(self):
        return self.__password

    def getPort(self):
        return self.__port

    def getDatabase(self):
        return self.__database
