from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Sequence, Type


class DataSourceInterface(metaclass=ABCMeta):
    '''Define an abstract interface for a data source object'''
    name: str
    connection_method: Callable
    apilevel: str = "2.0"
    threadsafety: int = 1
    paramstyle: str = 'format'
    connection_class: Type['ConnectionInterface']
    cursor_class: Type['CursorInterface']

    @abstractmethod
    def __init__(
        self: 'DataSourceInterface',
        name: str,
        connection_class: Type['ConnectionInterface'] = None,
        cursor_class: Type['CursorInterface'] = None,
        threadsafety: int = 1,
        paramstyle: str = 'format',
    ) -> None: pass

    @abstractmethod
    def connect(
        self: 'DataSourceInterface',
        *args, **kwargs
    ) -> 'ConnectionInterface': pass

    @abstractmethod
    def register_connection_method(
        self: 'DataSourceInterface',
        method: Callable
    ) -> Callable: pass


class ConnectionInterface(metaclass=ABCMeta):
    '''Define an abstract interface for a connection object'''
    @abstractmethod
    def __init__(self: 'ConnectionInterface', *args, **kwargs) -> None: pass

    @abstractmethod
    def close(self: 'ConnectionInterface', *args, **kwargs) -> Any: pass

    @abstractmethod
    def commit(self: 'ConnectionInterface', *args, **kwargs) -> Any: pass

    @abstractmethod
    def rollback(self: 'ConnectionInterface', *args, **kwargs) -> Any: pass

    @abstractmethod
    def cursor(
        self: 'ConnectionInterface',
        *args, **kwargs
    ) -> 'CursorInterface': pass


class CursorInterface(metaclass=ABCMeta):
    '''Define an abstract interface for a cursor object'''

    _description: Sequence[Sequence[Any]]
    _rowcount: int

    @abstractmethod
    def __init__(self: 'CursorInterface', *args, **kwargs) -> None: pass

    @abstractmethod
    def callproc(self: 'CursorInterface', *args, **kwargs) -> None: pass

    @abstractmethod
    def close(self: 'CursorInterface', *args, **kwargs) -> None: pass
