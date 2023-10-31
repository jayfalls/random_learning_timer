"""
This module is responsible for generating a random timer for a specified length of time in minutes.
"""
# DEPENDENCIES
## Builtin
import asyncio
from enum import Enum
import random
## App
from app.constants.signals import SIGNALS
from app.interfaces.signal_observer import SignalObserver

# VARIABLES
## Constants
### Signals
IO_SIGNALS: Enum = SIGNALS.IO_SIGNALS.value
AUDIO_SIGNALS: Enum = SIGNALS.AUDIO_SIGNALS.value
### Modifiers
RANDOM_TIME_SPAN: tuple = (360, 900) # Seconds


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
    def __init__(self, signal_observer: SignalObserver):
        self.time_up: bool = True
        self.signal_observer = signal_observer

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
        self.signal_observer.notify(IO_SIGNALS.PRINT_OUTPUT.value, "Random Timer Started")
        print()
        lowest_time, longest_time = RANDOM_TIME_SPAN
        while not self.time_up:
            waiting_time: int = random.randint(lowest_time, longest_time)
            await asyncio.sleep(waiting_time)
            print()
            self.signal_observer.notify(IO_SIGNALS.PRINT_OUTPUT.value, "Take a 10 second break")
            print()
            self.signal_observer.notify(AUDIO_SIGNALS.NOTIFY.value)

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
            self.signal_observer.notify(IO_SIGNALS.PRINT_OUTPUT.value, f"{minutes}:{seconds}")
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
        coroutines: tuple = (
            self.__time_has_passed(length_minutes),
            self.__random_notify(),
            self.__print_progress(),
        )
        tasks: list = [asyncio.create_task(coroutine) for coroutine in coroutines]
        await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        self.time_up = True
        print()
        self.signal_observer.notify(IO_SIGNALS.PRINT_OUTPUT.value, "Study Session Complete!")
        self.signal_observer.notify(AUDIO_SIGNALS.FINISHED.value)
