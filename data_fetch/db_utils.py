

# Todo - wrap strings with '', handle Nones, add column list
def get_insert_queries(table, records):
    values = ','.join(['{}'.format(rec) for rec in records])
    query = "insert into {} values {};".format(table, values)
    print(query)
    return [query]

