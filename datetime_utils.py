# coding=utf-8
import dateutil.parser


def from_iso8601(s):
    d = dateutil.parser.parse(s)
    return d


def to_iso8601(dt):
    return dt.strftime("YYYY-MM-DDTHH:MM:SS.mmmmmmZ")
