import unittest
from datetime import timedelta

import datetime_utils
import sjPomotodo


class MyTestCase(unittest.TestCase):
    token = None

    def setUp(self):
        super(MyTestCase, self).setUp()

        separator = "="
        keys = {}

        # I named your file conf and stored it
        # in the same directory as the script
        with open('pomotodo.properties') as f:

            for line in f:
                if separator in line:
                    # Find the name and value by splitting the string
                    name, value = line.split(separator, 1)

                    # Assign key value pair to dict
                    # strip() removes white space from the ends of strings
                    keys[name.strip()] = value.strip()

        print(keys)
        self.token = keys['token']
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

    def test_pomotodo_date(self):
        day_dt = datetime_utils.from_iso8601("2020-05-25T00:00:00+0800")
        started_later_than = datetime_utils.to_utc(day_dt)
        started_earlier_than = started_later_than + timedelta(days=1)

        sjPomotodo.do_main(self.token, started_later_than, started_earlier_than)

        # self.assertEqual(True, False)
        pass


if __name__ == '__main__':
    unittest.main()
