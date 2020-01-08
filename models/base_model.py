import datetime

INT = 'INT'
STRING = 'STRING'
TIMESTAMP = 'TIMESTAMP'


# Small utility to validate and clean strings in timestamp format before insertion to DB
def validate_timestamp(value):
    try:
        clean = value.replace('T', ' ').replace('Z', '')
        datetime.datetime.strptime(clean, '%Y-%m-%d %H:%M:%S')
        return clean
    except ValueError:
        return None


def clean_string(s):
    return s.replace("'", "\\'").replace("%", "\\%")


class BaseModel:
    pass
