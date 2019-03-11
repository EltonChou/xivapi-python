import aiohttp
import requests


class Core:

    __API_BASE = 'https://xivapi.com/'

    def __init__(self, api_key, test_mode):
        self.api_key = api_key
        self.test_mode = test_mode

    def get(self, endpoint, params=None):
        if not params:
            params = {}
        params['key'] = self.api_key
        url = self.request_url(endpoint)
        # async with aiohttp.ClientSession() as session:
        #     async with session.get(url) as r:
        #         if self.test_mode:
        #             return await r
        #         return await r.json()
        r = requests.get(url, params)
        if self.test_mode:
            return r
        return r.json()

    def request_url(self, endpoint):
        return '{}{}'.format(self.__API_BASE, endpoint)
