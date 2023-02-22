from datetime import datetime


def check_date_format(a_date) -> bool:
    """ check if a_date is a date """
    try:
        res = bool(datetime.strptime(a_date, '%d/%m/%Y'))
    except ValueError:
        res = False
    return res


def check_time_format(a_time) -> bool:
    """ check if a_time is a time """
    try:
        res = bool(datetime.strptime(a_time, '%H:%M'))
    except ValueError:
        res = False
    return res
