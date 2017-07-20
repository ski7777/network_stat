#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

import os
import time
import threading
from __main__ import *


class main(threading.Thread):
    def __init__(self, name, prop):
        self.modName = name
        self.prop = prop
        self.returnData = {'up': False, 'ping': -1.0}
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        while True:
            start = time.time()
            self.doPing()
            rest = self.prop['interval'] - time.time() + start
            if rest > 0:
                time.sleep(rest)

    def getData(self):
        ret = {}
        for x, y in self.returnData.items():
            ret["_".join([self.modName, x])] = y
        return(ret)

    def ping_avg(self, host):
        try:
            x = os.popen('ping -c ' + str(self.prop['ping']['count']) + ' -i ' + str(self.prop['ping']['server_interval']) + ' ' + host).read().splitlines()
            x = x[len(x) - 1]
            avg = float(x.split('=')[1].split('/')[1])
            return(avg)
        except:
            return(None)

    def doPing(self):
        server_pings = []
        for server in self.prop['ping']['servers']:
            t = self.ping_avg(server)
            if t != None:
                server_pings.append(t)
        if len(server_pings) != 0:
            self.returnData['ping'] = float(round(sum(server_pings) / len(server_pings), 2))
        else:
            self.returnData['ping'] = -1.0
            self.returnData['up'] = False
            return

        if self.returnData['ping'] <= 5000.0:
            self.returnData['up'] = True
        else:
            self.returnData['up'] = False
