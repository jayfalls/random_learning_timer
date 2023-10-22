"""
This module handles audio output.
"""
# DEPENDENCIES
## Builtin
from enum import Enum
## Third Party
import simpleaudio as sa
from simpleaudio import WaveObject


# VARIABLES
## Constants
NOTIFY_SOUND: WaveObject = sa.WaveObject.from_wave_file("app/sounds/notify.wav")
FINISHED_SOUND: WaveObject = sa.WaveObject.from_wave_file("app/sounds/study_done.wav")
class Sounds(Enum):
    """
    Enum class for representing different sounds.
    """
    NOTIFY_SOUND = NOTIFY_SOUND
    FINISHED_SOUND = FINISHED_SOUND

# PLAYBACK
def _play_sound(sound: WaveObject) -> None:
    """
    Play a sound.

    Args:
        sound (WaveObject): The sound to be played.

    Returns:
        None: This function does not return anything.
    """
    sound.play()

def play_notify() -> None:
    """
    Play a notification sound.

    Returns:
        None: This function does not return anything.
    """
    _play_sound(Sounds.NOTIFY_SOUND.value)

def play_finished() -> None:
    """
    Play a finished sound.

    Returns:
        None: This function does not return anything.
    """
    _play_sound(Sounds.FINISHED_SOUND.value)
