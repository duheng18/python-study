#!/usr/bin/env python
#coding=utf-8
import configparser

def get_cfg(in_file):
    config=configparser.ConfigParser()
    config.read(in_file)
    return config

cfg=get_cfg("test.cfg")
print(cfg.get("mail_server","smtp_host"))
