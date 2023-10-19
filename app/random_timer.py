"""
This module is responsible for generating a random timer for a specified length of time in minutes.
"""

import asyncio
import random
import study_io

# VARIABLES
## Constants
TIME_SPAN: tuple = (360, 1080) # Seconds


class RandomTimer:
    """
    This class represents a random timer.
    It can be used to generate random time intervals within a specified range.

    Attributes:
        None

    Methods:
        __init__: Initializes an instance of the class.

    Example usage:
        timer = RandomTimer()
        timer.start_random_timer(minutes: int)
    """
    def __init__(self):
        self.time_up: bool = True

    async def time_has_passed(self, length_minutes: int) -> bool:
        """
        Check if a certain amount of time has passed.

        Args:
            length_minutes (int): The length of time in minutes.

        Returns:
            bool: True if the specified amount of time has passed, False otherwise.
        """
        time_passed: int = 1
        length_seconds: int = length_minutes * 60
        while True:
            await asyncio.sleep(1)
            time_passed += 1
            if time_passed > length_seconds:
                break
        return True

    async def random_notify(self) -> None:
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
        lowest_time, longest_time = TIME_SPAN
        while not self.time_up:
            waiting_time: int = random.randint(lowest_time, longest_time)
            await asyncio.sleep(waiting_time)
            print()
            study_io.immediate_print("Take a 10 second break")
            print()
            study_io.play_notify()

    async def print_progress(self) -> None:
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

    ## Timer Start
    async def start_timer(self, length_minutes: int) -> None:
        """
        Generates a random timer for a specified length of time in minutes.

        Args:
            length_minutes (int): The length of time for the timer, in minutes.

        Returns:
            None
        """
        self.time_up = False
        counting_time = asyncio.create_task(self.time_has_passed(length_minutes))
        asyncio.create_task(self.random_notify())
        asyncio.create_task(self.print_progress())
        self.time_up = await counting_time
        print()
        study_io.immediate_print("Study Session Complete")
        study_io.play_finished()
