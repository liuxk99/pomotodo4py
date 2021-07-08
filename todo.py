# encoding=utf-8
# -------------------------------------------------------------------------------
# Name:        pomo
# Purpose:      python client for pomotodo
#
# Author:      thomas
#
# Created:     07/07/2021
# Copyright:   (c) thomas 2021
# Licence:     <your licence>
# coding=utf-8
# -------------------------------------------------------------------------------
"""
[
  {
    "uuid": "ac753187-2f22-4b5c-b716-f1fcecfb4410",
    "created_at": "2016-08-06T06:48:52.000Z",
    "updated_at": "2016-08-06T06:51:12.000Z",
    "description": "Catch some little Monsters",
    "notice": null,
    "pin": false,
    "completed": false,
    "completed_at": null,
    "repeat_type": "none",
    "remind_time": null,
    "estimated_pomo_count": null,
    "costed_pomo_count": 0,
    "sub_todos": [
      "81921b2e-8b54-46cf-bb47-0d3c3c7e8302",
      "ff59811e-4c53-404f-a842-9590b632616f"
    ]
  }
]
"""
import re

import datetime_utils


class Pomo:
    def __init__(self, uuid, created_at, updated_at, description, pin, completed, completed_at, repeat_type, estimated_pomo_count, costed_pomo_count, started_at, ended_at,
                 local_started_at, local_ended_at, length, abandoned=False, manual=False):
        self._uuid = uuid
        self._created_at = created_at
        self._updated_at = updated_at
        self._description = description
        self._pin = pin

        self._started_at = started_at
        self._ended_at = ended_at
        self._local_started_at = local_started_at
        self._local_ended_at = local_ended_at
        self._length = length
        self._abandoned = abandoned
        self._manual = manual

    def __str__(self):
        uuid = str(self._uuid)
        created_at = self._created_at.isoformat()
        updated_at = self._updated_at.isoformat()
        description = self._description
        started_at = self._started_at.isoformat()
        ended_at = self._ended_at.isoformat()
        local_started_at = self._local_started_at.isoformat()
        local_ended_at = self._local_ended_at.isoformat()
        length = str(self._length)
        abandoned = str(self._abandoned)
        manual = str(self._manual)

        return (u'uuid: %s\n started_at: %s, ended_at: %s\n'
                u' local_started_at: %s, local_ended_at: %s\n'
                u' description: %s\n'
                u' create_at: %s, update_at: %s\n'
                u' length: %s, abandoned: %s, manual: %s\n'
                % (uuid, started_at, ended_at,
                   local_started_at, local_ended_at,
                   description,
                   created_at, updated_at,
                   length, abandoned, manual)).encode("utf-8")

    @staticmethod
    def from_json(e):
        uuid = e[u'uuid']
        created_at = e[u'created_at']
        updated_at = e[u'updated_at']
        description = e[u'description']
        started_at = e[u'started_at']
        ended_at = e[u'ended_at']
        local_started_at = e[u'local_started_at']
        local_ended_at = e[u'local_ended_at']
        length = e[u'length']
        abandoned = e[u'abandoned']
        manual = e[u'manual']

        return Pomo(uuid, datetime_utils.from_iso8601(created_at), datetime_utils.from_iso8601(updated_at), description,
                    datetime_utils.from_iso8601(started_at), datetime_utils.from_iso8601(ended_at),
                    datetime_utils.from_iso8601(local_started_at), datetime_utils.from_iso8601(local_ended_at),
                    length, abandoned, manual)
        pass
