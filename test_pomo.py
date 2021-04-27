# coding=utf-8
import re
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
        print(json)
        Pomo.from_json(json)
        # self.fail()

    def testcaseActions01(self):
        pomo1 = "#SW/App 'xxx' |2021/04/26"
        print(pomo1)

        pattern = "'.+'"
        print(pattern)

        self.assertIsNotNone((re.search(pattern, pomo1)))
        return

    def testcaseActions02(self):
        pomo1 = u"#生活/日常 '天气<应用:墨迹天气>' |2021/04/26"
        pomo2 = u"#社会/户籍(北京) '积分落户'·申报 |2021年"

        pattern = u"'.+'"
        print(pattern)

        obj = re.search(pattern, pomo1)
        self.assertIsNotNone(obj)
        print(obj)

        obj = re.search(pattern, pomo2)
        self.assertIsNotNone(obj)
        print(obj)

        print(pomo1)
        pat = u"(.+)'.+'(.+)"
        obj = re.match(pat, pomo1)
        if obj:
            print(obj.group(2))

        print(pomo2)
        obj = re.match(pat, pomo2)
        if obj:
            print(obj.group(2))

        return
