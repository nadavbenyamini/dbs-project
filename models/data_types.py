import datetime


# Fake ENUM
class Types:
    INT = 'INT'
    STRING = 'STRING'
    TIMESTAMP = 'TIMESTAMP'


def valid_timestamp(value):
    try:
        datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return True
    except TypeError:
        return False
