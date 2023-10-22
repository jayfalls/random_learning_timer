"""
This module contains the interfaces for control of the components.
"""
# DEPENDENCIES
## Builtin
from abc import ABC, abstractmethod
from typing import final
## App
from app.components import audio
from app.components import cli_io
from app.components.random_timer import RandomTimer
from app.interfaces.signal_observer import SignalObserver


# BASE CLASSES
class IOInterface(ABC):
    """
    Interface class for IO modules.
    """
    # FIXED METHODS
    ## Audio Output
    @staticmethod
    @final
    def notify() -> None:
        """
        Play a notification sound.

        Returns:
            None
        """
        audio.play_notify()
    @staticmethod
    @final
    def finished() -> None:
        """
        Play a finished sound.

        Returns:
            None
        """
        audio.play_finished()

    # COMPULSORY METHODS
    ## Input
    @staticmethod
    @abstractmethod
    def get_study_length() -> int:
        """
        Get the length of a study.

        Returns:
            int: The length of the study.
        """
    ## Output
    @staticmethod
    @abstractmethod
    def print(text: str) -> None:
        """
        A static method that prints the given text.

        Args:
            text (str): The text to be printed.

        Returns:
            None
        """

class TimerInterface(ABC):
    """
    Interface class for Timer modules.
    """
    # INTIALISATION
    def __init__(self, signal_observer: SignalObserver):
        self.signal_observer = signal_observer

    # COMPULSORY METHODS
    @abstractmethod
    async def start_timer(self,study_length: int) -> None:
        """
        A static method that starts a timer.

        Args:
            signal_observer (SignalObserver): An instance of the SignalObserver class.
            study_length (int): The length of the study in seconds.

        Returns:
            None
        """


# IMPLEMENTATIONS
class CLIIOInterface(IOInterface):
    """
    Interface class for the cli_io module.
    """
    # INPUT
    @staticmethod
    def get_study_length() -> int:
        """
        Get the length of a study.

        Returns:
            int: The length of the study.
        """
        return cli_io.get_study_length()

    # OUTPUT
    @staticmethod
    def print(text: str) -> None:
        cli_io.immediate_print(text)

class RandomTimerInterface(TimerInterface):
    """
    Interface class for the RandomTimer module.
    """
    # TIMER METHODS
    async def start_timer(self, study_length: int) -> None:
        """
        Starts a timer for a study with the given study length.

        Args:
            signal_observer (SignalObserver): The signal observer object.
            study_length (int): The length of the study in seconds.

        Returns:
            None
        """
        random_timer = RandomTimer(self.signal_observer)
        await random_timer.start_timer(study_length)
