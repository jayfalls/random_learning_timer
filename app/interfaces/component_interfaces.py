"""
This module contains the interfaces for control of the components.
"""
# DEPENDENCIES
## Builtin
from abc import ABC, abstractmethod
## App
from app.components import study_io
from app.components.random_timer import RandomTimer


# BASE CLASSES
class IOInterface(ABC):
    """
    Interface class for a IO module.
    """
    @staticmethod
    @abstractmethod
    def get_study_length() -> int:
        """
        Get the length of a study.

        Returns:
            int: The length of the study.
        """

class TimerInterface(ABC):
    """
    Interface class for a Timer module.
    """
    @staticmethod
    @abstractmethod
    async def start_timer(study_length: int) -> None:
        """
        Start a timer for the specified study length.

        Parameters:
            study_length (int): The length of the study session in minutes.

        Returns:
            None
        """


# IMPLEMENTATIONS
class StudyIOInterface(IOInterface):
    """
    Interface class for the StudyIO module.
    """
    @staticmethod
    def get_study_length() -> int:
        """
        Get the length of a study.

        Returns:
            int: The length of the study.
        """
        return study_io.get_study_length()

class RandomTimerInterface(TimerInterface):
    """
    Interface class for the RandomTimer module.
    """
    @staticmethod
    async def start_timer(study_length: int) -> None:
        """
        Start a timer for the specified study length.

        Parameters:
            study_length (int): The length of the study in seconds.

        Returns:
            None
        """
        random_timer = RandomTimer()
        await random_timer.start_timer(study_length)
