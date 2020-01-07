from database import sql_executor
import datetime

INT = 'INT'
STRING = 'STRING'
TIMESTAMP = 'TIMESTAMP'


# TODO: Move to some utils file/class
def validate_timestamp(value):
    try:
        clean = value.replace('T', ' ').replace('Z', '')
        datetime.datetime.strptime(clean, '%Y-%m-%d %H:%M:%S')
        return clean
    except ValueError:
        return None


class BaseModel:

    def get_distinct_values_by_field(self, field, use_ssh=False):
        """
        :param field: db column
        :param use_ssh: True iff running outside of Nova (i.e. when fetching data)
        :return: values: list of unique values from that column
        """
        query = 'select distinct {} from {}'.format(field, self.table)
        results = sql_executor.select(query, use_ssh=use_ssh)
        rows = results['rows']
        field_index = results['headers'].index(field)
        results = set()
        for row in rows:
            results.add(row[field_index])
        return list(results)

    def get_distinct_values_by_multiple_fields(self, fields, use_ssh=False):
        """
        :param fields: list of db columns
        :param use_ssh: True iff running outside of Nova (i.e. when fetching data)
        :return: values: list of unique tuples, each tuple consisted of the relevant columns
        """
        query = 'select distinct {} from {}'.format(', '.join(fields), self.table)
        results = sql_executor.select(query, use_ssh=use_ssh)
        rows = results['rows']
        field_indexes = [results['headers'].index(f) for f in fields]
        results = set()
        for row in rows:
            values = []
            for ind in field_indexes:
                values.append(row[ind])
            results.add(tuple(values))
        return list(results)
