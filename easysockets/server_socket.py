from typing import Any, Callable
from .connection import Connection
import socket
import threading


def close_connection(func: Callable) -> Callable:
    """
    Wrapper for functions that need to close the connection after the function is done.
    """

    def wrapper(connection: Connection) -> Any:
        try:
            result = func(connection)
        finally:
            if not connection.is_closed:
                connection.close()

        return result

    return wrapper


class ServerSocket:
    def __init__(self, client_handler: Callable) -> None:
        super().__init__()

        self.__client_handler = close_connection(client_handler)

        # TCP socket
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__threads = []

    def listen(self, host: str, port: int) -> None:
        self.__socket.bind((host, port))
        self.__socket.listen()

        while True:
            client, _ = self.__socket.accept()
            connection = Connection(client)

            # Start a new thread for each client
            thread = threading.Thread(
                target=self.__client_handler,
                args=(connection,),
            )

            self.__threads.append(thread)

            thread.start()
