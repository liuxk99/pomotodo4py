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
from datetime import timedelta

import requests

API_URL = 'https://api.pomotodo.com/1/pomos'


def get_pomos(token, dt):
    mydt = dt - timedelta(days=1)
    headers = {'Authorization': 'token ' + token}
    parameters = {'started_later_than': mydt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")}
    result = requests.get(API_URL, headers=headers, params=parameters)
    return result.json()
