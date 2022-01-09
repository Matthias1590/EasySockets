from .connection import Connection
import socket


class ClientSocket:
    def __init__(self) -> None:
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host: str, port: int) -> Connection:
        self.__socket.connect((host, port))

        return Connection(self.__socket)
