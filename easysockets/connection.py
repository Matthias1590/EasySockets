from __future__ import annotations
import socket
from typing import Any, Callable


MESSAGE_SIZE_BYTES = 8


def connection_closed_error(message: str) -> Callable:
    """
    Decorator to raise an error if the connection is closed.
    """

    def decorator(func: Callable) -> Callable:
        def wrapper(connection: Connection, *args, **kwargs) -> Any:
            if connection.is_closed:
                raise ConnectionClosedError(message)

            return func(connection, *args, **kwargs)

        return wrapper

    return decorator


class ConnectionClosedError(Exception):
    pass


class Connection:
    def __init__(self, socket: socket.socket) -> None:
        self.__socket = socket
        self.__is_closed = False

    @property
    def is_closed(self) -> bool:
        return self.__is_closed

    @connection_closed_error("Cannot send data through closed connection")
    def send(self, data: bytes) -> None:
        data_size = len(data).to_bytes(MESSAGE_SIZE_BYTES, byteorder="big")

        self.__socket.send(data_size)
        self.__socket.send(data)

    @connection_closed_error("Cannot receive data through closed connection")
    def receive(self) -> bytes:
        data_size = self.__socket.recv(MESSAGE_SIZE_BYTES)

        if not data_size:
            return None

        data_size = int.from_bytes(data_size, byteorder="big")

        data = b""
        while len(data) < data_size:
            block_size = min(data_size, 4096)

            data += self.__socket.recv(block_size)

        return data

    @connection_closed_error("Cannot close closed connection")
    def close(self) -> None:
        self.__socket.close()
        self.__is_closed = True
