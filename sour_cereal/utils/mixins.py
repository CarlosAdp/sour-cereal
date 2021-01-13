from abc import ABC
from typing import Callable, Type
from functools import wraps
from sour_cereal.exception import Error


class OpenCloseMixin(ABC):
    '''Mixin for classes with open-close dynamics.'''

    def when_closed(method: Callable) -> Callable:
        '''Mark a method to allow it's execution even when it's instance is
        closed.
        '''
        setattr(method, '_when_closed', True)
        return method

    def _only_if_open(method: Callable) -> Callable:
        '''Run a method only when it is allowed to.

        A method is allowed to run when it's instance is open or, otherwise,
        when it has permission by being marked by the :func:`~when_closed`
        decorator.
        '''
        @wraps(method)
        def wrapped(instance, *args, **kwargs):
            if instance._open or getattr(method, '_when_closed', False):
                return method(instance, *args, **kwargs)
            else:
                raise Error(
                    f'The instance is closed and the method {method.__name__} '
                    'cannot run in such condition.'
                )

        return wrapped

    def __init_subclass__(
        cls: Type['OpenCloseMixin'], **kwargs
    ) -> Type['OpenCloseMixin']:
        for attr_name in cls.__dict__:
            if (
                isinstance(attr := getattr(cls, attr_name), Callable)
                and not attr_name.startswith('__')
            ):
                setattr(cls, attr_name, cls._only_if_open(attr))

        return cls

    @when_closed
    def open(self: 'OpenCloseMixin') -> None:
        self._open = True

    @when_closed
    def close(self: 'OpenCloseMixin') -> None:
        setattr(self, '_open', False)
