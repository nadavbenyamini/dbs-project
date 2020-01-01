import requests
import queue


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
        self.db_items = []
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

    def fetch(self, params={}):
        """
        :param params: dictionary of HTTP query params
        :return: response from the actual HTTP GET request
        """
        url = self.get_url()
        return requests.get(url=url, headers=self.headers, params=params)

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

    def get_url(self):
        """
        :return: the final url for HTTP request
        """
        return '{}/{}'.format(self.base_url, self.path)

    def build_queries(self):
        for item in self.items():
            for (query, args) in self.item_to_queries(item):
                self.db_queue.put((query, args))

    def item_to_queries(self, item):
        """
        Converts a single item into the relevant queries
        :param item: JSON item from proccesed response
        :return: list of tuples, each tuple is (query, args)
        """
        pass
