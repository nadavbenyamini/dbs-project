

def get_insert_queries(table, columns, records):
    values = ','.join(['{}'.format(tuple(rec)) for rec in records])
    query = "insert into {} {} values {};".format(table, tuple(columns),  values)
    return [query]

