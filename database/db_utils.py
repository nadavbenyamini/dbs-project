

def get_insert_queries(table, columns, records):
    values = ','.join([tuple(rec) for rec in records])
    query = "insert into {} {} values {};".format(table, tuple(columns),  values)
    print(query)
    return [query]

