import requests
# from database.db_utils import get_insert_queries
# from models.all_models import *
from database import sql_executor
import traceback


class BaseFetcher:
    """
    Base class for remote data fetching
    Should be inherited by a class per source - which handles that source's headers, api key's, tokens, etc.
    Each of those source classes should be inherited by classes for specific api paths that are responsible
    for preparing the HTTP request and handling it's response

    The general flow is -
    1) Prepare params for each request
    2) Fetch responses and process them into items in the relevant structure for our DB
    3) Turn these items into SQL insert queries, and execute
    4) return a summary to indicate errors in api requests / queries
    """
    def __init__(self):
        self.requests = []
        self.api_responses = []
        self.api_errors = []
        # self.items = []
        # self.tables_updated = []
        self.queries = []
        self.db_responses = []
        self.db_errors = []
        self.sql_executor = sql_executor

    def fetch_all(self):
        self.requests = self.prepare_requests()
        self.start_fetching()
        # self.build_insert_queries()
        self.execute_insert_queries()
        return self.get_summary()

    def start_fetching(self):
        """
        Iterates over self.requests, each item is the params dictionary for a single HTTP request
        Then fetches, processes and stores the responses, and errors if were
        """
        i = 0
        for req in self.requests:
            print('Path: {} started request {}: {}'.format(self.path, i, req))
            try:
                response = self.fetch(req)
                self.api_responses.append(response.json())
                self.queries += self.response_to_insert_queries(req, response.json())
                # self.items += self.response_to_items(req, response.json())
            except Exception as e:
                self.api_errors.append(str(e))
            finally:
                i += 1

    def get_url(self):
        """
        :return: the final url for HTTP request
        """
        return '{}/{}'.format(self.base_url, self.path)

    def fetch(self, params={}):
        """
        :param params: dictionary of HTTP query params
        :return: response from the actual HTTP GET request
        """
        url = self.get_url()
        return requests.get(url=url, headers=self.headers, params=params)

    def execute_insert_queries(self):
        i = 0
        for query in self.queries:
            i += 1
            try:
                response = sql_executor.insert(query, use_ssh=True)
                print('Query {} succeeded'.format(i))
                self.db_responses.append(response)
            except Exception as e:
                print('Query {} failed: {}'.format(i, e))
                self.db_errors.append(traceback.format_exc())

    def get_summary(self):
        """
        :return: JSON response with a summary of the fetching results
        """
        request_count = len(self.requests)
        success_count = len(self.api_responses)
        summary = {
            'data_fetch': {
                'summary': 'Finished processing {} requests, {} succeeded'.format(request_count, success_count),
                'errors': self.api_errors},
            'data_insertion': {
                'summary': 'Finished preparing and executing {} queries, {} succeeded'.format(len(self.queries), len(self.db_responses)),
                'errors': self.db_errors
            }
        }
        return summary

    # ------------------------------------------------------------------------------- #
    # ------------------ Functions to be overridden by subclasses ------------------- #
    # ------------------------------------------------------------------------------- #

    def prepare_requests(self):
        """
        Prepare the params of the requests. Specific for each data source and path
        """
        pass

    def response_to_items(self, request, response):
        """
        Process the results JSON into the relevant structure before inserting to our DB
        Each of these JSON items can be inserted to one table or more
        :return: list of JSON items
        """
        pass

    def response_to_insert_queries(self, request, response):
        """
        Process the results JSON into the relevant insert queries for our DB
        :param request: dictionary with params of HTTP request
        :param response: HTTP response
        :return: list insert queries
        """
        pass


# OLD CODE:
'''
    def build_insert_queries(self):
        """
        Converts item list to DB record structure and populates query list with the final queries
        """
        all_records = {}
        for item in self.items:
            try:
                item_records = self.item_to_records(item)
                for table in item_records:
                    if table not in all_records:
                        all_records[table] = []
                    all_records[table] += item_records[table]
            except Exception as e:
                print('Error in item_to_records: {}'.format(e))
                self.db_errors.append(traceback.format_exc())

        self.tables_updated = list(set(all_records.keys()))

        for table in all_records:
            columns = self.table_to_columns(table)
            if len(columns) > 0:
                queries = get_insert_queries(table, columns, all_records[table])
                for q in queries:
                    self.queries.append(q)

    def table_to_columns(self, table):
        for m in self.models:
            if m.table == table:
                return [f['name'] for f in m.fields]
        return []

    def item_to_records(self, item):
        """
        Converts a single item into the tuples according to the relevant DB records, per table
        :param item: JSON item from processed response
        :return: dictionary - {table1: [record1, record2], table2: [record1, record2]}

        This is a DEFAULT IMPLEMENTATION only, can be overridden
        """
        records = {}
        for model in self.models:
            records[model.table] = []
            record = []

            for field in model.fields:
                value = item.get(field['name'], None)
                try:
                    if field['pk']:
                        assert value is not None
                    if value is None:
                        record.append('NULL')
                    elif field['type'] == INT:
                        record.append(int(value))
                    elif field['type'] == STRING:
                        record.append(str(value).replace('%', '\\%'))
                    elif field['type'] == TIMESTAMP:
                        value = validate_timestamp(value)
                        record.append(value)
                    else:
                        record.append(value)

                except Exception as e:
                    print('Error adding {} to record: {}, value={}'.format(e, field['name'], value))
                    raise e

            records[model.table].append(tuple(record))
        return records
'''