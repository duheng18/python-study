#!/usr/bin/env python
#coding=utf-8

import subprocess

# print(subprocess.check_output("/Users/duheng/Documents/project/python/190719/file",shell=True))
# print(subprocess.check_output("ls",shell=True))

# print(subprocess.check_call("path",shell=True))
print(subprocess.call("ifconfig -a",shell=True))