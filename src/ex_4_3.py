""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<

def time_between_shutdowns(logfile):
    """
    Calculate the amount of time between the first and last shutdowns in a log file.

    Args:
    - logfile (str): The path to the log file.

    Returns:
    - timedelta: The amount of time between the first and last shutdowns.
    """
    shutdown_events = get_shutdown_events(logfile)

    # If shutdown_events is a string, split it into lines
    if isinstance(shutdown_events, str):
        shutdown_events = shutdown_events.split('\n')

    # Assuming shutdown_events is a list of strings
    shutdown_events = [event.strip() for event in shutdown_events if event.strip()]

    # Assuming each line is a log entry with a timestamp
    timestamps = [line.split(' ')[1] for line in shutdown_events]

    # Assuming timestamps is a list of timestamp strings
    datetimes = [logstamp_to_datetime(timestamp) for timestamp in timestamps]

    # Calculate the timedelta between the first and last timestamps
    time_diff = max(datetimes) - min(datetimes)

    return time_diff



# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
