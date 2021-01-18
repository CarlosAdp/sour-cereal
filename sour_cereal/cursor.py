from typing import Tuple

from open_close_mixin import OpenCloseMixin


class Cursor(OpenCloseMixin):
    connection: 'Connection'
    _description: Tuple[Tuple[str, ...], ...]
    _rowcount: int

    def __init__(self: 'Cursor', connection: 'Connection') -> None:
        self.connection = connection
        self._description = None
        self._rowcount = None

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
