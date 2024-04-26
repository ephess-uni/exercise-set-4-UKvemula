""" ex_4_1.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


import re

def num_shutdowns(logfile):
    """
    Counts the number of shutdown events in the given log file.

    Args:
    - logfile (str): The path to the log file.

    Returns:
    - int: The number of shutdown events.
    """
    with open(logfile, 'r') as file:
        lines = file.readlines()

    shutdown_count = 0
    for line in lines:
        if "Shutdown initiated" in line:
            shutdown_count += 1

    return shutdown_count


# Example usage
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')
    pass


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')

