from typing import Type

from .utils import to_camel_case
from .connection import Connection
from .cursor import Cursor

DEFAULT_THREADSAFETY = 1
DEFAULT_PARAMSTYLE = 'format'


class DataSourceAPI(object):
    '''A new data source interface instance.

    *If you need to check which values are available for each of the PEP-249
    parameters, please refer to https://www.python.org/dev/peps/pep-0249/*

    :param name: The name to your new data source API
    :type name: str
    :param connection_class: A custom :class:`~.data_source_api.Connection`.
    This class will be used for connection instantiation and, if not provided,
    a new class, child of :class:`~.data_source_api.Connection`, with name
    `<name of API in camel case>Connection` will be defined and used instead.
    :type connection_class: Type[Connection]
    :param cursor_class: A custom :class:`~.data_source_api.Cursor`. This class
    will be used for query executions and, if not provided, a new class, child
    of :class:`~.data_source_api.Cursor`, with name
    `<name of API in camel case>Connection` will be defined and used instead.
    :type cursor_class: Type[Cursor]
    :param threadsafety: The level of thread safety the interface supports. De-
    faults to 1
    :type threadsafety: int, optional
    :param paramstyle: The type of parameter marker formatting expected. De-
    faults to `format`
    :type paramstyle: str, optional
    '''

    name: str
    apilevel: str = '2.0'
    threadsafety: int
    paramstyle: str
    connection_class: Type[Connection]
    cursor_class: Type[Cursor]

    def __init__(
        self: 'DataSourceAPI',
        name: str,
        *,
        connection_class: Type[Connection] = None,
        cursor_class: Type[Cursor] = None,
        threadsafety: str = DEFAULT_THREADSAFETY,
        paramstyle: str = DEFAULT_PARAMSTYLE,

    ) -> None:
        self.name = name
        self.threadsafety = threadsafety
        self.paramstyle = paramstyle
        self.connection_class = connection_class or type(
            to_camel_case(self.name) + 'Connection', (Connection, ), {}
        )
        self.cursor_class = cursor_class or type(
            to_camel_case(self.name) + 'Cursor', (Cursor, ), {}
        )

    def connect(
        self: 'DataSourceAPI',
        *args, **kwargs
    ) -> Connection:
        '''Return a new connection.

        :return: A new connection object
        :rtype: Connection
        '''
        return self.connection_class(self, *args, **kwargs)
