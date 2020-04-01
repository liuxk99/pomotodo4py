# coding=utf-8
from unittest import TestCase

from pomo import Pomo

json = u'{' \
       u'    "uuid": "26a37b6f-6e69-4a2e-ae79-e9c264a4a653",' \
       u'    "created_at": "2020-03-30T12:25:26.800Z",' \
       u'    "updated_at": "2020-03-30T12:25:26.800Z",' \
       u'    "description": "#生活/行/车(福特·蒙迪欧) \'维修\'·搭火",' \
       u'    "started_at": "2020-03-30T11:59:20.254Z",' \
       u'    "ended_at": "2020-03-30T12:25:26.799Z",' \
       u'    "local_started_at": "2020-03-30T19:59:20.000Z",' \
       u'    "local_ended_at": "2020-03-30T20:25:26.000Z",' \
       u'    "length": 25,' \
       u'    "abandoned": false,' \
       u'    "manual": false' \
       u'}'


class TestPomo(TestCase):
    def test_from_json(self):
        print json
        Pomo.from_json(json)
        # self.fail()
