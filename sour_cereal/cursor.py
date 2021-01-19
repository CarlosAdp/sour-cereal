from typing import Any, Tuple

from open_close_mixin import OpenCloseMixin

from .exceptions import NotSupportedError


class Cursor(OpenCloseMixin):
    '''A cursor open by a connection.

    It's open on instantiation.

    :param connection: The connection that opened the cursor
    :type connection: :class:`~.Connection`
    '''
    connection: 'Connection'
    _description: Tuple[Tuple[str, ...], ...]
    _rowcount: int

    def __init__(self: 'Cursor', connection: 'Connection') -> None:
        super().__init__()
        self.connection = connection
        self._description = None
        self._rowcount = None

        self.open()

    @property
    def description(self: 'Cursor') -> Tuple[Tuple[str, ...], ...]:
        '''Returns a read-only description of columns.

        :return: a description of the result set of the cursor
        :rtype: Tuple[Tuple[str, ...], ...]
        '''
        return self._description

    @property
    def rowcount(self: 'Cursor') -> int:
        '''Returns a read-only version of the row count.

        :return: the row count of the last executed operation
        :rtype: int
        '''
        return self._description if self._description is not None else -1

    def is_open(self: 'Cursor') -> bool:
        '''Indicate if a cursor is open taking into consideration the connec-
        tion status

        :return: Whether the cursor (and the connection) is open or not
        :rtype: bool
        '''
        return self.connection.is_open() and super().is_open()

    def callproc(
        self: 'Cursor',
        procname: str,
        *parameters: Tuple
    ) -> Any:
        '''Placeholder method for calling stored database procedures.

        :param procname: the stored procedure name
        :type procname: str
        :param parameters: a sequence containing the parameters that the proce-
        dure expects
        :type parameters: Tuple
        '''
        raise NotSupportedError
