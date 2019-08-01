#!/usr/bin/env python
#coding=utf-8

from shutil import make_archive
import os

def targz_dir():
    achive_name="myimage"
    root_dir="/Users/duheng/Documents/project/python/190719/image"
    make_archive(achive_name,'gztar',root_dir)

if __name__=="__main__":
    targz_dir()