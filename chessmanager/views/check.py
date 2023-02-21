from datetime import datetime
from questionary import Validator, ValidationError, prompt


def check_date_format(a_date) -> bool:
    try:
        res = bool(datetime.strptime(a_date, '%d/%m/%Y'))
    except ValueError:
        res = False
    return res



