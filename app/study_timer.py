"""
This module contains the main process for starting a study session.
"""
# DEPENDENCIES
## Builtin
import asyncio
## App
from app.interfaces.component_interfaces import IOInterface
from app.interfaces.component_interfaces import TimerInterface
from app.interfaces import component_interfaces
## Temp
from app.components import study_io


# INTERFACES
def get_study_length(interface: IOInterface) -> int:
    """
    Get the length of a study from the given interface.

    Args:
        communication (IOCommunication): The communication object containing the study.

    Returns:
        int: The length of the study.
    """
    return interface.get_study_length()

async def start_random_timer(interface: TimerInterface, study_length: int) -> None:
    """
    Start a random timer from the given interface for the given study length.

    Parameters:
        interface (TimerInterface): The interface for the timer.
        study_length (int): The length of the study in seconds.

    Returns:
        None
    """
    await interface.start_timer(study_length)


# MAIN PROCESS
async def start() -> None:
    """
    Start the study session.

    This function plays a notification sound, gets the study length from the study_io module,
    creates a random timer, and starts the timer with the study length. 

    Parameters:
    None

    Returns:
    None
    """
    study_io_interface = component_interfaces.StudyIOInterface()
    study_length: int = get_study_length(study_io_interface)
    random_timer_interface = component_interfaces.RandomTimerInterface()
    await start_random_timer(random_timer_interface, study_length)
    # Loop the function
    await start()

if __name__ == "__main__":
    print("Starting Up...")
    study_io.play_notify()
    asyncio.run(start())
