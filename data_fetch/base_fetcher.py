import requests
from database import sql_executor
import traceback


class BaseFetcher:
    """
    Base class for remote data fetching
    Should be inherited by a class per source - which handles that source's headers, api key's, tokens, etc.
    Each of those source classes should be inherited by classes for specific api paths that are responsible
    for preparing the HTTP request and parsing it's response

    The general flow is -
    1) Prepare params for each request
    2) Fetch responses and parse them into insert queries
    3) Execute the queries
    4) return a summary to indicate errors in api requests / queries
    """
    def __init__(self):
        self.requests = []
        self.api_responses = []
        self.api_errors = []
        self.queries = []
        self.db_responses = []
        self.db_errors = []
        self.sql_executor = sql_executor

    def fetch_all(self):
        self.requests = self.prepare_requests()
        self.start_fetching()
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
                # self.queries += self.response_to_insert_queries(req, response.json())
                self.queries = self.response_to_insert_queries(req, response.json())
                self.execute_insert_queries()
            except Exception as e:
                print(e)
                self.api_errors.append(str(e))
            finally:
                i += 1
        self.queries = []


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
        """
        Executes list of queries sequentially, stores errors and responses in class fields
        """
        i = 0
        for query in self.queries:
            print(query)
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

    def response_to_insert_queries(self, request, response):
        """
        Process the results JSON into the relevant insert queries for our DB
        :param request: dictionary with params of HTTP request
        :param response: HTTP response
        :return: list insert queries
        """
        pass
