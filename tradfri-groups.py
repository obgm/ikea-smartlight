#!/usr/bin/env python

# file        : tradfri-groups.py
# purpose     : controlling status from the Ikea tradfri smart groups
#
# author      : harald van der laan
# date        : 2017/04/10
# version     : v1.1.0
#
# changelog   :
# - v1.1.0      refactor for cleaner code                               (harald)
# - v1.0.0      initial concept                                         (harald)

"""
    tradfri-groupss.py - controlling the Ikea Tradfri smart groups

    This module requires libcoap version >= 4.2, with DTLS support.
"""

# pylint convention disablement:
# C0103 -> invalid-name
# C0200 -> consider-using-enumerate
# pylint: disable=C0200, C0103

from __future__ import print_function

import sys
import argparse

from tradfri import tradfriActions, tradfriObject

def parse_args():
    """ function for getting parsed arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', choices=['power', 'brightness', 'color'], required=True)
    parser.add_argument('-g', '--groupid', help='get group ID from tradfri-status.py',
                        required=True)
    parser.add_argument('-v', '--value',
                        help='power: on/off, brightness: 0 - 100', required=True)

    args = parser.parse_args()

    return args

def main():
    """ main function """
    args = parse_args()
    tradfri = tradfriObject.Tradfri()

    if args.action == 'power':
        if args.value == 'on' or args.value == 'off':
            tradfriActions.tradfri_power_group(tradfri, args.groupid, args.value)
        else:
            sys.stderr.write('[-] Tradfri: power state can only be on/off\n')
            sys.exit(1)
    elif args.action == 'brightness':
        if 0 <= int(args.value) <= 100:
            tradfriActions.tradfri_dim_group(tradfri, args.groupid, args.value)
        else:
            sys.stderr.write('[-] Tradfri: dim value can only be between 1 and 100\n')
            sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)
