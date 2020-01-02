from database import sql_executor


class BaseModel:

    def get_all_values_by_field(self, field):
        query = 'select distinct {} from {}'.format(field, self.table)
        results = sql_executor.select(query)
        rows = results['rows']
        field_index = results['headers'].index(field)
        results = set()
        for row in rows:
            results.add(row[field_index])
        return list(results)
