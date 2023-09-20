import asyncio
import random
import simpleaudio as sa
import sys
import time


# VARIABLES
TIME_SPAN: tuple = (360, 1080) # Seconds
NOTIFY_SOUND = sa.WaveObject.from_wave_file("app/sounds/notify.wav")
FINISHED_SOUND = sa.WaveObject.from_wave_file("app/sounds/study_done.wav")

# States
time_up: bool = True


# CLI INPUT
## Error Handling
def is_valid_number(string_input: str) -> bool:
    if string_input.isdigit():
        return True
    
    print("Please enter a valid number")
    return False

## User Values
def get_study_length() -> int:
    while True:
        study_length = input("How long is your study session in minutes?")
        
        if not is_valid_number(study_length):
            continue

        study_length = int(study_length)
        # Make sure amount is valid
        if study_length < 15:
            print("Time must be more than 15 minutes")
            continue
        
        break
        
    return study_length


# RANDOM TIMER
async def time_has_passed(length_minutes: int) -> bool:
    time_passed: int = 1
    length_seconds: int = length_minutes * 60
    while True:
        await asyncio.sleep(1)
        time_passed += 1
        if time_passed > length_seconds:
            break
    return True

async def random_notify() -> None:
    global time_up
    lowest_time, longest_time = TIME_SPAN
    print("Random Timer Started")
    while not time_up:
        waiting_time: int = random.randint(lowest_time, longest_time)
        sys.stdout.flush()  # Force immediate display
        await asyncio.sleep(waiting_time)
        print()
        print("Take a 10 second break")
        play_notify = NOTIFY_SOUND.play()
        play_notify.wait_done()  # Wait for the sound to finish playing
    print("Study Session Complete")
    play_done = FINISHED_SOUND.play()
    play_done.wait_done()  # Wait for the sound to finish playing

async def print_progress() -> None:
    global time_up
    time_passed: int = 0
    while not time_up:
        time_passed += 1
        minutes, seconds = divmod(time_passed, 60)
        print(f"{minutes}:{seconds}", end="\r")
        sys.stdout.flush()  # Force immediate display
        await asyncio.sleep(1)

## Timer Start
async def random_timer(length_minutes: int) -> None:
    global time_up
    time_up = False
    counting_time = asyncio.create_task(time_has_passed(length_minutes))
    randomly_notifying = asyncio.create_task(random_notify())
    printing_timer_progress = asyncio.create_task(print_progress())
    time_up = await counting_time
        

# MAIN PROCESS
async def start() -> None:
    play_notify = NOTIFY_SOUND.play()
    study_length = get_study_length()
    await random_timer(study_length)

asyncio.run(start())