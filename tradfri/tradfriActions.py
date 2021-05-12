#!/usr/bin/env python

# file        : tradfri/tradfriActions.py
# purpose     : module for controling status of the Ikea tradfri smart lights
#
# author      : harald van der laan
# date        : 2017/04/10
# version     : v1.1.0
#
# changelog   :
# - v1.1.0      refactor for cleaner code                               (harald)
# - v1.0.0      initial concept                                         (harald)

"""
    tradfri/tradfriActions.py - controlling the Ikea tradfri smart lights

    This module requires libcoap with dTLS compiled, at this moment there is no python coap module
    that supports coap with dTLS. see ../bin/README how to compile libcoap with dTLS support
"""

# pylint convention disablement:
# C0103 -> invalid-name
# pylint: disable=C0103

import sys
import os

global coap
coap = '/usr/local/bin/coap-client'

def tradfri_power_light(tradfri, lightbulbid, value):
    """ function for power on/off tradfri lightbulb """
    path = '/15001/{}'.format(lightbulbid)
    payload = '{ "3311": [{ "5850": %d }] }' % int(value=='on')
    return tradfri.put(path, payload)

def tradfri_dim_light(tradfri, lightbulbid, value):
    """ function for dimming tradfri lightbulb """
    path = '/15001/{}'.format(lightbulbid)
    dim = float(value) * 2.55
    payload = '{ "3311" : [{ "5851" : %s }] }' % int(dim)
    return tradfri.put(path, payload)

def tradfri_color_light(hubip, securityid, lightbulbid, value):
    """ function for color temperature tradfri lightbulb """
    path = '/15001/{}'.format(lightbulbid)
    if value == 'warm':
        payload = '{ "3311" : [{ "5709" : %s, "5710": %s }] }' % ("33135", "27211")
    elif value == 'normal':
        payload = '{ "3311" : [{ "5709" : %s, "5710": %s }] }' % ("30140", "26909")
    elif value == 'cold':
        payload = '{ "3311" : [{ "5709" : %s, "5710": %s }] }' % ("24930", "24684")
    return tradfri.put(path, payload)

def tradfri_power_group(hubip, securityid, groupid, value):
    """ function for power on/off tradfri lightbulb """
    path = '/15004/{}'.format(groupid)
    payload = '{ "3311": [{ "5850": %d }] }' % int(value=='on')
    return tradfri.put(path, payload)

def tradfri_dim_group(hubip, securityid, groupid, value):
    """ function for dimming tradfri lightbulb """
    path = '/15004/{}'.format(lightbulbid)
    dim = float(value) * 2.55
    payload = '{ "3311" : [{ "5851" : %s }] }' % int(dim)
    return tradfri.put(path, payload)
