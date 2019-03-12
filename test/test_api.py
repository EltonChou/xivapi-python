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

    def test_lodestone(cls):
        r = cls.run(cls.xivapi.lodestone())
        r_news = cls.run(cls.xivapi.lodestone_news())
        r_notice = cls.run(cls.xivapi.lodestone_notices())
        r_mainten = cls.run(cls.xivapi.lodestone_maintenance())
        r_update = cls.run(cls.xivapi.lodestone_updates())
        r_status = cls.run(cls.xivapi.lodestone_status())
        r_wstatus = cls.run(cls.xivapi.lodestone_worldstatus())
        r_db = cls.run(cls.xivapi.lodestone_devblog())
        r_dp = cls.run(cls.xivapi.lodestone_devposts())
        r_dd = cls.run(cls.xivapi.lodestone_deepdungeon())
        r_f = cls.run(cls.xivapi.lodestone_feasts())
        assert r is 200
        assert r_news is 200
        assert r_notice is 200
        assert r_mainten is 200
        assert r_update is 200
        assert r_status is 200
        assert r_wstatus is 200
        assert r_db is 200
        assert r_dp is 200
        assert r_dd is 200
        assert r_f is 200

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
