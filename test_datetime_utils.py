# coding=utf-8
from unittest import TestCase

import datetime_utils


class Test(TestCase):
    def test_utc(self):
        from datetime import datetime
        print datetime.utcnow()
        pass

    def test_datetime(self):
        dt_str = "2020-03-30T11:59:20.254Z"
        dt = datetime_utils.from_iso8601(dt_str)
        print dt

        from dateutil import tz
        tz_local = tz.tzlocal()
        dt2 = dt.astimezone(tz_local)
        print dt2

        pass

    def test_parser(self):
        day = "2020-03-31T00:00:00+08:00"
        local_dt = datetime_utils.from_iso8601(day)
        print local_dt.__class__
        print "1-local datetime: " + local_dt.isoformat()

        utc_dt = datetime_utils.to_utc(local_dt)
        print "2-utc datetime: " + utc_dt.isoformat()
        print utc_dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        dt = datetime_utils.to_local(utc_dt)
        print "3-new datetime: " + dt.isoformat()

        pass

    def test_utc_day(self):
        from datetime import datetime
        dt = datetime.utcnow()
        print dt.strftime("%Y%m%d")
        print dt.isoformat()

        print datetime_utils.to_iso8601(dt)
        pass

    def test_utc_iso(self):
        from datetime import datetime
        from dateutil import tz
        print datetime(2017, 6, 9).isoformat()
        print datetime(2017, 6, 9, tzinfo=tz.tz.gettz('UTC')).isoformat()
        # '2017-06-09T00:00:00+00:00'
        pass

    def test_utc_today(self):
        dt = datetime_utils.utc_today()
        print dt
        pass
