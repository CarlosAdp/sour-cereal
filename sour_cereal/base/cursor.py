from __future__ import annotations


class BaseCursor(object):
    '''Define a base cursor for commands execution to a data source

    :param connection: The connection object that generated the cursor
    :type connection: BaseConnection
    '''
    def __init__(
        self: 'BaseCursor',
        connection,
        *args, **kwargs
    ) -> None:
        self.connection = connection
