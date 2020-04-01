# coding=utf-8
import codecs

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

        return (u'%s [%s - %s]\n%s' % (cur_date, begin_time, end_time, self._description)).encode("utf-8")

    def to_markdown(self):
        begin_date = datetime_utils.from_iso8601(self._begin)
        end_date = datetime_utils.from_iso8601(self._end)
        cur_date = begin_date.strftime("%Y/%m/%d")
        begin_time = begin_date.strftime("%H:%M")
        end_time = end_date.strftime("%H:%M")

        return (u'%s [%s - %s]\n**\\%s**\n---\n' % (cur_date, begin_time, end_time, self._description)).encode("utf-8")

    def to_text(self):
        # to text as YouNote spec.
        begin_date = datetime_utils.from_iso8601(self._begin)
        end_date = datetime_utils.from_iso8601(self._end)
        begin_time = begin_date.strftime("%H:%M")
        end_time = end_date.strftime("%H:%M")

        return (u'%s - %s\n%s\n' % (begin_time, end_time, self._description)).encode("utf-8")

    def to_YNoteMarkdown(self):
        # 转化为有道云笔记Markdown格式.
        begin_date = datetime_utils.from_iso8601(self._begin)
        end_date = datetime_utils.from_iso8601(self._end)
        begin_time = begin_date.strftime("%H:%M")
        end_time = end_date.strftime("%H:%M")

        time_str = u'<font color=gray>%s - %s</font><br>' % (begin_time, end_time)
        activity_str_format_1 = u'%s<br>'
        activity_str_format_2 = u'[%s](%s)<br>'

        activity_str = activity_str_format_1 % (self._description)
        matched = False
        for key in trello_dict.keys():
            if self._description.find(key) >= 0:
                activity_str = activity_str_format_2 % (self._description, trello_dict[key])
                matched = True
                break

        if not matched:
            print '    u"%s": "",' % (self._description)

        return (u'%s\n%s\n' % (time_str, activity_str)).encode("utf-8")

    pass

    @staticmethod
    def from_json(pomo):
        return Activity(pomo['uuid'], pomo['local_started_at'], pomo['local_ended_at'], pomo['description'])

    @staticmethod
    def started_time_key(self):
        return datetime_utils.from_iso8601(self._begin)


def export_file(activities, md_file, note_file):
    print "md_file: %s" % md_file
    print "note_file: %s" % note_file

    out_md = codecs.open(md_file, 'w', 'utf-8-sig')
    out_note = codecs.open(note_file, 'w', 'utf-8-sig')

    i = 0
    for activity in activities:
        if i > 0:
            # print activity.to_markdown()
            out_md.write(activity.to_markdown().decode('utf-8'))
            out_note.write(activity.to_YNoteMarkdown().decode('utf-8'))
        i = i + 1
    out_md.close()
    out_note.close()

    pass
