from datetime import datetime


def check_date_format(a_date) -> bool:
    try:
        res = bool(datetime.strptime(a_date, '%d/%m/%Y'))
    except ValueError:
        res = False
    return res


def check_time_format(a_time) -> bool:
    try:
        res = bool(datetime.strptime(a_time, '%H:%M'))
    except ValueError:
        res = False
    return res
