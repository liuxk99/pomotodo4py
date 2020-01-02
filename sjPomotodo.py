#!bin/env/python
# encoding=utf-8
# -------------------------------------------------------------------------------
# Name:        sjPomotodo
# Purpose:      python client for pomotodo
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
from datetime import datetime


def help(cmd):
    print "%s --token $token [--date $date]" % cmd
    sys.exit(1)

    pass


def do_main(token, date):
    print "do_main('%s', '%s')" % (token, str(date))
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
        opts, arg = getopt.getopt(sys.argv[1:], "t:d:", ["help", "date=", "token="])
    except getopt.GetoptError:
        print("syntax error")
        help(exec_cmd)

    # print opts
    # print args
    token = None
    date = datetime.now()
    for opt, arg in opts:
        if opt in '--token':
            token = arg
        elif opt in '--date':
            date = arg
        elif opt in '--help':
            help(exec_cmd)

    if token is None:
        print("syntax error")

    do_main(token, date)
    pass
