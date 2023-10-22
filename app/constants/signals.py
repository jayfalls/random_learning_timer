"""
All the different signals to handle observer behaviour
"""
# DEPENDENCIES
## Builtin
from enum import Enum


# VARIABLES
## Constants
### Private
class _IO(Enum):
    """
    Enum class for representing different IO signals.
    """
    PRINT_OUTPUT: str = "print_output"

class _AUDIO(Enum):
    """
    Enum class for representing different Audio signals.
    """
    NOTIFY: str = "notify"
    FINISHED: str = "finished"


### Public
class SIGNALS(Enum):
    """
    Enum class for representing different signal types.
    """
    IO_SIGNALS: Enum = _IO
    AUDIO_SIGNALS: Enum = _AUDIO
