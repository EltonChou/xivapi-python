import os
import unittest

import xivapi


class TestApi (unittest.TestCase):
    def setUp(self):
        self.xivapi = xivapi.Client(os.getenv('XIV_API_KEY'), test_mode=True, snake_case=1)

    def test_search_api(self):
        r = self.xivapi.search(
            indexes="item,achievement,instantcontent",
            body={
                "query": {
                    "bool": {
                        "must": [
                            {
                                "wildcard": {
                                    "NameCombined_en": "*aiming*"
                                }
                            }
                        ],
                        "filter": [
                            {
                                "range": {
                                    "ItemSearchCategory.ID": {
                                        "gt": "1"
                                    }
                                }
                            },
                            {
                                "range": {
                                    "LevelItem": {
                                        "gte": "100"
                                    }
                                }
                            },
                            {
                                "range": {
                                    "LevelItem": {
                                        "lte": "125"
                                    }
                                }
                            }
                        ]
                    }
                },
                "from": 0,
                "size": 10,
                "sort": [
                    {
                        "LevelItem": "desc"
                    }
                ]
            }
        )
        self.assertEqual(r.status_code, 200)

    def test_content_api(self):
        ids = [10,5,24,20]
        r = self.xivapi.content('item', ids=ids)
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main(verbosity=2)
