import requests
import json
# from .paginator import Paginator


class Client:

    __API_BASE = 'https://xivapi.com/'
    __SUPPORT_LANGUAGE = ['en', 'jp', 'de', 'fr', 'cn', 'kr']
    __CHARACTER_DATA = ['AR', 'FR', 'FC', 'FCM', 'PVP']

    def __init__(self, api_key, test_mode=False, **kwargs):
        self.test_mode = test_mode
        self.params = {**kwargs}
        self.params['key'] = api_key

    def search(self, string=None, **kwargs):
        return self.get('search', params=kwargs)

    def lore(self, string=None, **kwargs):
        return self.get('lore', params=kwargs)

    def content(self, content=None, limit=100, ids=None, **kwargs):
        if not content:
            return self.get('content')

        if limit > 3000:
            limit = 3000
        kwargs['limit'] = limit
        
        if ids:
            kwargs['ids'] = ','.join([str(id) for id in ids])

        return self.get(content, params=kwargs)

    def schema(self, content):
        return self.get('{}/schema'.format(content))

    def servers(self, group=False):
        endpoint = 'servers/dc' if group else 'servers'
        return self.get(endpoint)

    def character(self, id, **kwargs):
        return self.get('character/{}'.format(id), params=kwargs)

    def character_search(self, name, server=None, page=None):
        params = {
            "name": name,
            "server": server,
            "page": page
        }
        return self.get('character/search', params=params)

    def character_verification(self, id):
        return self.get('character/{}/verification'.format(id))

    def character_update(self, id):
        return self.get('character/{}/update'.format(id))

    def freecompany(self, id, **kwargs):
        return self.get('freecompany/{}'.format(id))

    def freecompany_search(self, name, server=None, page=None):
        params = {
            "name": name,
            "server": server,
            "page": page
        }
        return self.get('freecompany/search', params=params)

    def linkshell(self, id, **kwargs):
        return self.get('linkshell/{}'.format(id))

    def linkshell_search(self, name, server=None, page=None):
        params = {
            "name": name,
            "server": server,
            "page": page
        }
        return self.get('linkshell/search')

    def pvpteam(self, id):
        return self.get('pvpteam/{}'.format(id))

    def pvpteam_search(self, name, server=None, page=None):
        params = {
            "name": name,
            "server": server,
            "page": page
        }
        return self.get('pvpteam/search')

    def market_price(self, server, item_id):
        return self.get('market/{}/items/{}'.format(server, item_id))

    def market_price_history(self, server, item_id):
        return self.get('market/{}/items/{}/history'.format(server, item_id))

    def market_category(self, server, category_id):
        return self.get('market/{}/category/{}'.format(server, category_id))

    def market_categories(self):
        return self.get('market/categories')

    def patchlist(self):
        return self.get('patchlist')

    def get(self, endpoint, params=None):
        if not params:
            params = {}

        url = '{}{}'.format(self.__API_BASE, endpoint)
        r = requests.get(url, json={**self.params, **params})

        if self.test_mode:
            return r
        return r.json()