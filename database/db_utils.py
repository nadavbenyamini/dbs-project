

def get_insert_queries(table, columns, records):
    values = ','.join(['{}'.format(tuple(rec)) for rec in records])
    columns_string = '(' + ', '.join(['{}'.format(c.replace("'", "")) for c in columns]) + ')'
    query = "insert into {} {} values {};".format(table, columns_string, values)
    print(query)
    return [query]

