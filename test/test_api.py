import asyncio
import os

import pytest

import xivapi


class TestApi:
    @classmethod
    def setup_class(cls):
        cls.xivapi = xivapi.Client(os.getenv('XIV_API_KEY'), test_mode=True)
        cls.loop = asyncio.get_event_loop()
        cls.run = cls.loop.run_until_complete

    @classmethod
    def teardown_class(cls):
        cls.loop.close()

    def test_search(cls):
        r = cls.run(cls.xivapi.search('aiming'))
        assert r is 200

    def test_lore(cls):
        r = cls.run(cls.xivapi.lore('legendary'))
        assert r is 200

    def test_content(cls):
        r = cls.run(cls.xivapi.content())
        r_i = cls.run(cls.xivapi.content('item'))
        r_i_i = cls.run(cls.xivapi.content('item', 1675))
        assert r is 200
        assert r_i is 200
        assert r_i_i is 200

    def test_schema(cls):
        r = cls.run(cls.xivapi.schema('item'))
        assert r is 200

    def test_server(cls):
        r = cls.run(cls.xivapi.servers())
        r_g = cls.run(cls.xivapi.servers(group=True))
        assert r is 200
        assert r_g is 200

    def test_character(cls):
        _id = 730968
        r = cls.run(cls.xivapi.character(_id))
        r_s = cls.run(
            cls.xivapi.character_search('hagia karahalios', 'Bahamut')
        )
        r_v = cls.run(cls.xivapi.character_verification(_id, '?'))
        r_u = cls.run(cls.xivapi.character_update(_id))
        assert r is 200
        assert r_s is 200
        assert r_v is 200
        assert r_u is 200

    def test_fc(cls):
        r = cls.run(cls.xivapi.freecompany(9231253336202687179))
        r_s = cls.run(
            cls.xivapi.freecompany_search('Firelink Shrine', 'Bahamut')
        )
        assert r is 200
        assert r_s is 200

    def test_ls(cls):
        r = cls.run(cls.xivapi.linkshell(19984723346535274))
        r_s = cls.run(cls.xivapi.linkshell_search('Hangouts', 'Bahamut'))
        assert r is 200
        assert r_s is 200

    def test_pvp(cls):
        _id = 'fe35a6801f223df825c60a090285ab9b15eedb14'
        r = cls.run(cls.xivapi.pvpteam(_id))
        r_s = cls.run(cls.xivapi.pvpteam_search('-DAIGINJO-'))
        assert r is 200
        assert r_s is 200

    def test_market(cls):
        # ! This endpoint has been disabled at this time.
        r_p = cls.run(cls.xivapi.market_price('phoenix', 5))
        r_h = cls.run(cls.xivapi.market_price_history('phoenix', 5))
        r_c = cls.run(cls.xivapi.market_category('phoenix', 10))
        r_cs = cls.run(cls.xivapi.market_categories())
        assert r_p == 500
        assert r_h == 500
        assert r_c == 500
        assert r_cs is 200

    def test_patch(cls):
        r = cls.run(cls.xivapi.patchlist())
        assert r is 200
