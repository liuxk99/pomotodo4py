import unittest
from datetime import timedelta

import conf
import datetime_utils
import sjPomotodo


class MyTestCase(unittest.TestCase):
    token = None

    def setUp(self):
        super(MyTestCase, self).setUp()

        self.token = conf.load_token()
        pass

    def test_pomotodo_yesterday(self):
        started_earlier_than = datetime_utils.utc_today()
        started_later_than = started_earlier_than - timedelta(days=1)

        sjPomotodo.do_main(self.token, started_later_than, started_earlier_than)

        # self.assertEqual(True, False)
        pass

    def test_pomotodo_today(self):
        started_later_than = datetime_utils.utc_today()

        sjPomotodo.do_main(self.token, started_later_than)

        # self.assertEqual(True, False)
        pass


if __name__ == '__main__':
    unittest.main()
