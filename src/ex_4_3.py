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
      Calculate the amount of time between the first and last shutdown events in the log file.

      Args:
      - logfile (str): The path to the log file.

      Returns:
      - timedelta: The amount of time between the first and last shutdown events.
      """
    shutdown_events = get_shutdown_events(logfile)

    if not shutdown_events:
        return timedelta(seconds=0)

    first_shutdown = logstamp_to_datetime(shutdown_events[0])
    last_shutdown = logstamp_to_datetime(shutdown_events[-1])

    return last_shutdown - first_shutdown
    pass


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')

