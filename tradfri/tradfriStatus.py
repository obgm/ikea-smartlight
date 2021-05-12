#!/usr/bin/env python

# file        : tradfri/tradfriStatus.py
# purpose     : getting status from the Ikea tradfri smart lights
#
# author      : harald van der laan
# date        : 2017/04/10
# version     : v1.1.0
#
# changelog   :
# - v1.1.0      refactor for cleaner code                               (harald)
# - v1.0.0      initial concept                                         (harald)

"""
    tradfriStatus.py - module for getting status of the Ikea tradfri smart lights

    This module requires libcoap with dTLS compiled, at this moment there is no python coap module
    that supports coap with dTLS. see ../bin/README how to compile libcoap with dTLS support
"""

# pylint convention disablement:
# C0103 -> invalid-name
# pylint: disable=C0103

import json

from tradfri import tradfriConfig

def tradfri_get_devices(tradfri):
    """ function for getting all tradfri device ids """
    path = '/15001'
    return json.loads(tradfri.get(path))

def tradfri_get_lightbulb(tradfri, deviceid):
    """ function for getting tradfri lightbulb information """
    path = '/15001/{}'.format(deviceid)
    return json.loads(tradfri.get(path))

def tradfri_get_groups(tradfri):
    """ function for getting tradfri groups """
    path = '/15004'
    return json.loads(tradfri.get(path))

def tradfri_get_group(tradfri, groupid):
    """ function for getting tradfri group information """
    path = '/15004/{}'.format(groupid)
    return json.loads(tradfri.get(path))
