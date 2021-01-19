from contextlib import suppress

from open_close_mixin import OpenCloseMixin

from .cursor import Cursor
from .exceptions import NotSupportedError, ProgrammingError


class Connection(OpenCloseMixin):
    '''A connection instance to a data source.

    It's open on instantiation.

    :param api: The data source API used to instantiate the connection
    :type api: :class:`~.DataSourceAPI`
    '''
    api: 'DataSourceAPI'

    not_open_exception = ProgrammingError(
        'The connection is not open. "{method_name}" cannot be executed'
    )

    not_closed_exception = ProgrammingError(
        'The connection is not closed. "{method_name}" cannot be executed'
    )

    def __init__(self: 'Connection', api: 'DataSourceAPI'):
        '''Please refer to this class documentation.'''
        super().__init__()
        self.api = api
        self.open()

    def close(self: 'Connection') -> None:
        '''Close the connection.'''
        with suppress(NotSupportedError):
            self.rollback()
        super().close()

    def commit(self: 'Connection') -> None:
        '''Placeholder method for commit.

        Raises exception for not being implemented yet.

        :raise: NotSupportedError
        '''
        raise NotSupportedError

    def rollback(self: 'Connection') -> None:
        '''Placeholder method for rollback.

        Raises exception for not being implemented yet.

        :raise: NotSupportedError
        '''
        raise NotSupportedError

    def cursor(self: 'Connection', *args, **kwargs) -> 'Cursor':
        '''Get a cursor.

        :return: A cursor
        :rtype: Cursor
        '''
        return self.api.cursor_class(self, *args, **kwargs)
