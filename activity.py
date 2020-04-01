# coding=utf-8
import datetime_utils
from trello import trello_dict


class Activity:
    def __init__(self, _uuid, _begin, _end, _description):
        self._uuid = _uuid
        self._begin = _begin
        self._end = _end
        self._description = _description

    def __str__(self):
        begin_date = datetime_utils.from_iso8601(self._begin)
        end_date = datetime_utils.from_iso8601(self._end)
        cur_date = begin_date.strftime("%Y/%m/%d")
        begin_time = begin_date.strftime("%H:%M")
        end_time = end_date.strftime("%H:%M")

        return '%s [%s - %s]\n%s' % (cur_date, begin_time, end_time, self._description)

    def to_markdown(self):
        begin_date = datetime_utils.from_iso8601(self._begin)
        end_date = datetime_utils.from_iso8601(self._end)
        cur_date = begin_date.strftime("%Y/%m/%d")
        begin_time = begin_date.strftime("%H:%M")
        end_time = end_date.strftime("%H:%M")

        return '%s [%s - %s]\n**\\%s**\n---\n' % (cur_date, begin_time, end_time, self._description)

    def to_text(self):
        # to text as YouNote spec.
        begin_date = datetime_utils.from_iso8601(self._begin)
        end_date = datetime_utils.from_iso8601(self._end)
        begin_time = begin_date.strftime("%H:%M")
        end_time = end_date.strftime("%H:%M")

        return '%s - %s\n%s\n' % (begin_time, end_time, self._description)

    def to_YNoteMarkdown(self):
        # 转化为有道云笔记Markdown格式.
        begin_date = datetime_utils.from_iso8601(self._begin)
        end_date = datetime_utils.from_iso8601(self._end)
        begin_time = begin_date.strftime("%H:%M")
        end_time = end_date.strftime("%H:%M")

        time_str = '<font color=gray>%s - %s</font><br>' % (begin_time, end_time)
        activity_str_format_1 = '%s<br>'
        activity_str_format_2 = '[%s](%s)<br>'

        activity_str = activity_str_format_1 % (self._description)
        for key in trello_dict.keys():
            if self._description.find(key) >= 0:
                activity_str = activity_str_format_2 % (self._description, trello_dict[key])
                break

        return '%s\n%s\n' % (time_str, activity_str)

    pass
