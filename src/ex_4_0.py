""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


import re

def get_shutdown_events(logfile):
    """
    Return a list of shutdown events from the given log file.
    """
    with open(logfile, 'r') as file:
        return [line.strip() for line in file if 'Shutdown initiated' in line]

def num_shutdowns(logfile):
    """
    Return the number of shutdown events in the given log file.
    """
    return len(get_shutdown_events(logfile))

pass


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
