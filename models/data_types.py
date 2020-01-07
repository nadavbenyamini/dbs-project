import datetime


def validate_timestamp(value):
    try:
        clean = value.replace('T', ' ').replace('Z', '')
        datetime.datetime.strptime(clean, '%Y-%m-%d %H:%M:%S')
        return clean
    except ValueError:
        return None
