import os
import unittest

import xivapi


class TestApi (unittest.TestCase):
    def setUp(self):
        self.xivapi = xivapi.Client(os.getenv('XIV_API_KEY'), test_mode=True)

    def test_api(self):
        ch_s = self.xivapi.content()
        self.assertEqual(ch_s.status_code, 200)

if __name__ == "__main__":
    unittest.main(verbosity=2)