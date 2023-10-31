"""
This module contains the main process for starting a study session.
"""
# DEPENDENCIES
## Builtin
import asyncio
from enum import Enum
## App
from app.constants.signals import SIGNALS
from app.interfaces import component_interfaces
from app.interfaces.component_interfaces import IOInterface, TimerInterface
from app.interfaces.signal_observer import SignalObserver


# VARIABLES
## Constants
IO_SIGNALS: Enum = SIGNALS.IO_SIGNALS.value
AUDIO_SIGNALS: Enum = SIGNALS.AUDIO_SIGNALS.value


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

async def start_timer(interface: TimerInterface, study_length: int) -> None:
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
def initialise_signal_observer(io_interface: IOInterface) -> SignalObserver:
    """
    Initializes a signal observer with the given IO interface.

    Args:
        io_interface (IOInterface): An instance of the IOInterface class.

    Returns:
        SignalObserver: An instance of the SignalObserver class.

    """
    io_signal_methods: dict = {
        IO_SIGNALS.PRINT_OUTPUT.value: io_interface.print,
    }
    audio_signal_methods: dict = {
        AUDIO_SIGNALS.NOTIFY.value: io_interface.notify,
        AUDIO_SIGNALS.FINISHED.value: io_interface.finished,
    }
    signal_observer = SignalObserver()
    signal_observer.attach_signalled_observers(io_signal_methods)
    signal_observer.attach_signalled_observers(audio_signal_methods)
    return signal_observer

def initialise_interfaces() -> tuple:
    """
    Initialise the interfaces required for the system.

    Returns:
        A tuple containing the IO interface and the Timer interface.
    """
    io_interface: IOInterface = component_interfaces.CLIIOInterface()
    signal_observer: SignalObserver = initialise_signal_observer(io_interface)
    timer_interface: TimerInterface = component_interfaces.RandomTimerInterface(signal_observer)

    return (signal_observer, io_interface, timer_interface)

async def initialise_timer() -> None:
    """
    Asynchronously initializes a timer.
    
    Parameters:
        None

    Returns:
        None
    """
    signal_observer, io_interface, timer_interface = initialise_interfaces()
    signal_observer.notify(AUDIO_SIGNALS.NOTIFY.value)
    study_length: int = get_study_length(io_interface)
    await start_timer(timer_interface, study_length)

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
    await initialise_timer()
    # Loop the function
    await start()

if __name__ == "__main__":
    print("Starting Up...")
    asyncio.run(start())
