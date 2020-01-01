import requests
import queue
from data_fetch.db_utils import get_insert_queries


# Base abstract class for fetching data and inserting to db
class BaseFetcher:
    """
    Base class for remote data fetching
    Should be inherited by a class per source - which handles that source's headers, api key's, tokens, etc.
    Each of those source classes should be inherited by classes for specific api paths that are responsible
    for preparing the HTTP request and handling it's response

    The general process is -
    1) prepare params for each request
    2) fetch responses
    3) process responses into the relevant structure for our DB
    4) return a summary of which request succeeded and which failed
    """
    def __init__(self):
        self.requests = []
        self.responses = []
        self.errors = []
        self.items = []
        self.db_queue = queue.Queue()

    def fetch_all(self):
        self.requests = self.prepare_requests()
        self.start_fetching()
        self.build_queries()
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
                self.responses.append(response.json())
                self.items += self.response_to_items(response.json())
                self.errors.append(None)
            except Exception as e:  # requests.exceptions.HTTPError as e:
                self.errors.append(e)
                self.responses.append(None)
            finally:
                i += 1

    def get_summary(self):
        """
        :return: JSON response with a summary of the fetching results
        """
        request_count = len(self.requests)
        success_count = len([r for r in self.responses if r is not None])
        summary = {'summary': 'Finished processing {} requests, {} succeeded'.format(request_count, success_count),
                   'requests': []}

        for i in range(len(self.requests)):
            req = self.requests[i]
            res = self.responses[i]
            result_count = len(res) if type(res) == list else len(res.keys())
            err = self.errors[i]
            summary['requests'].append({'request': req, 'result_count': result_count, 'error': err})

        return summary

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

    def build_queries(self):
        """
        Converts item list to DB record structure and populates query queue with the final queries
        """
        all_records = {}
        for item in self.items:
            item_records = self.item_to_records(item)
            for table in item_records:
                if table not in all_records:
                    all_records[table] = []
                all_records[table] += item_records[table]

        for table in all_records:
            queries = get_insert_queries(table, all_records[table])
            for q in queries:
                self.db_queue.put(q)

    # ------------------------------------------------------------------------------- #
    # ------------------ Functions to be overridden by subclasses ------------------- #
    # ------------------------------------------------------------------------------- #

    def prepare_requests(self):
        """
        Prepare the params of the requests. Specific for each data source and path
        """
        pass

    def response_to_items(self, response):
        """
        Process the results JSON into the relevant structure before inserting to our DB
        :return: list of JSON items
        """
        pass

    def item_to_records(self, item):
        """
        Converts a single item into the DB records, per table
        :param item: JSON item from proccesed response
        :return: dictionary - {table1: {key1: record, key2: record}, table2: {key1: record, key2: record}}
        """
        pass
