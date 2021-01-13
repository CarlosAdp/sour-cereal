from typing import Any, Callable, Dict, Tuple, Type

from .utils import to_camel_case


class Cursor(object):
    connection: 'Connection'

    def __init__(
        self: 'Cursor',
        connection: 'Connection',
        *args, **kwargs
    ) -> None:
        self.connection = connection


class Connection(object):
    data_source: 'DataSource'
    client: Any
    closed: bool

    def __init__(
        self: 'Connection',
        data_source: 'DataSource',
        *args, **kwargs
    ) -> None:
        self.data_source = data_source
        self.closed = False

    def close(self: 'Connection') -> None:
        self.closed = True

    def cursor(self: 'Connection', *args, **kwargs) -> Cursor:
        return Cursor(connection=self, *args, **kwargs)


class DataSource(object):
    name: str
    connection_method: Callable
    apilevel: str = "2.0"
    threadsafety: int = 1
    paramstyle: str = 'format'
    connection_class: Type['Connection']
    cursor_class: Type['Cursor']

    def __init__(
        self: 'DataSource',
        name: str,
        connection_class: Type['Connection'] = None,
        cursor_class: Type['Cursor'] = None,
        threadsafety: int = 1,
        paramstyle: str = 'format',
    ) -> None:
        self.name = name
        self.connection_class = connection_class or type(
            to_camel_case(name) + 'Connection', (Connection, ), {}
        )
        self.cursor_class = cursor_class or type(
            to_camel_case(name) + 'Cursor', (Cursor, ), {}
        )
        self.threadsafety = threadsafety
        self.paramstyle = paramstyle

        self.connection_method = None

    def connect(self: 'DataSource', *args, **kwargs) -> Connection:
        creation_method = self.connection_method or self.connection_class

        return creation_method(self, *args, **kwargs)

    def register_connection_method(
        self: 'DataSource',
        method: Callable
    ) -> Callable:
        self.connection_method = method

        return method


register_connection_method = DataSource.register_connection_method
