from datetime import datetime


def get_insert_queries(table, columns, records):
    columns_string = prepare_columns_string(columns)
    values = prepare_values_string(records)
    query = "insert into {} {} values {};".format(table, columns_string, values)
    print(query)
    return [query]


def prepare_columns_string(columns):
    columns.append('insertion_time')
    return '(' + ', '.join(['{}'.format(c.replace("'", "")) for c in columns]) + ')'


def prepare_values_string(records):
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    values_str = ','.join(['{}'.format(tuple(rec) + (now_str, )) for rec in records])
    return values_str.replace("'NULL'", "NULL")
