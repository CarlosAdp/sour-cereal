'''Defines an extraction.'''
from typing import Any, List, Tuple
from datetime import datetime

from .connections.base_source_connection_interface import \
        BaseSourceConnectionInterface


class Extraction:
    '''Describe the procedure of data fetching.

    :param source: a data source class or instance
    :type source: BaseSourceConnection
    :param parameters: a dictionary with the extraction parameters
    :type parameters: dict, optional

    An extraction describes the procedure of data fetching from a source. It's
    instantiation requires a data source and a dictionary of parameters.

    Every extraction may have a fingerprint and a list of pairs (timestamp,
    status), from which one may check if the extraction is ready or not.
    '''
    source: BaseSourceConnectionInterface
    parameters: Any
    fingerprint: Any
    status_over_time: list

    def __init__(
        self: 'Extraction',
        source: BaseSourceConnectionInterface,
        parameters: Any = None
    ) -> None:
        '''Please, refer to the class documentation.'''
        self.source = source
        self.parameters = parameters
        self.fingerprint = None
        self.status_over_time = []

    def prepare(self: 'Extraction') -> None:
        '''Prepare the extraction and set its fingerprint.

        :raises IOError: raised when the method does not succeed.
        '''
        self.fingerprint = self.source.prepare_extraction(self.parameters)

    def get_all_status(self: 'Extraction') -> List[Tuple]:
        '''Return all extraction's status

        :return: the description of the current status
        :rtype: Any
        '''
        return self.status_over_time

    def get_current_status(self: 'Extraction') -> Tuple:
        '''Return only the current status

        :return: only the current status of the extraction
        :rtype: Tuple
        '''
        return next(filter(lambda t: t[0], self.status_over_time), None)[1]

    def update_status(self: 'Extraction') -> None:
        '''Update status list with a new status.

        :raises IOError: raised when the method does not succeed.
        '''
        self.status_over_time.append(
            (datetime.now(),
             self.source.get_status_of_extraction(self.fingerprint))
        )

    def is_ready(self: 'Extraction') -> bool:
        '''Indicate whether the extraction is ready or not (may use the
        `get_current_status` method).

        :raises IOError: raised when the method does not succeed.
        :return: `True` if it's ready and `False` otherwise
        :rtype: bool
        '''
        return self.source.check_availability_of_extraction(
            self.get_current_status()
        )

    def execute(self: 'Extraction') -> Any:
        '''Execute the extraction and return a result.

        :raises IOError: raised when the method does not succeed.
        :return: the result of the extraction. It may be a list of filenames to
        which data was writing, the data itself, etc.
        :rtype: Any
        '''
        return self.source.execute_extraction(self.fingerprint)

    def clean_resources(self: 'Extraction') -> bool:
        '''Attempt to clean resources that might have been allocated for the
        extraction and return this operation's success (or failure).

        :raises IOError: raised when the method does not succeed.
        :return: `True` if the resources got cleaned and `False` otherwise
        :rtype: bool
        '''
        return self.source.clean_resources_of_extraction(self.fingerprint)