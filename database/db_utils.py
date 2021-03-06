import datetime


def get_insert_queries(table, columns, records):
    columns_string = prepare_columns_string(columns)
    values = prepare_values_string(records)
    query = "insert IGNORE into {} {} values {};".format(table, columns_string, values)
    return [query]


def prepare_columns_string(columns):
    return '(' + ', '.join(['{}'.format(c.replace("'", "")) for c in columns]) + ')'


def prepare_values_string(records):
    values_str = ','.join(['{}'.format(tuple(rec)) for rec in records])
    return values_str.replace("'NULL'", "NULL")


def validate_timestamp(value):
    try:
        clean = value.replace('T', ' ').replace('Z', '')
        datetime.datetime.strptime(clean, '%Y-%m-%d %H:%M:%S')
        return clean
    except ValueError:
        return None


def clean_string(s):
    return s.replace("'", "''").replace("%", "\\%")
