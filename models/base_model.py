from database import sql_executor
import datetime

INT = 'INT'
STRING = 'STRING'
TIMESTAMP = 'TIMESTAMP'


# Small utility to validate and clean strings in timestamp format before insertion to DB
def validate_timestamp(value):
    try:
        clean = value.replace('T', ' ').replace('Z', '')
        datetime.datetime.strptime(clean, '%Y-%m-%d %H:%M:%S')
        return clean
    except ValueError:
        return None


class BaseModel:

    def get_distinct_values_by_field(self, field, order_by=None, desc=True, use_ssh=False):
        """
        :param field: db column
        :param order_by: db_column
        :param desc: True iff sort descending
        :param use_ssh: True iff running outside of Nova (i.e. when fetching data)
        :return: values: list of unique values from that column
        """
        order_by_field = order_by if order_by else ''
        order_by_direction = 'desc' if order_by and desc else 'asc' if order_by else ''
        query = 'select distinct {0} from {1} {2} {3}'\
            .format(field, self.table, order_by_field, order_by_direction)
        results = sql_executor.select(query, use_ssh=use_ssh)
        rows = results['rows']
        field_index = results['headers'].index(field)
        results = set()
        for row in rows:
            results.add(row[field_index])
        return list(results)

    def get_distinct_values_by_multiple_fields(self, fields, order_by=None, desc=True, use_ssh=False):
        """
        :param fields: list of db columns
        :param order_by: db_column
        :param desc: True iff sort descending
        :param use_ssh: True iff running outside of Nova (i.e. when fetching data)
        :return: values: list of unique tuples, each tuple consisted of the relevant columns
        """

        order_by_field = order_by if order_by else ''
        order_by_direction = 'desc' if order_by and desc else 'asc' if order_by else ''
        query = 'select distinct {0} from {1} {2} {3}'\
            .format(', '.join(fields), self.table, order_by_field, order_by_direction)
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
