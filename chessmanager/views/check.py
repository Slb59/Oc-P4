from datetime import datetime


def check_date_format(a_date) -> bool:
    try:
        res = bool(datetime.strptime(a_date, '%d/%m/%Y'))
    except ValueError:
        res = False
    return res
