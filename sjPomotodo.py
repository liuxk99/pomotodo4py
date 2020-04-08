#!bin/env/python
# encoding=utf-8
# -------------------------------------------------------------------------------
# Name:        sjPomotodo
# Purpose:      python client for pomotodo.py
#
# Author:      thomas
#
# Created:     31/03/2020
# Copyright:   (c) thomas 2020
# Licence:     <your licence>
# coding=utf-8
# -------------------------------------------------------------------------------

# if not called as a module
import getopt
import sys
from datetime import timedelta

import datetime_utils
import pomotodo
from activity import Activity, export_file
from pomo import Pomo


def help(cmd):
    print "%s --token=$token " \
          "(--started_later_than=$(iso8601-date) [--started_earlier_than=$(iso8601-date])|--date $(iso8601-date)"\
          % cmd
    sys.exit(1)

    pass


def do_main(token, started_later_than_dt, started_earlier_than = None):
    print "do_main('%s', '%s~%s')" % (token, str(started_later_than_dt), str(started_earlier_than))

    json_items = pomotodo.get_pomos(token, started_later_than_dt, started_earlier_than, True)

    pomos = []
    for e in json_items:
        pomos.append(Pomo.from_json(e))

    # print "%d pomos" % len(pomos)
    # for pomo in pomos:
    #     print pomo

    activities = []
    for e in json_items:
        activities.append(Activity.from_json(e))

    json_items = pomotodo.get_pomos(token, started_later_than_dt, started_earlier_than)
    for e in json_items:
        activities.append(Activity.from_json(e))

    activities.sort(key=Activity.started_time_key)
    print "total %d activities" % len(activities)
    for e in activities:
        print e

    export_file(activities, "trello.md", "YNote.md")
    pass


if __name__ == '__main__':
    # sys.setdefaultencoding('utf8')
    exec_cmd = sys.argv[0]

    print sys.argv[1:]
    if len(sys.argv) < 2:
        help(exec_cmd)

    # parse parameters
    opts = []
    try:
        opts, arg = getopt.getopt(sys.argv[1:], "t:d:",
                                  ["help", "token=", "started_later_than=", "started_earlier_than=",
                                   "date="])
    except getopt.GetoptError:
        print("syntax error")
        help(exec_cmd)

    # print opts
    # print args
    token = None
    started_later_than_dt = datetime_utils.utc_today()
    started_earlier_than = None

    for opt, arg in opts:
        if opt in '--token':
            token = arg
        elif opt in '--started_later_than':
            begin_datetime = datetime_utils.from_iso8601(arg)
            started_later_than_dt = datetime_utils.to_utc(begin_datetime)
        elif opt in '--started_earlier_than':
            end_datetime = datetime_utils.from_iso8601(arg)
            started_earlier_than = datetime_utils.to_utc(end_datetime)
        elif opt in '--date':
            begin_datetime = datetime_utils.from_iso8601(arg)
            started_later_than_dt = datetime_utils.to_utc(begin_datetime)
            started_earlier_than = started_later_than_dt + timedelta(days=1)
        elif opt in '--help':
            help(exec_cmd)

    if token is None:
        print("syntax error")

    do_main(token, started_later_than_dt, started_earlier_than)
    pass
