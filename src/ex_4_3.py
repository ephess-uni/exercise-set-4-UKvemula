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
    - logfile (str): Path to the log file.

    Returns:
    - datetime.timedelta: Time difference between the first and last shutdowns.
    """
    shutdown_events = get_shutdown_events(logfile)
    if len(shutdown_events) < 2:
        return timedelta(0)  # Return zero timedelta if less than two shutdown events

    first_shutdown = logstamp_to_datetime(shutdown_events[0].split()[1])
    last_shutdown = logstamp_to_datetime(shutdown_events[-1].split()[1])

    return last_shutdown - first_shutdown

# Example usage
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')

def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    pass


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
