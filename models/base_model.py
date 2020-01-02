from database import sql_executor


class BaseModel:

    def get_all_values_by_field(self, field):
        query = 'select distinct (field)s from {}'.format(self.table)
        args = {'field': field}
        return sql_executor.select(query, args).get('rows', [])
