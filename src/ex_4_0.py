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
    Get a list of shutdown events from the log file.

    Args:
    - logfile (str): The path to the log file.

    Returns:
    - list: A list of strings representing the shutdown events.
    """
    with open(logfile, 'r') as file:
        lines = file.readlines()

    shutdown_events = []
    for line in lines:
        if 'Shutdown initiated' in line:
            date_match = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', line)
            if date_match:
                shutdown_events.append(date_match.group(0))

    return shutdown_events

pass


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
