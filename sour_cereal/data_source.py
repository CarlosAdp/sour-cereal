from typing import Type

from .utils import to_camel_case
from .utils.mixins import OpenCloseMixin

DEFAULT_THREADSAFETY = 1
DEFAULT_PARAMSTYLE = 'format'


class Connection(OpenCloseMixin):
    '''A connection instance a data source.

    It's open on instantiation.
    '''
    def __init__(self: 'Connection'):
        super().open()

    def foo(self):
        print("AAA")


class DataSourceAPI(object):
    '''A new data source interface instance.

    *If you need to check which values are permitted for PEP-249 parameters,
    refer to https://www.python.org/dev/peps/pep-0249/*

    :param name: The name to your new data source API
    :type name: str
    :param connection_class: A custom :class:`~.data_source_api.Connection`.
    This class will be used for connection instantiation and, if not provided,
    a new class, child of :class:`~.data_source_api.Connection`, with name
    `<name of API in camel case>Connection` will be defined and used instead.
    :type connection_class: Type[Connection]
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

    def __init__(
        self: 'DataSourceAPI',
        name: str,
        *,
        connection_class: Type[Connection] = None,
        threadsafety: str = DEFAULT_THREADSAFETY,
        paramstyle: str = DEFAULT_PARAMSTYLE,

    ) -> None:
        self.name = name
        self.threadsafety = threadsafety
        self.paramstyle = paramstyle
        self.connection_class = connection_class or type(
            to_camel_case(self.name) + 'Connection', (Connection, ), {}
        )

    def connect(
        self: 'DataSourceAPI',
        *args, **kwargs
    ) -> Connection:
        return self.connection_class(self, *args, **kwargs)
