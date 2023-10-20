"""
This module contains the main process for starting a study session.
"""
# DEPENDENCIES
## Third Party
import asyncio
## App
from components import study_io
from components.random_timer import RandomTimer


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
    study_io.play_notify()
    study_length: int = study_io.get_study_length()
    random_timer = RandomTimer()
    await random_timer.start_timer(study_length)
    await start()

if __name__ == "__main__":
    print("Starting Up...")
    asyncio.run(start())
