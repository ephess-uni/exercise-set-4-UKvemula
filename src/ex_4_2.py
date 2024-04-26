""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    """
        Parse a date string in the format 'YYYY-MM-DDTHH:MM:SS' into a datetime.datetime object.

        Args:
        - datestr (str): Date string in the format 'YYYY-MM-DDTHH:MM:SS'.

        Returns:
        - datetime.datetime: Datetime object parsed from the input date string.
        """
    return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')

    pass


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')