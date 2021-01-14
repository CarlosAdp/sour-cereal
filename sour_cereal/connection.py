from abc import ABC

from open_close_mixin import OpenCloseMixin

from .exceptions import NotSupportedError


class Connection(ABC, OpenCloseMixin):
    '''A connection instance a data source.

    It's open on instantiation.
    '''
    def __init__(self: 'Connection'):
        super().__init__()
        self.open()

    def close(self: 'Connection') -> None:
        '''Close the connection '''
        self.rollback()
        super().close()

    def commit(self: 'Connection') -> None:
        raise NotSupportedError

    def rollback(self: 'Connection') -> None:
        raise NotSupportedError
