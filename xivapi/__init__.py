import requests
from .core import Core


class Client(Core):

    __SUPPORT_LANGUAGE = ['en', 'jp', 'de', 'fr', 'cn', 'kr']
    __CHARACTER_DATA = ['AR', 'FR', 'FC', 'FCM', 'PVP']

    # FIXME: This is weired
    def __init__(self, api_key, test_mode=False, **kwargs):
        super().__init__(api_key, test_mode)
        self.params = {}
        for k, v in kwargs.items():
            self.params[k] = v

    def __get(self, endpoint, params=None):
        if not params:
            params = {}
        return super().get(endpoint, params={**self.params, **params})

    def search(self, **kwargs):
        return self.__get('search', kwargs)

    def lore(self, string: str):
        return self.__get('lore', {"string": string})

    def content(self, content=None, limit=100, ids=None, **kwargs):
        if not content:
            return self.__get('content')

        return self.__get(content, params=kwargs)

    def schema(self, content):
        return self.__get('{}/schema'.format(content))

    def servers(self, group=False):
        endpoint = 'servers/dc' if group else 'server'
        return self.__get(endpoint)

    def character(self, id, **kwargs):
        return self.__get('character/{}'.format(id), params=kwargs)

    def character_search(self, name, server=None, page=None):
        params = self.__nsp(name, server, page)
        return self.__get('character/search', params=params)

    def character_verification(self, id):
        return self.__get('character/{}/verification'.format(id))

    def character_update(self, id):
        return self.__get('character/{}/update'.format(id))

    def freecompany(self, id, **kwargs):
        return self.__get('freecompany/{}'.format(id))

    def freecompany_search(self, name, server=None, page=None):
        params = self.__nsp(name, server, page)
        return self.__get('freecompany/search', params=params)

    def linkshell(self, id, **kwargs):
        return self.__get('linkshell/{}'.format(id))

    def linkshell_search(self, name, server=None, page=None):
        params = self.__nsp(name, server, page)
        return self.__get('linkshell/search', params=params)

    def pvpteam(self, id):
        return self.__get('pvpteam/{}'.format(id))

    def pvpteam_search(self, name, server=None, page=None):
        params = self.__nsp(name, server, page)
        return self.__get('pvpteam/search', params=params)

    def market_price(self, server, item_id):
        return self.__get('market/{}/items/{}'.format(server, item_id))

    def market_price_history(self, server, item_id):
        return self.__get('market/{}/items/{}/history'.format(server, item_id))

    def market_category(self, server, category_id):
        return self.__get('market/{}/category/{}'.format(server, category_id))

    def market_categories(self):
        return self.__get('market/categories')

    def patchlist(self):
        return self.__get('patchlist')

    @staticmethod
    def __nsp(name, server, page):
        p = {'name': name}
        if server:
            params['server'] = server
        if page:
            params['page'] = page

        return p
