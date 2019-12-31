import requests


# Base abstract class for fetching data and inserting to db
class BaseFetcher:
    def __init__(self):
        self.requests = []
        self.responses = []
        self.errors = []

    def fetch_all(self):
        self.prepare_requests()
        self.start_fetching()
        return self.after_fetching()

    def start_fetching(self):
        i = 0
        for req in self.requests:
            print('Path: {} started request {}: {}'.format(self.path, i, req))
            try:
                response = self.fetch(req)
                processed_response = self.process_response(response.json())
                self.responses.append(processed_response)
                self.errors.append(None)
            except Exception as e:  # requests.exceptions.HTTPError as e:
                self.errors.append(e)
                self.responses.append(None)
            finally:
                i += 1

    def after_fetching(self):
        request_count = len(self.requests)
        success_count = len([r for r in self.responses if r is not None])
        summary = "Finished processing {} requests, {} succeeded: [".format(request_count, success_count)

        for i in range(len(self.requests)):
            req = self.requests[i]
            res = self.responses[i]
            err = self.errors[i]
            summary += "{{request: {}, response: {}, error: {}}}, ".format(req, res, err)

        return (summary + ']XXX').replace(', ]XXX', ']')

    def fetch(self, params={}):
        url = self.get_url()
        return requests.get(url=url, headers=self.headers, params=params)

    def get_url(self):
        return '{}/{}'.format(self.base_url, self.path)

    def process_response(self, response):
        pass
