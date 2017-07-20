#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

__all__ = ['env', 'executeCMD']

import os
import json
import importlib
import time


from execution import *

env = {}
env['path'] = {}
env['path']['root'] = os.path.dirname(os.path.abspath(__file__))
env['path']['pluginroot'] = os.path.join(env['path']['root'], 'plugins')

data = json.load(open('../config.json'))
print(json.dumps(data, indent=4, sort_keys=True))
for n, m in data['modules'].items():
    modName = 'plugins.' + m['type']
    data['modules'][n]['module'] = importlib.import_module(modName)
    exec('data["modules"][n]["object"] = data["modules"][n]["module"].main(n , m["properties"])')

while True:
    for n, m in data['modules'].items():
        print(n + ":")
        print(json.dumps(m['object'].getData(), indent=4, sort_keys=True))
        print()
    time.sleep(1)
    print()
