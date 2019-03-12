import asyncio
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

    async def __get(self, endpoint, params=None):
        if not params:
            params = {}
        params = {**self.params, **params}
        result = await super().get(endpoint, params=params)
        return result

    async def search(self, string, **kwargs):
        kwargs['string'] = string
        r = await self.__get('search', kwargs)
        return r

    async def lore(self, string: str):
        r = await self.__get('lore', {'string': string})
        return r

    async def content(self, content=None, ids=None, limit=100, **kwargs):
        endpoint = content if content else 'content'
        if content:
            kwargs['limit'] = limit
            if ids:
                kwargs['id'] = ids
        r = await self.__get(endpoint, params=kwargs)
        return r

    async def schema(self, content):
        r = await self.__get('{}/schema'.format(content))
        return r

    async def servers(self, group=False):
        endpoint = 'servers/dc' if group else 'server'
        r = await self.__get(endpoint)
        return r

    async def character(self, id, **kwargs):
        r = await self.__get('character/{}'.format(id), params=kwargs)
        return r

    async def character_search(self, name, server=None, page=None):
        params = self.__nsp(name, server, page)
        r = await self.__get('character/search', params=params)
        return r

    async def character_verification(self, id, token):
        params = {'token': token}
        r = await self.__get('character/{}/verification'.format(id), params=params)
        return r

    async def character_update(self, id):
        r = await self.__get('character/{}/update'.format(id))
        return r

    async def freecompany(self, id, **kwargs):
        r = await self.__get('freecompany/{}'.format(id))
        return r

    async def freecompany_search(self, name, server=None, page=None):
        params = self.__nsp(name, server, page)
        r = await self.__get('freecompany/search', params=params)
        return r

    async def linkshell(self, id, **kwargs):
        r = await self.__get('linkshell/{}'.format(id))
        return r

    async def linkshell_search(self, name, server=None, page=None):
        params = self.__nsp(name, server, page)
        r = await self.__get('linkshell/search', params=params)
        return r

    async def pvpteam(self, id):
        r = await self.__get('pvpteam/{}'.format(id))
        return r

    async def pvpteam_search(self, name, server=None, page=None):
        params = self.__nsp(name, server, page)
        r = await self.__get('pvpteam/search', params=params)
        return r

    async def market_price(self, server, item_id):
        r = await self.__get('market/{}/items/{}'.format(server, item_id))
        return r

    async def market_price_history(self, server, item_id):
        r = await self.__get('market/{}/items/{}/history'.format(server, item_id))
        return r

    async def market_category(self, server, category_id):
        r = await self.__get('market/{}/category/{}'.format(server, category_id))
        return r

    async def market_categories(self):
        r = await self.__get('market/categories')
        return r

    async def patchlist(self):
        r = await self.__get('patchlist')
        return r

    @staticmethod
    def __nsp(name, server, page):
        p = {'name': name}
        if server:
            params['server'] = server
        if page:
            params['page'] = page

        return p
