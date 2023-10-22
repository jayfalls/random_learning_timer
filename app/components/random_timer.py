"""
This module is responsible for generating a random timer for a specified length of time in minutes.
"""
# DEPENDENCIES
## Builtin
import asyncio
import random
## App
from app.components import study_io

# VARIABLES
## Constants
RANDOM_TIME_SPAN: tuple = (360, 1080) # Seconds


# FUNCTIONS
class RandomTimer:
    """
    This class represents a random timer.
    It can be used to generate random time intervals within a specified range.

    Attributes:
        None

    Methods:
        time_has_passed(length_minutes: int) 
            Checks if a certain amount of time has passed.
        random_notify() 
            Generates a random notification at random intervals.
        print_progress() 
            Prints the progress every second.
        start_timer(length_minutes: int) 
            Generates random timers for a specified length of time in minutes.

    Example usage:
        timer = RandomTimer()
        timer.start_random_timer(minutes: int)
    """
    def __init__(self):
        self.time_up: bool = True

    # INNER FUNCTIONS
    async def __time_has_passed(self, length_minutes: int) -> None:
        """
        A function that checks if a certain amount of time has passed.

        Parameters:
            length_minutes (int): The length of time in minutes.

        Returns:
            None: This function does not return anything.
        """
        time_passed: int = 1
        length_seconds: int = length_minutes * 60
        while True:
            await asyncio.sleep(1)
            time_passed += 1
            if time_passed > length_seconds:
                break

    async def __random_notify(self) -> None:
        """
        Asynchronous function that generates random notifications at random intervals.
        The function does the following:
        - Prints "Random Timer Started"
        - Generates a random waiting time between `lowest_time` and `longest_time`
        - Sleeps for the generated waiting time
        - Prints "Take a 10 second break"
        - Plays a notification sound and waits for it to finish playing

        Returns:
        None
        """
        study_io.immediate_print("Random Timer Started")
        print()
        lowest_time, longest_time = RANDOM_TIME_SPAN
        while not self.time_up:
            waiting_time: int = random.randint(lowest_time, longest_time)
            await asyncio.sleep(waiting_time)
            print()
            study_io.immediate_print("Take a 10 second break")
            print()
            study_io.play_notify()

    async def __print_progress(self) -> None:
        """
        Asynchronously prints the progress every second.

        Parameters:
        None

        Returns:
        None
        """
        time_passed: int = 0
        while not self.time_up:
            time_passed += 1
            minutes, seconds = divmod(time_passed, 60)
            study_io.immediate_print(f"{minutes}:{seconds}")
            await asyncio.sleep(1)

    # OUTER FUNCTIONS
    async def start_timer(self, length_minutes: int) -> None:
        """
        Generates random timers for a specified length of time in minutes.

        Args:
            length_minutes (int): The length of time for the timer, in minutes.

        Returns:
            None
        """
        self.time_up = False
        tasks: tuple = (
            self.__time_has_passed(length_minutes),
            self.__random_notify(),
            self.__print_progress()
        )
        await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        self.time_up = True
        print()
        study_io.immediate_print("Study Session Complete")
        study_io.play_finished()
