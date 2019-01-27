import requests


class Core:

    __API_BASE = 'https://xivapi.com/'

    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, endpoint, params=None):
        if not params:
            params = {}
        params['key'] = self.api_key
        url = self.request_url(endpoint)
        r = requests.get(url, params)
        if self.test_mode:
            return r
        return r.json()

    def request_url(self, endpoint):
        return '{}{}'.format(self.__API_BASE, endpoint)
