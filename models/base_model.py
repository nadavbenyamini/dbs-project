from database import sql_executor


class BaseModel:

    def get_distinct_values_by_field(self, field):
        """
        :param field: db column
        :return: values: list of unique values from that column
        """
        query = 'select distinct {} from {}'.format(field, self.table)
        results = sql_executor.select(query)
        rows = results['rows']
        field_index = results['headers'].index(field)
        results = set()
        for row in rows:
            results.add(row[field_index])
        return list(results)

    def get_distinct_values_by_multiple_fields(self, fields):
        """
        :param fields: list of db columns
        :return: values: list of unique tuples, each tuple consisted of the relevant columns
        """
        query = 'select distinct {} from {}'.format(', '.join(fields), self.table)
        results = sql_executor.select(query)
        rows = results['rows']
        field_indexes = [results['headers'].index(f) for f in fields]
        results = set()
        for row in rows:
            values = []
            for ind in field_indexes:
                values.append(row[ind])
            results.add(tuple(values))
        return list(results)
