#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

import subprocess


def executeCMD(cmd, root=False):
    if root:
        cmd = ' '.join(['sudo', cmd])
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return(out, err)
