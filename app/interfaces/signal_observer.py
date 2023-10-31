"""
This module handles signals using the observer pattern
"""
# DEPENDENCIES
## Builtin
from typing import Callable, TypedDict


# VARIABLES
## Constants
class Signal(TypedDict):
    """
    Dictionary representing a signal string and its associated callable function.
    """
    signal: str
    callable_function: Callable[[str], None]
### Error Messages
SIGNAL_NOT_FOUND: str = "Signal does not exist: "


# BASE CLASS
class SignalObserver:
    """
    Class representing a signal observer.
    """
    # VARIABLES
    signal_observers: Signal = {}
    # OBSERVER METHODS
    def attach_signalled_observers(self, signal_observers: Signal) -> None:
        """
        Attach a signal observer to the current object.

        Args:
            signal_observer (Signal): The signal observer dictionary to be attached.

        Returns:
            None
        """
        try:
            self.signal_observers.update(signal_observers)
        except TypeError as error:
            assert error

    def detach_signal(self, signal: str) -> None:
        """
        Remove a signal observer from the list of signal observers.

        Parameters:
            signal (str): The name of the signal to detach.

        Returns:
            None
        """
        try:
            del self.signal_observers[signal]
        except KeyError as error:
            assert Exception(f"{SIGNAL_NOT_FOUND}{error}")

    def notify(self, signal: str, *args: str ) -> None:
        """
        Notifies the observers for a given signal.

        Args:
            signal (str): The signal to notify the observers for.
            *args (str): Variable number of arguments to pass to the observers.

        Returns:
            None
        """
        if not signal in self.signal_observers:
            return
        function_callable = self.signal_observers[signal]
        function_callable(*args)
        if len(args) > 1:
            _ = [function_callable(argument) for argument in args if isinstance(argument, str)]
            return
        function_callable(*args)
            